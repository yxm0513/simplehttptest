from django.core.management import execute_from_command_line
from django.http import HttpResponse
from django.urls import path

def hello(request):
    return HttpResponse("Hello, Django!")

urlpatterns = [
    path('', hello),
]

if __name__ == "__main__":
    execute_from_command_line()

