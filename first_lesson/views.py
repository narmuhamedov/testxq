from django.shortcuts import render
from django.views.generic import TemplateView

#CBV8

class FirstLessonView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Привет я такой то и мы изучаем Джанго ура Товарищи"
        context['emodji'] = "🤯"
        context['run_string'] = "🐍➡️🐍➡️🐍➡️🐍➡️🐍➡️🐍➡️🐍➡️🐍➡️🐍🐍➡️🐍➡️🐍➡️🐍➡️🐍➡️🐍➡️🐍➡️🐍➡️🐍"
        return context

# DEF 

# def first_lesson(request):
#   if request.method == 'GET':
#     context = {
#       "text": "Привет я такой то и мы изучаем Джанго ура Товарищи",
#       "emodji": "🤯",
#       "run_string": "🐍➡️🐍➡️🐍➡️🐍➡️🐍➡️🐍➡️🐍➡️🐍➡️🐍🐍➡️🐍➡️🐍➡️🐍➡️🐍➡️🐍➡️🐍➡️🐍➡️🐍"
#     }