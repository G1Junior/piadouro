from django.forms import ModelForm, inlineformset_factory, CharField, PasswordInput, Select
from django.contrib.auth.models import User
from pessoa.models import Perfil

class UserForm(ModelForm):
    password2 = CharField(max_length=60, required=True, widget=PasswordInput ())
    class Meta:
        model = User
        exclude = ['is_staff', 'is_active', 'date_joined', 'last_login',
         'groups', 'user_permissions', 'id_superuser',]
        widgets = { 
             'password': PasswordInput()
         }


# class ProfileForm(ModelForm):

#     class meta:
#         model = Perfil
#         exclude = ['usuario']
class UserProfileForm(ModelForm):
    class Meta:
        model = Perfil
        exclude = ['usuario']