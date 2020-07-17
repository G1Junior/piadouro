from django.urls import path
from pessoa.views import Home

urlpatterns = [
    path('<pk>/', Home.as_view()),
]