from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Film
# Create your views here.
from .serializer import FilmSerializer

class FilmAPIList(generics. ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class FilmAPIUpdate(generics.UpdateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class FilmAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

# class FilmAPIView(APIView):
#     def get(self, request):
#         w = Film.objects.all()
#         return Response({'posts': FilmSerializer(w, many=True).data}) # many обрабатывать не 1 а список записей
#
#     def post(self, request):
#         #проверям если заголовка нет = исключение
#         serializer = FilmSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Метод PUT не определен"})
#
#         try:
#             instance = Film.objects.get(pk=pk)
#         except:
#             return Response({"error": "Объект не найден"})
#
#         serializer = FilmSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({"post": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Метод DELETE не определен"})
#
#         # здесь код для удаления записи с переданным pk
#
#         return Response({"post": "delete post " + str(pk)})

# class FilmAPIView(generics.ListAPIView):
#     queryset = Film.objects.all()
#     serializer_class = FilmSerializer