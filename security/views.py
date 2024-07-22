from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, PasswordResetView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy


# Widok rejestracji
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('homepage')
    else:
        form = UserCreationForm()
    return render(request, 'security/register.html', {'form': form})


# Widok logowania
class CustomLoginView(LoginView):
    template_name = 'security/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('dashboard:homepage')

# Widok przypomnienia hasła
class CustomPasswordResetView(PasswordResetView):
    template_name = 'security/password_reset.html'
    success_url = reverse_lazy('security:password_reset_done')
