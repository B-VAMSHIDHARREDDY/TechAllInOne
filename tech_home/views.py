from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

class HomeView(View):
    template_name = 'home.html'
    def get(self, request):
        return render(request, self.template_name)


class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

class SignupView(View):
    template_name = 'signup.html'

    def get(self, request):
        form = UserCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, self.template_name, {'form': form})
