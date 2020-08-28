from django.urls import path
from pessoa.views import Home, UserList, Follow, RedirectHome, Registration

urlpatterns = [
    path('', RedirectHome.as_view(), name='home'),
    path('usuarios/', UserList.as_view(), name='usuarios'),
    path('cadastro/', Registration.as_view(), name='registration'),
    path('follow/<int:profile_id>', Follow.as_view(), name='follow'),
    path('<username>/', Home.as_view(), name='perfil'),
]
