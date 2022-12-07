from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404

from .forms import AddStrainForm
from .models import Strain



def strain_list(request):
    strains = Strain.objects.all()

    return render(request, "strains/strain_list.html", {
        'strains': strains
    })


def strain_detail(request, pk):
    strain = get_object_or_404(Strain, pk=pk)

    return render(request, 'strains/strain_detail.html', {
        'strain': strain
    })


@login_required
def add_strain(request):
    if request.method == 'POST':
        form = AddStrainForm(request.POST)

        if form.is_valid():
            strain = form.save(commit=False)
            strain.save()

            messages.success(request, 'Strain created successfully.')

            return redirect('strain_list')
    else:
        form = AddStrainForm()

    return render(request, 'strains/add_strain.html', {
        'form': form
    })


@login_required
def strain_delete(request, pk):
    strain = get_object_or_404(Strain, pk=pk)
    strain.delete()

    messages.success(request, 'Strain deleted successfully.')

    return redirect('strain_list')


@login_required
def strain_edit(request, pk):
    strain = get_object_or_404(Strain, pk=pk)

    if request.method == 'POST':
        form = AddStrainForm(request.POST, instance=strain)

        if form.is_valid():
            form.save()

            messages.success(request, 'Changes saved successfully.')

            return redirect(strain_list)

    else:
        form = AddStrainForm(instance=strain)

    return render(request, 'strain/strain_edit.html', {
        'form': form
    })