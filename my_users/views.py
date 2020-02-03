from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import MyUserRegisterForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = MyUserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}')
            form.save()

            return redirect('my_blog:home')
    else:
        form = MyUserRegisterForm()

    context = {
        'form': form
    }
    return render(request, 'my_users/register.html', context)

