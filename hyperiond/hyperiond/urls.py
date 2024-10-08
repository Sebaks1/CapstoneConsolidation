from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView  # new

urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html"), name="home"),  # new
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),  # new
    path('blog/', include('blog.urls')),
    path('polls/', include('polls.urls')),
    path('user_auth/', include("django.contrib.auth.urls")),
    path('band', include('band.urls')),
]
