from django.urls import path,include
from .import views

urlpatterns = [
    
    path('',views.Chatbot,name='chatbot'),
    path('get',views.get_bot_response,name="response"),
    
    
]
