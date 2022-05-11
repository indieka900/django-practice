from django.urls import path
from . import views
app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.Detailview.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('creat-question/', views.createQuestion, name="create_question"),
    path('<str:pk>/update-question/', views.updateQuiz, name="update_question"),
    path('<str:pk>/create-choice/', views.createChoice, name="create-choice"),
    path('<str:pk>/delete-question/', views.deleteQuiz, name="delete_question")
]