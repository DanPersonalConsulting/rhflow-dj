from django.shortcuts import render, get_object_or_404, redirect
from .forms import EmpresaForm, OrganizacaoForm, GestorRhForm
from .models import Empresa, Organizacao, GestorRh


def empresa_list(request):
    empresas = Empresa.objects.all()
    return render(request, 'empresa/empresa_list.html', {'empresas': empresas})


def empresa_create(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST, request.FILES)
        if form.is_valid():
            Empresa.objects.create(**form.cleaned_data)
            return redirect('empresa:empresa_list')
    else:
        form = EmpresaForm()
    return render(request, 'empresa/empresa_form.html', {'form': form})


def empresa_update(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    if request.method == 'POST':
        form = EmpresaForm(request.POST, request.FILES, initial={
            'razao_social': empresa.razao_social,
            'nome_fantasia': empresa.nome_fantasia,
            'cnpj': empresa.cnpj,
            'cep': empresa.cep,
            'endereco': empresa.endereco,
            'uf': empresa.uf,
            'cidade': empresa.cidade,
            'bairro': empresa.bairro,
            'numero': empresa.numero,
            'complemento': empresa.complemento,
            'logomarca': empresa.logomarca,
            'cnae': empresa.cnae,
            'porte': empresa.porte,
            'organizacao': empresa.organizacao,
        })
        if form.is_valid():
            for key, value in form.cleaned_data.items():
                setattr(empresa, key, value)
            empresa.save()
            return redirect('empresa_list')
    else:
        form = EmpresaForm(initial={
            'razao_social': empresa.razao_social,
            'nome_fantasia': empresa.nome_fantasia,
            'cnpj': empresa.cnpj,
            'cep': empresa.cep,
            'endereco': empresa.endereco,
            'uf': empresa.uf,
            'cidade': empresa.cidade,
            'bairro': empresa.bairro,
            'numero': empresa.numero,
            'complemento': empresa.complemento,
            'logomarca': empresa.logomarca,
            'cnae': empresa.cnae,
            'porte': empresa.porte,
            'organizacao': empresa.organizacao,
        })
    return render(request, 'empresa/empresa_form.html', {'form': form})


def empresa_delete(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    if request.method == 'POST':
        empresa.delete()
        return redirect('empresa_list')
    return render(request, 'empresa/empresa_confirm_delete.html', {'empresa': empresa})


def organizacao_list(request):
    organizacoes = Organizacao.objects.all()
    return render(request, 'empresa/organizacao_list.html', {'organizacoes': organizacoes})


def organizacao_create(request):
    if request.method == 'POST':
        form = OrganizacaoForm(request.POST)
        if form.is_valid():
            organizacao = Organizacao(
                nome=form.cleaned_data['nome'],
                usuario_admin=form.cleaned_data['usuario_admin']
            )
            organizacao.save()
            return redirect('empresa:organizacao_list')
    else:
        form = OrganizacaoForm()
    return render(request, 'empresa/organizacao_form.html', {'form': form, 'title': 'Criar Organização'})


def organizacao_update(request, pk):
    organizacao = get_object_or_404(Organizacao, pk=pk)
    if request.method == 'POST':
        form = OrganizacaoForm(request.POST, instance=organizacao)
        if form.is_valid():
            organizacao.nome = form.cleaned_data['nome']
            organizacao.usuario_admin = form.cleaned_data['usuario_admin']
            organizacao.save()
            return redirect('empresa:organizacao_list')
    else:
        form = OrganizacaoForm(initial={'nome': organizacao.nome, 'usuario_admin': organizacao.usuario_admin})
    return render(request, 'empresa/organizacao_form.html', {'form': form, 'title': 'Editar Organização'})


def organizacao_delete(request, pk):
    organizacao = get_object_or_404(Organizacao, pk=pk)
    if request.method == 'POST':
        organizacao.delete()
        return redirect('empresa:organizacao_list')
    return render(request, 'empresa/organizacao_confirm_delete.html', {'organizacao': organizacao})
