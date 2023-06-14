from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import ImagenesForm
from .models import Imagenes

class InicioView(FormView):
  form_class=ImagenesForm
  template_name='inicio.html'
  success_url=reverse_lazy('inicio')

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["titulo"] = 'Django y Azure Storage'
      context["imagenes"] = Imagenes.objects.all()
      return context
  
  def form_valid(self, form):
    form.save()
    return super().form_valid(form)