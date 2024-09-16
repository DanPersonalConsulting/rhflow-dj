import json
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import SetPasswordForm, PasswordChangeForm, AuthenticationForm
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
#from app.accounts.forms import PasswordResetForm
#from app.accounts.models import PasswordReset
from app.accounts.forms import UserModelForm
from app.accounts.models import User


def login_custom_view(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if not user == None:
			is_first_login = user.last_login
			login(request, user)
			if not is_first_login:
				return redirect('base:first-access', user.slug)
			else:
				return redirect('base:home')
		else:
			form_login = AuthenticationForm()
	else:
		form_login = AuthenticationForm()

	context = {
		'form': form_login
	}
	return render(request, 'registration/login.html', context)

@login_required
def logout_custom_view(request):
	logout(request)
	return redirect('account:login')


@login_required
def editar_perfil(request):
    profile = request.user
    if request.method == 'POST':
        form = UserModelForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Perfil atualizado com sucesso!'}, status=200)
    else:
        form = UserModelForm(instance=profile)
    
    return render(request, 'accounts/editar_perfil.html', {'form': form})
    