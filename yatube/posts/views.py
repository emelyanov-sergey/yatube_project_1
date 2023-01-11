from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse('главная старница')


def group_posts(request, any_slug):
    return HttpResponse('Группы')
