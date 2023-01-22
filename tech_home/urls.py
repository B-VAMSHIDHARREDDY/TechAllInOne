from django.urls import path
from .views import LoginView, SignupView,HomeView





urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
]
