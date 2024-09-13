# views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Funcionario
from .forms import FuncionarioForm

class FuncionarioListView(ListView):
    model = Funcionario
    template_name = 'funcionario_list.html'
    context_object_name = 'funcionarios'

class FuncionarioCreateView(CreateView):
    model = Funcionario
    form_class = FuncionarioForm
    template_name = 'funcionario_form.html'
    success_url = reverse_lazy('funcionario-list')

class FuncionarioUpdateView(UpdateView):
    model = Funcionario
    form_class = FuncionarioForm
    template_name = 'funcionario_form.html'
    success_url = reverse_lazy('funcionario-list')

class FuncionarioDeleteView(DeleteView):
    model = Funcionario
    template_name = 'funcionario_confirm_delete.html'
    success_url = reverse_lazy('funcionario-list')

class FuncionarioDetailView(DetailView):
    model = Funcionario
    template_name = 'funcionario_detail.html'
    context_object_name = 'funcionario'
