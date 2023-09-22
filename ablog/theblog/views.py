from django.shortcuts import render
from dajngo.views.generic import ListView, DetailView


#def home(request):
#    return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
