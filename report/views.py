from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
# from .models import *
# from .forms import contact_form #NEEDS WORK HERE
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import redirect


def feedback(request):
    if request.method == 'POST':
        form = contact_form()
    else:
        form = contact_form(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            content = form.cleaned_data['content']
            try:
                send_mail(email, name, content, [
                          'californiamikegreen@yahoo.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "contact.html", {'form': form})


def success(request):
    return HttpResponse('Success! Thank you for your message.')
