from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
import os

def user_directory_path(instance, filename):
    """
    Define o caminho onde os arquivos serão salvos no S3, organizados por usuário.
    Exemplo: 'users/user-email-com/meuarquivo.pdf'
    """
    email_slug = instance.email.replace("@", "-at-").replace(".", "-")  # Garante unicidade
    ext = filename.split('.')[-1]  # Pega a extensão do arquivo
    new_filename = f"{uuid.uuid4()}.{ext}"  # Nome único para evitar sobrescrições
    return os.path.join("users", email_slug, new_filename)


class CostumerUser(AbstractUser):
    sexo = models.CharField(max_length=15, blank=True, null=True, default=None)
    biografia = models.TextField(blank=True)
    imagem = models.ImageField(blank=True, null=True, upload_to=user_directory_path)

    def get_file_url(self):
        """Retorna a URL da imagem ou um placeholder caso esteja vazia."""
        if self.imagem:  # Evita erro caso a imagem esteja vazia
            return self.imagem.url
