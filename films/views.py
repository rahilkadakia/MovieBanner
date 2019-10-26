from django.shortcuts import render, redirect
from .forms import MovieForm
from .models import Movie

def index(request):
    Movie.movie_name = request.POST.get('movie_name', False)
    return render(request, 'films/index.html', {'Movie Name': Movie.movie_name})

def Create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('index')
    form = MovieForm()
    context = {
        'form': form
    }
    return render(request, 'films/create.html', context)
