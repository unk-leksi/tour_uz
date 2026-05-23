from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Excursion
from .forms import ExcursionForm

def excursion_list(request):
    excursions = Excursion.objects.all()
    return render(request, 'excursions/excursion_list.html', {'excursions': excursions})

def excursion_detail(request, excursion_id):
    excursion = get_object_or_404(Excursion, pk=excursion_id)
    return render(request, 'excursions/excursion_detail.html', {'excursion': excursion})

@login_required
def excursion_create(request):
    if request.method == 'POST':
        form = ExcursionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('excursions:excursion_list')
    else:
        form = ExcursionForm()
    return render(request, 'excursions/excursion_form.html', {'form': form})

@login_required
def excursion_edit(request, excursion_id):
    excursion = get_object_or_404(Excursion, pk=excursion_id)
    if request.method == 'POST':
        form = ExcursionForm(request.POST, request.FILES, instance=excursion)
        if form.is_valid():
            form.save()
            return redirect('excursions:excursion_detail', excursion_id=excursion.id)
    else:
        form = ExcursionForm(instance=excursion)
    return render(request, 'excursions/excursion_form.html', {'form': form})
