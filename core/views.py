from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import SignupForm

def frontpage(request):
    return render(request, 'core/frontpage.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request,user)

            return redirect('frontpage')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {'form': form})    

from django.contrib.auth.views import LogoutView
from django.http import HttpResponseRedirect
from django.urls import reverse

class LogoutViewAllowGet(LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
