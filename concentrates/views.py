from django.shortcuts import render, redirect, get_object_or_404

from .models import Concentrate


def concentrate_list(request):
    concentrates = Concentrate.objects.all().order_by('name')

    return render(request, "concentrates/concentrates_list.html", {
        'concentrates': concentrates,
    })


def concentrate_detail(request, pk):
    concentrate = get_object_or_404(Concentrate, pk=pk)

    return render(request, "concentrates/concentrates_detail.html", {
        'concentrate': concentrate
    })




