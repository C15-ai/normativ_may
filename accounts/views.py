import random
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect


from .models import PasswordResetCode
from .forms import RegisterForm, LoginForm, ProfileForm, ForgotPasswordForm, RestorePasswordForm
from .utils import send_email

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            login(request, user)
            return redirect('fighter_list')
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('fighter_list')
    else:
        form = ProfileForm(instance=request.user)

    return render(request, 'accounts/profile.html', {'form': form})





def forgot_password(request):
    form = ForgotPasswordForm(request.POST or None)

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data["username"]

            user = User.objects.filter(username=username).first()

            if user:

                code = random.randint(100000, 999999)

                PasswordResetCode.objects.create(
                    user=user,
                    code=code
                )

                send_email(
                    subject="Reset Password",
                    message=f"Your code is: {code}",
                    recipient_list=[user.email]
                )

                return redirect("restore_password")
    return render(request,"accounts/forgot_password.html",{"form": form})


def restore_password(request):
    form = RestorePasswordForm(request.POST or None)

    if request.method == "POST":

        if form.is_valid():
            code = form.cleaned_data["code"]
            new_password = form.cleaned_data["new_password"]
            confirm_password = form.cleaned_data["confirm_password"]
            if new_password != confirm_password:

                return render(request,"accounts/restore_password.html",{"form": form,"error": "Parol Xato"})

            code_obj = PasswordResetCode.objects.filter(
                code=code,
                is_used=False
            ).first()

            if not code_obj:
               return render(request,"accounts/restore_password.html",{"form": form,"error": "Invalid code"})
            if code_obj.is_expired():
               return render(request,"accounts/restore_password.html",{"form": form,"error": "Code expired"})

            user = code_obj.user
            user.set_password(new_password)
            user.save()
            code_obj.is_used = True
            code_obj.save()
        return redirect("login")
    return render(request,"accounts/restore_password.html",{"form": form})