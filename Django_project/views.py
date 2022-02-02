from django.shortcuts import render
from project_sliders.models import Slider


def sliders(request, *args, **kwargs):
    slide = Slider.objects.all()
    context = {
        'slider': slide,
    }
    return render(request, 'slider.html', context)


def home_page(request):
    slide = Slider.objects.first()
    context = {
        'dd': slide
    }
    return render(request, 'Index.html', context)
