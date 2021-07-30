from django.urls import path
from .views import AccountsCreate, AccountsView, LoginView

urlpatterns = [
    path("accounts/", AccountsCreate.as_view()),
    path("login/", LoginView.as_view()),
    path("mywallet/", AccountsView.as_view())
]