from django.shortcuts import render
from .forms import BasicaForm

# Create your views here.

def basica(request):
  form = BasicaForm(request.POST)
  if request.method == 'POST':
    form = BasicaForm(request.POST)
    if form.is_valid():
      form.save()
    else:
      form = BasicaForm()
  return render(request, 'forms/historial.html', {'form': form})