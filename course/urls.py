from django.urls import path
from .views import CourseInfo


urlpatterns = [
    path('', CourseInfo.as_view()),
   
] 
