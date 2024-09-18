from django.shortcuts import render, get_object_or_404, redirect
from .forms import FuncionarioForm
from .models import Funcionario


def funcionario_list(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'funcionario/funcionario_list.html', {'funcionarios': funcionarios})

def funcionario_create(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            Funcionario.objects.create(**form.cleaned_data)
            return redirect('funcionario:funcionario_create')
    else:
        form = FuncionarioForm()
    return render(request, 'funcionario/funcionario_form.html', {'form': form})

def funcionario_update(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    if request.method == 'POST':
        form = FuncionarioForm(request.POST, initial={
            'nome': funcionario.nome,
            'matricula': funcionario.matricula,
            'cpf': funcionario.cpf,
            'telefone': funcionario.telefone,
            'data_nascimento': funcionario.data_nascimento,
            'genero': funcionario.genero,
            'raca_cor': funcionario.raca_cor,
            'nacionalidade': funcionario.nacionalidade,
            'escolaridade': funcionario.escolaridade,
            'cep': funcionario.cep,
            'endereco': funcionario.endereco,
            'cidade': funcionario.cidade,
            'uf': funcionario.uf,
            'data_inicio': funcionario.data_inicio,
            'ativo': funcionario.ativo,
            'regime_contrato': funcionario.regime_contrato,
            'motivo_termino': funcionario.motivo_termino,
            'local_de_trabalho': funcionario.local_de_trabalho,
            'gestor': funcionario.gestor.id if funcionario.gestor else None,
        })
        if form.is_valid():
            for key, value in form.cleaned_data.items():
                setattr(funcionario, key, value)
            funcionario.save()
            return redirect('funcionario:funcionario_list')
    else:
        form = FuncionarioForm(initial={
            'nome': funcionario.nome,
            'matricula': funcionario.matricula,
            'cpf': funcionario.cpf,
            'telefone': funcionario.telefone,
            'data_nascimento': funcionario.data_nascimento,
            'genero': funcionario.genero,
            'raca_cor': funcionario.raca_cor,
            'nacionalidade': funcionario.nacionalidade,
            'escolaridade': funcionario.escolaridade,
            'cep': funcionario.cep,
            'endereco': funcionario.endereco,
            'cidade': funcionario.cidade,
            'uf': funcionario.uf,
            'data_inicio': funcionario.data_inicio,
            'ativo': funcionario.ativo,
            'regime_contrato': funcionario.regime_contrato,
            'motivo_termino': funcionario.motivo_termino,
            'local_de_trabalho': funcionario.local_de_trabalho,
            'gestor': funcionario.gestor.id if funcionario.gestor else None,
        })
    return render(request, 'funcionario/funcionario_form.html', {'form': form})


def funcionario_delete(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    if request.method == 'POST':
        funcionario.delete()
        return redirect('funcionario:funcionario_list')
    return render(request, 'funcionario/funcionario_confirm_delete.html', {'funcionario': funcionario})
