from email.message import EmailMessage
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from .forms import UserRegisterationForm
from ..core import settings
from django.template.loader import render_to_string
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            
            send_mail(
                subject="New User Registration",
                message = f'User {form.cleaned_data["username"]} has registered with email {form.cleaned_data["email"]}',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.ADMIN_EMAIL]
            )
            html_content = render_to_string(
                "emails/user_welcome.html",
                {"username": form.cleaned_data['username']}
            )
            email = EmailMessage(
                subject="Welcome to Our Site",
                body=html_content,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[form.cleaned_data['email']],
                cc = [settings.ADMIN_EMAIL],
            )
            email.content_subtype = "html"
            email.send()
            return redirect('login')
        else:
            form = UserRegisterationForm()
    return render(request, 'users/registration.html', {'form': form})  
        



    