from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect,render
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from .form import Questionform, Choiceform
from .models import Choice,Question

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        """Return the last five published questions. """
        return  Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')

class Detailview(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #redisplay the question voting form
        return render(request, 'polls/detail.html',{
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        #always return HttpResponseRedirect after succesfully dealing
        #with POST data This prevents data
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
def createQuestion(request):
    form = Questionform()
    if request.method == 'POST':
        form = Questionform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
            
    context = {"form":form}
    return render(request, 'polls/form.html', context)


def createChoice(request, pk):
    choice = Choice.objects.get(id=pk)
    form = Choiceform(instance=choice)
    if request.method == 'POST':
        form = Choiceform(request.POST, instance=choice)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'polls/form.html', context)

def updateQuiz(request, pk):
    question = Question.objects.get(id=pk)
    form = Questionform(instance=question)
    if request.method == 'POST':
        form = Questionform(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'polls/form.html', context)

def deleteQuiz(request,pk):
    question = Question.objects.get(id=pk)
    if request.method == 'POST':
        question.delete()
        return redirect('/')
    return render(request, 'polls/delete.html', {"obj":question})
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
# Create your views here.
