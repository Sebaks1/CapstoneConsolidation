from django.shortcuts import render
# Imports the render function, which is used to render templates and return an HTTP response.

from django.contrib.auth import authenticate, login
# Imports the authenticate and login functions from Django's authentication framework. 
# authenticate checks if a user's credentials are valid, and login logs in a user by creating a session.

from django.http import HttpResponse, HttpResponseRedirect
# Imports HttpResponse and HttpResponseRedirect, which are used to return a simple HTTP response 
# or redirect the user to another URL, respectively.

from django.urls import reverse
# Imports the reverse function, which is used to generate URLs from the URL patterns defined in your Django project.

# Create your views here.
# This is a placeholder comment created by Django when a new app is generated. It indicates where view functions should be defined.


def user_login(request):
  # This view handles displaying the login form.

  return render(request, 'authentication/login.html')
  # The render function takes the request object and the template name as arguments, 
  # and returns an HttpResponse object with that rendered template. This will display the login page to the user.


def authenticate_user(request):
  # This view handles the authentication process when the user submits the login form.

  username = request.POST['username']
  password = request.POST['password']
  # Retrieves the username and password from the POST request. 
  # These are the credentials entered by the user in the login form.

  user = authenticate(username=username, password=password)
  # The authenticate function checks if the provided username and password match a user in the database. 
  # If the credentials are correct, it returns a User object; otherwise, it returns None.

  if user is None:
    # If the user object is None, it means the authentication failed (invalid credentials).
    
    return HttpResponseRedirect(
      reverse('user_auth:login')
    )
    # Redirects the user back to the login page using HttpResponseRedirect. 
    # The reverse function is used to avoid hardcoding the URL; it looks up the URL by its name ('user_auth:login').
  
  else:
    # If the authentication is successful (user is not None):
    
    login(request, user)
    # Logs in the user by creating a session. The user will now be considered "authenticated" for subsequent requests.

    return HttpResponseRedirect(
      reverse('user_auth:show_user')
    )
    # Redirects the user to the show_user view, which will display the user's information. 
    # Again, reverse is used to look up the URL by its name ('user_auth:show_user').


def show_user(request):
  # This view displays the authenticated user's information.

  print(request.user.username)
  # Prints the username of the logged-in user to the console. This is primarily for debugging purposes.

  return render(request, 'authentication/user.html', {
    "username": request.user.username,
    "password": request.user.password
  })
  # Renders the user.html template and passes the username and password of the authenticated user to the template context.
  # The context is a dictionary where the keys are the variable names that can be used in the template, 
  # and the values are the corresponding data.
