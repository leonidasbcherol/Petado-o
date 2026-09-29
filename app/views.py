from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Pet
from .forms import PetForm

def home(request):
    return render(request, 'app/home.html')

def lista_pets(request):
    pets = Pet.objects.all()
    return render(request, 'app/lista_pets.html', {'pets': pets})

def detalhe_pet(request, id):
    pet = get_object_or_404(Pet, id=id)
    return render(request, 'app/detalhe_pet.html', {'pet': pet})

@login_required
def criar_pet(request):
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pets')
    else:
        form = PetForm()
    return render(request, 'app/form_pet.html', {'form': form})

@login_required
def editar_pet(request, id):
    pet = get_object_or_404(Pet, id=id)
    if request.method == 'POST':
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('lista_pets')
    else:
        form = PetForm(instance=pet)
    return render(request, 'app/form_pet.html', {'form': form, 'pet': pet})

@login_required
def excluir_pet(request, id):
    pet = get_object_or_404(Pet, id=id)
    if request.method == 'POST':
        pet.delete()
        return redirect('lista_pets')
    return render(request, 'app/confirmar_exclusao.html', {'pet': pet})
