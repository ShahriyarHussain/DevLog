from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm


# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account Creation Successful! Username: {username}')
            return redirect('login')
        # else:
        #     messages.info(
        #         request, f'Invalid Password')
        #     return redirect('blog-home')

    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {
        'form': form,
        'title': 'Oblog- Register'
    })


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Profile Updated!')
            return redirect('profile')
        else:
            messages.warning(request, f'No Changes Made')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'title': 'Your Profile'
    }
    return render(request, 'users/profile.html', context)
