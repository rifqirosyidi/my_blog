from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import MyUserRegisterForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = MyUserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account Created Successfully!, You are now able to login')
            form.save()

            return redirect('my_users:login')
    else:
        form = MyUserRegisterForm()

    context = {
        'form': form
    }

    return render(request, 'my_users/register.html', context)


@login_required
def profile(request):
    return render(request, 'my_users/profile.html')
