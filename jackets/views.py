from django.shortcuts import render, get_object_or_404
from .models import Jacket, Jacket_Detail
# Create your views here.
def jeckets(request, *args, **kwargs):
    jackets = Jacket.objects.all()
    context = {'jeck': jackets}
    return render(request, 'jeckets/index.html', context=context)



def jacket_detail(request, jacket_id, *args, **kwargs):
    jacket = get_object_or_404(Jacket, id = jacket_id)
    context ={'jecks': jacket}
    return render(request, "jeckets/detail.html", context=context)