from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm


# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def courses(request):
    return render(request, 'courses.html')


def trainers(request):
    return render(request, 'trainers.html')


def events(request):
    return render(request, 'events.html')


def contact(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save()
            return redirect('contact')
    else:
        form = MessageForm()
    return render(request, 'contact.html', {'form': form})

