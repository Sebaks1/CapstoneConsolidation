# accounts/views.py

# Import the UserCreationForm, a built-in form that handles user creation (registration)
from django.contrib.auth.forms import UserCreationForm

# Import reverse_lazy, a function that resolves URLs lazily, used here to redirect after successful form submission
from django.urls import reverse_lazy

# Import CreateView, a generic view that handles the creation of objects (like new user accounts)
from django.views.generic import CreateView


# Define a SignUpView class that handles the user registration process
class SignUpView(CreateView):
    # Specify the form class to use for user registration
    form_class = UserCreationForm
    
    # Define the URL to redirect to after a successful sign-up
    # reverse_lazy is used instead of reverse to avoid evaluating the URL until it’s needed
    success_url = reverse_lazy("login")
    
    # Specify the template to render the sign-up form
    template_name = "registration/signup.html"
