from rest_framework import generics 
from .models import Categoria, Autor, Livro 
from .serializers import LivroSerializer, AutorSerializer, CategoriaSerializer
from .filters import LivroFilter

class LivroList(generics.ListCreateAPIView): 
    queryset = Livro.objects.all() 
    serializer_class = LivroSerializer 
    filterset_class = LivroFilter
    search_fields = ("^name",)
    ordering_fields = ['titulo', 'autor', 'categoria', 'publicado_em']
    
class LivroDetail(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Livro.objects.all() 
    serializer_class = LivroSerializer 
    name = "livro-detail"
    
class AutorList(generics.ListCreateAPIView): 
    queryset = Autor.objects.all() 
    serializer_class = AutorSerializer 
    name = "autor-list" 
    search_fields = ("^name",)
    ordering_fields = ['nome']

class CategoriaList(generics.ListCreateAPIView): 
    queryset = Categoria.objects.all() 
    serializer_class = CategoriaSerializer 
    name = "categoria-list"
    search_fields = ("^name",)
    ordering_fields = ['nome']
