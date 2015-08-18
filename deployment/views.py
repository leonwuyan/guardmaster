from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from deployment.tasks import _do_kground_work

# Create your views here.


class Hello(View):
    def get(self, request, *args, **kwargs):
        _do_kground_work.delay('GreenPine')
        return HttpResponse('Hello, World!')
