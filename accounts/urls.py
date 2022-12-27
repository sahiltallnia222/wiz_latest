
from django.urls import path
from . import views

app_name='accounts'

urlpatterns = [
    path('register/',views.register_user,name='register'),
    path('activate-account/',views.activate_account,name='activate_account'),
    path('deactivate-account/',views.deactivate_account,name='deactivate_account'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('activate/<uidb64>/<token>/',views.activate,name='activate'),
    path('forgot_password/',views.forgot_password,name='forgot_password'),
    path('reset_password_validate/<uidb64>/<token>/',views.reset_password_validate,name='reset_password_validate'),
    path('reset_password/',views.reset_password,name='reset_password'),
]