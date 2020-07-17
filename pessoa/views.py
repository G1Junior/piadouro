from django.views.generic.detail import DetailView
from django.contrib.auth.models  import User

class Home(DetailView):
    template_name = 'home.html'
    model = User