from django.shortcuts import render
from django.contrib.auth.views import LoginView 
from forms.forms import RegisterForm, AdminFormRegister
from django.shortcuts import redirect
from django.contrib.auth.forms import  AuthenticationForm
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.decorators import login_required



class AuthView(LoginView):
    template_name = 'auth.html'


@login_required()
def index(request):
    return render(request, 'index.html')

@ensure_csrf_cookie  
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

@ensure_csrf_cookie
def admin_register_view(request):
    if request.method == 'POST':
        form = AdminFormRegister(request.POST)
        if form.is_valid():
            secret_token = form.cleaned_data.get('secret_token')
            if secret_token == 'SECRET123':
                form.save()
                return redirect('index')
            else:
                form.add_error('secret_token', 'Invalid secret token.')
    else:
        form = AdminFormRegister()
    return render(request, 'admin.html', {'form': form})