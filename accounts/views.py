from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views import View
from .forms import CustomUserCreationForm

class SignupView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, "accounts/signup.html", {"form": form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("diary:index")  # 適切なリダイレクト先を確認
        return render(request, "accounts/signup.html", {"form": form})

signup_view = SignupView.as_view()
