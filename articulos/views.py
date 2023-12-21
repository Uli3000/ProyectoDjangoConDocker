# views.py
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView, FormView
from .models import Articulo
from django.urls import reverse_lazy, reverse
from .forms import FormularioComentario, FiltroArticulosForm
from django.views import View
from django.views.generic.detail import SingleObjectMixin
import uuid

# Create your views here.

class VistaListaArticulos(ListView):
    model = Articulo
    template_name = 'lista_articulos.html'
    context_object_name = 'articulo_list'

    def get_queryset(self):
        genero = self.kwargs.get('genero', None)
        if genero:
            return Articulo.objects.filter(genero=genero)
        else:
            return Articulo.objects.all()

class VistaListaArticulosPorCategoria(ListView):
    model = Articulo
    template_name = 'lista_articulos_por_categoria.html'
    context_object_name = 'articulo_list'

    def get_queryset(self):
        plataforma = self.kwargs.get('plataforma', None)
        if plataforma:
            return Articulo.objects.filter(plataforma=plataforma)
        else:
            return Articulo.objects.all()

class VistaListaCategorias(ListView):
    model = Articulo
    template_name = 'lista_categorias.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Obtén la información del formulario
        form = FiltroArticulosForm(self.request.GET)
        
        # Aplica los filtros solo si el formulario es válido
        if form.is_valid():
            plataforma = form.cleaned_data.get('plataforma')
            genero = form.cleaned_data.get('genero')
            modalidad = form.cleaned_data.get('modalidad')

            # Filtra los artículos según los parámetros del formulario
            queryset = Articulo.objects.all()
            if plataforma:
                queryset = queryset.filter(plataforma=plataforma)
            if genero:
                queryset = queryset.filter(genero=genero)
            if modalidad:
                queryset = queryset.filter(modalidad=modalidad)

            context['articulo_list'] = queryset

        context['categorias'] = Articulo.objects.values_list('plataforma', flat=True).distinct()
        context['form'] = form

        return context

class VistaDetalleArticulo(DetailView):
    model = Articulo
    template_name = 'detalle_articulo.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FormularioComentario
        return context

    def post(self, request, *args, **kwargs):
        form = FormularioComentario(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.Articulo = self.get_object()
            comentario.autor = self.request.user
            comentario.save()
        return super().get(request, *args, **kwargs)

class VistaModificacionArticulo(UpdateView):
    model = Articulo
    fields = (
        'titulo',
        'descripcion',
        'genero',
        'plataforma',
        'modalidad',
        'costo',
    )
    template_name = 'editar_articulo.html'
    success_url = reverse_lazy('lista_articulos')

class VistaEliminacionArticulo(DeleteView):
    model = Articulo
    template_name = 'eliminar_articulo.html'
    success_url = reverse_lazy('lista_articulos')
    object_name = 'articulo'

class VistaCrearArticulo(CreateView):
    model = Articulo
    template_name = 'nuevo_articulo.html'
    fields = (
        'titulo',
        'descripcion',
        'genero',
        'plataforma',
        'modalidad',
        'costo',
        'imagen'
    )
    success_url = reverse_lazy('lista_articulos')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class ComentarioGet(DetailView):
    model = Articulo
    template_name = 'detalle_articulo.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FormularioComentario
        return context

class ComentarioPost(SingleObjectMixin, FormView, View):
    model = Articulo
    form_class = FormularioComentario
    template_name = 'detalle_articulo.html'

    def post(self, request, *args, **kwargs):
        self.Articulo = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comentario = form.save(commit=False)
        comentario.Articulo = self.Articulo
        comentario.save()
        return super().form_valid(form)
