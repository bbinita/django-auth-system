from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.core.mail import EmailMessage
from django.template.loader import render_to_string



# Create your views here.
def index(request):
    return render(request, 'index.html', {'title': 'index'})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            
            # Send welcome email with better error handling
            try:
                htmly = get_template('email.html')
                d = {'username': username}
                subject = 'Welcome to Our Platform'
                from_email = 'bbhusal394@gmail.com'
                to = email
                html_content = htmly.render(d)
                
                msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
                msg.attach_alternative(html_content, 'text/html')
                msg.send()
                
                print(f"✓ Email sent successfully to {email}")
                messages.success(request, f'Your account has been created! Check your email for welcome message.')
            except Exception as e:
                print(f"✗ Email sending failed: {str(e)}")
                messages.success(request, f'Your account has been created! You are now able to login')
            
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form, 'title': 'register here'})


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome {username}!!')
            return redirect('index')
        else:
            messages.error(request, f'Account does not exist. Please sign up first.')
    
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form, 'title': 'log in'})


def logout_view(request):
    logout(request)
    return render(request, 'logout.html')


def test_email(request):
    """Test email functionality"""
    from django.core.mail import send_mail
    from django.conf import settings
    
    try:
        print("=" * 50)
        print("EMAIL SETTINGS:")
        print(f"EMAIL_HOST_USER: {settings.EMAIL_HOST_USER}")
        print(f"EMAIL_HOST_PASSWORD length: {len(settings.EMAIL_HOST_PASSWORD)} characters")
        print(f"EMAIL_HOST_PASSWORD has spaces: {' ' in settings.EMAIL_HOST_PASSWORD}")
        print(f"EMAIL_HOST: {settings.EMAIL_HOST}")
        print(f"EMAIL_PORT: {settings.EMAIL_PORT}")
        print("=" * 50)
        
        send_mail(
            'Test Email from Django',
            'If you receive this, email is working!',
            settings.EMAIL_HOST_USER,
            ['bbhusal394@gmail.com'],
            fail_silently=False,
        )
        print("✓ Email sent successfully!")
        messages.success(request, 'Test email sent! Check your inbox.')
    except Exception as e:
        print(f"✗ Email failed: {str(e)}")
        messages.error(request, f'Email failed: {str(e)}')
    
    return redirect('index')