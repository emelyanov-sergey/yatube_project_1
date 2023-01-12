from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    template = 'posts/index.html'
    title = 'главная страница'
    context = {
        'title': title
    }
    return render(request, template, context)


def group_posts(request, any_slug):
    template = 'posts/group_list.html'
    title = 'информация о группах'
    context = {
        'title': title
    }
    return render(request, template, context)



