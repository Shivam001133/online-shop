from django.shortcuts import redirect, render
from .forms import UserForms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserForms(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New User {username} have been created")
            return redirect('users:login')
    form = UserForms()
    return render(request, 'users/register.html', {"form": form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')
