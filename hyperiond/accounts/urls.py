# accounts/urls.py

# Import the necessary module for URL routing
from django.urls import path

# Import the SignUpView from the current directory's views module
from .views import SignUpView

# Define the URL patterns for the accounts app
urlpatterns = [
    # Route for the signup page
    # When a user navigates to /signup/, the SignUpView will be called
    # and the name 'signup' can be used to refer to this URL pattern elsewhere in the project
    path("signup/", SignUpView.as_view(), name="signup"),
]
