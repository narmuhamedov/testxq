from django.shortcuts import render, get_object_or_404
from . import models


def film_list(request):
  if request.method == 'GET':
    query = models.Film.objects.all().order_by('-id')
    context = {'film': query}
    return render(request, template_name='films/films.html' , context=context)
  

def film_detail(request, id):
  if request.method == "GET":
    film_id = get_object_or_404(models.Film, id=id)
    context = {'film_id': film_id}
    return render(request, template_name='films/film_detail.html', context=context)