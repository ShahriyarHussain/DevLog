from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import Feedback
from .forms import FeedbackForm  # NEEDS WORK HERE
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import redirect


def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm()
    else:
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # email = form.cleaned_data['email']
            # name = form.cleaned_data['name']
            content = form.cleaned_data['content']
            form.save()
            try:
                send_mail('An Issue Occured', content, 'shossainshihab36@gmail.com', [
                    'md.shahriyar.hossain@g.bracu.ac.bd'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('feedback-success')
    return render(request, "report/feedback.html", {
        'form': form,
        'title': 'Report A Problem'
    })


def success(request):
    return render(request, "report/success.html")
