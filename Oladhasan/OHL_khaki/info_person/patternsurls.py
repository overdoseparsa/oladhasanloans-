from django.urls import path , include 
from django.http import HttpResponse
start_test = lambda req: HttpResponse("this is test page")
urlpatterns = [
    path('test/',  start_test , name="This is for test")
]