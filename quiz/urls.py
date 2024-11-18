"""quiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import dashboard

from perguntas.api.viewsets import PerguntaAllViewSet, PerguntaInformaticaViewSet, PerguntaLogicaViewSet, PerguntaDireitoViewSet

from rest_framework import routers


router = routers.DefaultRouter()
router.register('question-all', PerguntaAllViewSet, basename='Pergunta'),
router.register('question-computing', PerguntaInformaticaViewSet, basename='Pergunta-Informatica'),
router.register('question-logica', PerguntaLogicaViewSet, basename='Pergunta-logica'),
router.register('question-direito', PerguntaDireitoViewSet, basename='Pergunta-direito'),

urlpatterns = [
    path('api/v1/', include(router.urls)),

    path('', dashboard),
    path('accounts/', include('accounts.url')),
    path('questoes/', include('perguntas.url')),
    path('resposta/', include('respostas.url')),
    path('summernote/', include('django_summernote.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('admin/', admin.site.urls),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "handlers.views.page_not_404"