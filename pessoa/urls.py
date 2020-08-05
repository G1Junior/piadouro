from django.urls import path
from pessoa.views import Home, UserList

urlpatterns = [
    path('usuarios/', UserList.as_view(), name='usuarios'),
    path('<username>/', Home.as_view(), name='perfil'),
]
