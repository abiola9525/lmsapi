from django.urls import path
from feedback.views import FeedBack


urlpatterns = [
    path('', FeedBack.as_view()),
   
] 
