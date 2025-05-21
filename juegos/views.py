
from juegos.models import Juego
from django import forms
from django.views.generic import TemplateView, ListView , CreateView, DetailView, DeleteView


# Create your views here.
class IndexViews(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rotulo'] = 'Juegos de Mesa'
        return context
  
class JuegoListView(ListView):
    model = Juego
    template_name = 'juegos_list.html'
    context_object_name = 'juegos'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rotulo'] = 'Lista de Juegos'
        return context
    
class JuegoCreateView(CreateView):
    model = Juego
    template_name = 'nuevo_juego.html'
    fields = '__all__'
    success_url = '/list/' 

    def get_form(self):
        form = super().get_form()
        form.fields['imagen'].widget.attrs['accept'] = 'image/*'
        form.fields['fecha_lanzamiento'].widget = forms.DateInput(attrs={'type': 'date'})
        return form
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rotulo'] = 'Nuevo Juego'
        return context
    
class JuegoDetailView(DetailView):
    model = Juego
    template_name = 'detalles_juego.html'
    context_object_name = 'juego'  # Nombre del contexto para el juego
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resenas'] = self.object.resenas.all()
        return context
 
class JuegoDeleteView(DeleteView):
    model = Juego
    template_name = 'eliminar_juego.html'
    success_url = '/list/' 
    context_object_name = 'juego'  # Nombre del contexto para el juego
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rotulo'] = 'Eliminar Juego'
        return context