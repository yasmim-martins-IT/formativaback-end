from django.shortcuts import render
from .models import Reservar_de_Ambiente, Professor, Disciplina, Usuario
from .serializers import LoginSerializer,ProfessorSerializer,UsuarioSerializer,ReservaAmbientesSerializer,DisciplinaSerializer
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .permissions import IsGestor, IsProfessor
from rest_framework.response import Response
from rest_framework import status


class Login(TokenObtainPairView):
    serializer_class = LoginSerializer


class UsuarioCreateAPIView(CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAny] 


class ProfessorListCreateApiView(ListCreateAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    permission_classes = [IsAuthenticated, IsGestor]

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.query_params.get('nome')
        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        return queryset


class ProfessorRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    permission_classes = [IsAuthenticated, IsGestor]

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Professor.DoesNotExist:
            return Response({"detail": "Professor not found."}, status=status.HTTP_404_NOT_FOUND)




class ReservadeAmbientesListCreateApiView(ListCreateAPIView):
    queryset = Reservar_de_Ambiente.objects.all()
    serializer_class = ReservaAmbientesSerializer
    permission_classes = [IsAuthenticated, IsGestor, IsProfessor]

class Disciplinas(ListCreateAPIView):
    serializer_class = DisciplinaSerializer
    permission_classes = [IsAuthenticated, IsProfessor]

    def get_queryset(self):
        return Disciplina.objects.filter(professor_disciplina__user=self.request.user)

class MinhasReservas(ListCreateAPIView):
    serializer_class = ReservaAmbientesSerializer
    permission_classes = [IsAuthenticated, IsProfessor]

    def get_queryset(self):
        return Reservar_de_Ambiente.objects.filter(professor__usuario=self.request.user)
