from uuid import uuid4
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from app.funcionario.models import Funcionario


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField('Nome completo', max_length=100,)
    username = models.CharField('Username', max_length=50, unique=True,  blank=True)
    email = models.EmailField('Email', unique=True)
    avatar = models.ImageField('Avatar', upload_to='avatars/', blank=True, null=True)
    funcionario = models.ForeignKey(Funcionario, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Funcionario')

    slug = models.SlugField('slug', unique=True, max_length=150)

    is_active = models.BooleanField('Ativo ?', blank=True, default=True)
    is_staff = models.BooleanField('É da Equipe ?', blank=True, default=False)

    date_joined = models.DateTimeField('Data de Cadastro', auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'username']

    class Meta:
        db_table = 'user'  
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['is_active', 'is_staff' ]

    def __str__(self):
        return self.name

    
    def get_short_name(self):
        return str(self.name.split(' ')[0]).capitalize()


    def save(self, **kwargs):
        if not self.id:
            self.slug = uuid4()
        super().save(**kwargs)
