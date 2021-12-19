from django.urls import path
from .api.views import QuizList, QuizDetail

urlpatterns = [
    path('<int:pk>/', QuizDetail.as_view()),
    path('', QuizList.as_view()),
]
