from django import forms
from .models import Imagenes

class ImagenesForm(forms.ModelForm):
  def __init__(self,*args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['nombre'].widget.attrs['autofocus'] = True
    for form in self.visible_fields():
      form.field.widget.attrs['class']='form-control'
  
  class Meta:
    model=Imagenes
    fields='__all__'