from django.contrib.auth import logout

from django.shortcuts import render, redirect
from .models import Fighter
from .forms import FighterForm
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required


@login_required
def fighter_list(request):
    search = request.GET.get('search', '')

    page_number = request.GET.get('page')


    fighter = Fighter.objects.filter()
    if search:
        fighter = fighter.filter(
            Q(name__icontains=search) | Q(nickname__icontains=search) | Q(weight_class__icontains=search))
    paginator = Paginator(fighter, 3)

    fighter = paginator.get_page(page_number)

    return render(request, 'fighter/fighter_list.html', {'fighters': fighter, 'search': search})


@permission_required('fighter.add_fighter', raise_exception=True)
def fighter_create(request):
    if request.method == "POST":
        form = FighterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('fighter_list')
    else:
        form = FighterForm()

    return render(request, 'fighter/create_fighters.html', {'form': form})


@permission_required('fighter.change_fighter', raise_exception=True)
def fighter_update_form(request, pk=None):
    fighter = Fighter.objects.filter(id=pk).first()
    form = FighterForm(instance=fighter)
    return render(request, 'fighter/update_fighters.html', {'form': form, 'fighter': fighter, })

@login_required
def fighter_update(request, pk=None):
    fighter = Fighter.objects.filter(id=pk).first()
    if not fighter:
        return redirect('fighter_list')
    if request.method == "POST":
        form = FighterForm(instance=fighter, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
        return redirect('fighter_list')
    else:
        form = FighterForm(instance=fighter)

    return render(request, 'fighter/update_fighters.html', {'form': form, 'fighter': fighter})


@permission_required('fighter.change_fighter', raise_exception=True)
def fighter_delete(request, pk=None):
    Fighter.objects.filter(id=pk).update(is_active=False)

    return redirect('fighter_list')


def fighter_detail(request, pk):
    fighter = Fighter.objects.filter(id=pk).first()

    if not fighter:
        return redirect('fighter_list')

    return render(request, 'fighter/detail.html', {'fighter': fighter})


def logout_view(request):
    logout(request)
    return redirect('login')
