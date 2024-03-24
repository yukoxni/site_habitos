from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=200)
    sobrenome = models.TextField(max_length=200)
    email = models.EmailField(max_length=100, unique=True)
    senha_hash = models.CharField(max_length=128)  # Armazenamento do hash da senha

    def set_senha(self, senha):
        self.senha_hash = make_password(senha)

    def verificar_senha(self, senha):
        return check_password(senha, self.senha_hash)


# Create your models here.
