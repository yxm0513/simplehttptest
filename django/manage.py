from django.core.management import execute_from_command_line
from django.http import HttpResponse
from django.urls import path

from django.conf import settings

# Set up basic settings
settings.configure(
    DEBUG=True,
    SECRET_KEY='your_secret_key',
    INSTALLED_APPS=[
        'django.contrib.auth',
        'django.contrib.contenttypes',
    ],
)


def hello(request):
    return HttpResponse("Hello, Django!")

urlpatterns = [
    path('', hello),
]

if __name__ == "__main__":
    execute_from_command_line()

