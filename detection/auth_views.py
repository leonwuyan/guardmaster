from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import *
from django.views.decorators.http import require_POST
from guardmaster import common as Common
from detection.models import Excuse
import random

# Create your views here.


def index(request):
    excuse = random.choice(Excuse.objects.all())
    panels = None
    if request.user.is_authenticated():
        panels = Common.get_user_panels(request.user)

    data = {
        'title': excuse,
        'panels': panels,
    }

    return render(request, "detection/home.html", data)


@require_POST
def user_login(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
    except:
        return HttpResponseRedirect(reverse('index'))

    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponseRedirect(reverse('index'))


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
