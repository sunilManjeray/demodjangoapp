from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.shortcuts import render
from .models import UserInfo
from django.template import loader

from django.http import Http404


def index(request):
    name_list = UserInfo.objects.order_by('-name_text')[:5]

    # response = ', '.join([q.name_text for q in name_list])
    context = {
        'user_list': name_list
    }
    return render(request, 'myapp/index.html', context)


def details(request, user_id):

    name = get_object_or_404(UserInfo, pk=user_id)
    return render(request, 'myapp/details.html', {'name': name})


def results(request, user_id):
    return HttpResponse("you'r looking at user who's id %s." % user_id)


def names(request, user_id):
    return HttpResponse("You're working on user  %s." % user_id)
