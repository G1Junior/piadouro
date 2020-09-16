from django.urls import path

from pessoa.views import (Follow, Home, ProfileEditor, RedirectHome,
                          Registration, UserList)

urlpatterns = [
    path('', RedirectHome.as_view(), name='home'),
    path('cadastro/', Registration.as_view(), name='registration'),
    path('editor-perfil/', ProfileEditor.as_view(), name='profile-editor'),
    path('usuarios/', UserList.as_view(), name='usuarios'),
    path('seguir/<int:user_id>', Follow.as_view(), name='follow'),
    path('<username>/', Home.as_view(), name='perfil'),
]
