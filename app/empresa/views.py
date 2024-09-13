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

