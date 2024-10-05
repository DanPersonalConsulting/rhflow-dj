from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import update_session_auth_hash, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import SetPasswordForm, PasswordChangeForm, AuthenticationForm
from django.http import HttpResponse, JsonResponse, QueryDict
from django.shortcuts import render, get_object_or_404, redirect
from app.accounts.forms import UserAvatarForm, UserModelForm
from app.accounts.models import User
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.views import PasswordResetCompleteView
from django.contrib.auth.views import PasswordResetView


def login_custom_view(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if not user == None:
			login(request, user)
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
    
    

def update_avatar(request, user_id):
    user = get_object_or_404(User, pk=user_id)

    if request.method == 'PUT':
        data = QueryDict(request.body).dict()
        form = UserAvatarForm(data, request.FILES, instance=user)

        if form.is_valid():
            form.save()
            return redirect('account:editar_perfil')  
    else:
        form = UserAvatarForm(instance=user)

    return render(request, 'accounts/editar_perfil.html', {'form': form})



class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    success_url = reverse_lazy('account:password_reset_done')
    email_template_name = 'registration/password_reset_email.html'
    form_class = PasswordResetForm 
    
    def form_valid(self, form):
        form.save(
            from_email='movebla@movebla.cash', 
            request=self.request
        )
        return super().form_valid(form)

    
class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    success_url = reverse_lazy('account:password_reset_complete')
    form_class = SetPasswordForm


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'


class CustomPasswordChangeView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'registration/password_change.html'
    success_url = reverse_lazy('account:change_password')
    success_message = "Senha alterada com sucesso!"