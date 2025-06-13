from django.shortcuts import render, redirect, get_object_or_404
from .models import comuna
from .forms import ComunaForm

def comuna_list(request):
    comunas = comuna.objects.all()
    return render(request, 'MisComunas/list.html', {'comunas': comunas})

def comuna_create(request):
    if request.method == 'POST':
        form = ComunaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comuna_list')
    else:
        form = ComunaForm()
    return render(request, 'MisComunas/form.html', {'form': form})

def comuna_update(request, pk):
    comuna_instancia = get_object_or_404(comuna, pk=pk) 

    if request.method == 'POST':
        form = ComunaForm(request.POST, instance=comuna_instancia)
        if form.is_valid():
            form.save()
            return redirect('comuna_list')
    else:
        form = ComunaForm(instance=comuna_instancia)

    return render(request, 'MisComunas/form.html', {'form': form})

def comuna_delete(request, pk):
    comuna_instancia = get_object_or_404(comuna, pk=pk)
    if request.method == 'POST':
        comuna_instancia.delete()
        return redirect('comuna_list')
    return render(request, 'MisComunas/confirm_delete.html', {'comuna': comuna_instancia})
