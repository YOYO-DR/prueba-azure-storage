from typing import Any
from django.http import HttpRequest, HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import FormView,UpdateView
from django.urls import reverse_lazy
from .forms import ImagenesForm
from .models import Imagenes

class InicioView(FormView):
  form_class=ImagenesForm
  template_name='inicio.html'
  success_url=reverse_lazy('inicio')

  def post(self, request, *args, **kwargs):
    action=request.POST.get('action')
    if action:
      if 'delete' in action:
        id=int(action.replace('delete','').strip())
        img=Imagenes.objects.get(id=id)
        img.delete()
        return HttpResponseRedirect(self.success_url)
    return super().post(request,*args, **kwargs)

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["titulo"] = 'Django y Azure Storage'
      context["imagenes"] = Imagenes.objects.all()
      return context
  
  def form_valid(self, form):
    form.save()
    return super().form_valid(form)