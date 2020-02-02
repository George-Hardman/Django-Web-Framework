from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from users import views as user_views


def register(request):
    form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
