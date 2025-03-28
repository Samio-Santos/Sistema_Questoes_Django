from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib import messages
from perguntas.models import Pergunta
from categorias.models import Materia, Banca

class TestPerguntasViews(TestCase):
    def setUp(self):
        """Configura o ambiente de teste"""
        self.client = Client()
        self.factory = RequestFactory()
        
        # Criar usuário
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@test.com',
            password='testpass123'
        )
        
        # Criar matéria e banca
        self.materia = Materia.objects.create(materia='Test Subject')
        self.banca = Banca.objects.create(banca='Test Bank')
        
        # Criar pergunta
        self.pergunta = Pergunta.objects.create(
            enunciado='Test question',
            materia=self.materia,
            banca=self.banca
        )

    def test_perguntas_view_authenticated(self):
        """Testa se usuário logado pode ver as perguntas"""
        request = self.factory.get(reverse('perguntas:categoria_materia', kwargs={'materia': 'Test Subject'}))
        self.client.login(username='testuser', password='testpass123', request=request)
        response = self.client.get(reverse('perguntas:categoria_materia', kwargs={'materia': 'Test Subject'}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'perguntas_templates/index.html')

    def test_perguntas_view_unauthenticated(self):
        """Testa se usuário não logado é redirecionado"""
        response = self.client.get(reverse('perguntas:categoria_materia', kwargs={'materia': 'Test Subject'}))
        self.assertEqual(response.status_code, 302)

    def test_questoes_nao_resolvidas(self):
        """Testa a view de questões não resolvidas"""
        request = self.factory.get(reverse('perguntas:nao_resolvidas', kwargs={'materia': 'Test Subject'}))
        self.client.login(username='testuser', password='testpass123', request=request)
        response = self.client.get(reverse('perguntas:nao_resolvidas', kwargs={'materia': 'Test Subject'}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'perguntas_templates/index.html')

    def test_filtro_banca(self):
        """Testa o filtro por banca"""
        request = self.factory.get(reverse('perguntas:filtro_banca', kwargs={'banca': 'Test Bank', 'materia': 'Test Subject'}))
        self.client.login(username='testuser', password='testpass123', request=request)
        response = self.client.get(reverse('perguntas:filtro_banca', kwargs={'banca': 'Test Bank', 'materia': 'Test Subject'}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'perguntas_templates/index.html')

    def test_deletar_questoes(self):
        """Testa a funcionalidade de deletar questões"""
        request = self.factory.post(reverse('perguntas:deletar_questoes_resolvidas'))
        self.client.login(username='testuser', password='testpass123', request=request)
        response = self.client.post(
            reverse('perguntas:deletar_questoes_resolvidas'),
            {'pergunta_id': self.pergunta.id}
        )
        self.assertEqual(response.status_code, 302)  # Redirecionamento após deletar 