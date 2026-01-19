from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path(
        "password_change/",
        auth_views.PasswordChangeView.as_view(
            template_name="accounts/registration/password_change_form.html"
        ),
        name="password_change",
    ),
    path(
        "password_change/done/",
        auth_views.PasswordChangeDoneView.as_view(
            template_name="accounts/registration/password_change_done.html"
        ),
        name="password_change_done",
    ),
]
