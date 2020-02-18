from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import MyUserRegisterForm, MyUserUpdateForm, MyProfileUpdateForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = MyUserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account Created Successfully!, You are now able to login')
            form.save()

            return redirect('login')
    else:
        form = MyUserRegisterForm()

    context = {
        'form': form
    }

    return render(request, 'my_users/register.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = MyUserUpdateForm(request.POST, instance=request.user)
        p_form = MyProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Profile Updated')
            return redirect('profile')

    else:
        u_form = MyUserUpdateForm(instance=request.user)
        p_form = MyProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'my_users/profile.html', context)
