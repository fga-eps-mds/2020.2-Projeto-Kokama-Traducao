from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse

def admin_register(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                user.is_superuser = True
                user.save()
                return redirect('/admin/')
        else:
            form = UserCreationForm()
        return render(request, 'admin_register.html', {'form': form})
    else:
        return HttpResponse('<h1>Page not authorized</h1>', status=401)