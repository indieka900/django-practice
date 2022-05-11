from django.forms import ModelForm
from .models import Question,Choice

class Questionform(ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
class Choiceform(ModelForm):
    class Meta:
        model = Choice
        fields = '__all__'
        exclude = ['votes']