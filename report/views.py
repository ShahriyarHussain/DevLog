from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
# from .models import Feedback
from .forms import FeedbackForm
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import redirect


def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            # name = form.cleaned_data['name']
            # email = form.cleaned_data['email']
            # subject = form.cleaned_data['subject']
            # content = 'from' + name + ':' + form.cleaned_data['details']
            # # to_mail = 'shossainshihab36@gmail.com'
            # try:
            #     send_mail(subject, content, [
            #               email, 'shossainshihab36@gmail.com'], fail_silently=False)
            # except BadHeaderError:
            #     return HttpResponse('Invalid header found.')
            return redirect('feedback_success')
    else:
        form = FeedbackForm()
    return render(request, "report/feedback.html", {
        'form': form,
        'title': 'Feedback'})


def success(request):
    return render(request, 'report/feedback_success.html')
