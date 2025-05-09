from django.urls import path
from .views import *

urlpatterns = [
    path('login/', Login.as_view(), name='Login'), 
    path('professor/', ProfessorListCreateApiView.as_view(), name='criarListarPROFESSOR'),  
    path('usuarios/', UsuarioCreateAPIView.as_view(), name='criar_usuario'),
    path('professor/<int:pk>/', ProfessorRetrieveUpdateDestroy.as_view(), name = 'atualizarProfessor'),
    path('MinhasDisciplinas/' , Disciplinas.as_view(), name = 'verDisiciplinas'),
    path('MinhasReservas/' , MinhasReservas.as_view(), name ='verReservas'  ),
    path('reservarAmbientes/', ReservadeAmbientesListCreateApiView.as_view(), name='reservar')
]
