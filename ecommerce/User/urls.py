from django.urls import path, re_path
from django.contrib.auth.views import LogoutView
from django.conf import settings
from . import views
app_name = "User"

urlpatterns = [
    # re_path(r'^logout/$', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    re_path('logout/', views.logout_view, name='logout'),
    path("login/", views.login_request, name="login"),
    path("register_user/", views.register_user, name="register_user"),
]