from django.urls import path
from .views import (
    VistaListaArticulos,
    VistaDetalleArticulo,
    VistaModificacionArticulo,
    VistaEliminacionArticulo,
    VistaCrearArticulo,VistaListaCategorias,VistaListaArticulosPorCategoria
                    )

urlpatterns = [
    path('',VistaListaArticulos.as_view(),name='lista_articulos'),
    path('articulos/<str:genero>/', VistaListaArticulos.as_view(), name='lista_articulos_por_genero'),
    path('<uuid:pk>/',VistaDetalleArticulo.as_view(),name='detalle_articulo') ,
    path('editar/<uuid:pk>/',VistaModificacionArticulo.as_view(),name='editar_articulo'),
    path('eliminar/<uuid:pk>/',VistaEliminacionArticulo.as_view(),name='eliminar_articulo'),
    path('nuevo/',VistaCrearArticulo.as_view(),name='nuevo_articulo'),
    path('categorias/', VistaListaCategorias.as_view(), name='lista_categorias'),
    path('articulos/categoria/<str:plataforma>/', VistaListaArticulosPorCategoria.as_view(), name='lista_articulos_por_categoria'),
   
    ]
#agregar nuevo articulo en la pagina, para no poner la url