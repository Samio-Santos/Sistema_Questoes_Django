from django import urls
from django.db import router
from django.test import TestCase, Client, RequestFactory
from django.urls import reverse_lazy, reverse
from django.urls.conf import path
from categorias.models import *
from accounts.models import CostumerUser
from accounts.form import Userform
from respostas.models import Resposta
from perguntas.models import Pergunta
from social_django.models import UserSocialAuth
from model_mommy import mommy
from django.contrib.auth import get_user_model


class LoginViewTestcase(TestCase):

    def setUp(self):
        self.user = CostumerUser.objects.create_user(username='isco@gmail.com', email='', password='')

        self.user1 = CostumerUser.objects.create_user(username='bale@gmail.com', email='bale@gmail.com', password='bale1234')

        self.user_social = UserSocialAuth.objects.create(user=self.user, uid=self.user.username, provider='google-oauth2')

        self.validos = {
            'user': 'bale@gmail.com',
            'password': 'bale1234'
        }

        self.invalidos = {
            'user': 'bale@gmail.com',
            'password': 'bale1'
        } 
        
        self.usuario_não_existi = {
            'user': 'bal@gmail.com',
            'password': 'bale1'
        }

        self.redeSocial = {
            'user': self.user.email,
            'password': 'S@my67'
        }
    
        self.cliente = Client()

    def test_methodPost_login(self):
        self.cliente.get(reverse_lazy('login'), data=self.validos)

    def test_loginValido(self):
        self.cliente.post(reverse_lazy('login'), data=self.validos)

    def test_loginInvalido(self):
        self.cliente.post(reverse_lazy('login'), data=self.invalidos)

    def test_loginRedesocial(self):
        self.client.post(reverse_lazy('login'), data=self.redeSocial)

    def test_loginUsuario_não_existi(self):
        self.cliente.post(reverse_lazy('login'), data=self.usuario_não_existi)


class LogoutViewTestcase(TestCase):

    def setUp(self):
        self.cliente = Client()

        self.user = mommy.make('CostumerUser')

        self.dados = {
            'user': self.user.email,
            'password': self.user.password
        }

        self.cliente.post(reverse_lazy('logout'), data=self.dados)


    def test_logout(self):
        self.cliente.logout()


class RegisterViewTestcase(TestCase):
    def setUp(self):
        
        self.user = CostumerUser.objects.create_user(username='Betty-Santiago', email='ro@vu.com', sexo='Feminino', password='B@tyy12343', first_name='Betty', last_name='Santiago')
    

        self.validos = {
            'nome':'Ricky',
            'Snome': 'Wong',
            'email': 'voh@gmail.com',
            'sexo': 'Masculino',
            'password': 'M@my46667',
            'Rsenha':'M@my46667'
        }

        self.cliente = Client()


    def test_methodPost_register(self):
        self.cliente.get(reverse_lazy('register'), data=self.validos)

    def test_dados_register(self):
        self.cliente.post(reverse_lazy('register'), data=self.validos)
    
    def test_get_validacao_dados_register(self):
        dados_invalidos = {
            'nome':'',
            'Snome': 'Wong',
            'email': 'vohtu.org',
            'sexo': 'Masculino',
            'password': 'molpafa',
            'Rsenha':'Nolpafa'
        }
        self.cliente.post(reverse_lazy('register'), data=dados_invalidos)
    

class DashboardViewTestcase(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        
        # Criar usuário
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@test.com',
            password='testpass123'
        )
        
        # Criar matéria (se necessário para o teste)
        self.materia = Materia.objects.create(materia='Português')

    def test_dashboard(self):
        request = self.factory.get(reverse('dashboard'))
        self.client.login(
            username='testuser',
            password='testpass123',
            request=request
        )
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts_templates/dashboard.html')


class PerfilViewTestcase(TestCase):
    def setUp(self):

        self.cliente = Client()
        
        self.user = CostumerUser.objects.create_user(username='bale@gmail.com', email='bale@gmail.com', password='bale1234', first_name='Garet', last_name='Bale')

        self.urlPerfil = reverse_lazy('perfil_user', kwargs={'id': self.user.id})

        self.dados = {
            'first_name': self.user.first_name, 
            'last_name': self.user.last_name, 
            'email': self.user.email, 
            'sexo': 'Masculino'
        }

        self.validos = {
            'user': 'bale@gmail.com',
            'password': 'bale1234'
        }


        self.form = Userform(data=self.dados)

        self.cliente.post(reverse_lazy('login'), self.validos)



    def test_Url_Perfil_usuario(self):
        self.cliente.post(f'/accounts/perfil/2/')

    def test_methodPost_Perfil_usuario(self):
        self.cliente.get(self.urlPerfil)

    def test_perfil(self):
        self.cliente.post(self.urlPerfil, data=self.dados)

class lockedViewTestcase(TestCase):
    def setUp(self):
        self.cliente = Client()

    # depois de 5 tentativas erradas do usuario o usuario é bloqueado.
    def test_tela_bloqueio_usuario(self):
        self.cliente.post(reverse_lazy('locked'))
        
class Reset_Password_CompleteViewTestcase(TestCase):
    def setUp(self):
        self.cliente = Client()

    # depois de 5 tentativas erradas do usuario o usuario é bloqueado.
    def test_password_reset_complete(self):
        self.cliente.post(reverse_lazy('password_reset_complete'))