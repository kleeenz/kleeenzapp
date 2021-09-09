from django.shortcuts import render
from .models import table


def display_table(request):
    all_obj = table.objects.all()
    context = {'all' : all_obj}
    return render(request, 'demo_app/home.html', context)

