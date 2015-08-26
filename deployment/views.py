from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from deployment.tasks import _do_sh

# Create your views here.


class Hello(View):
    def get(self, request, *args, **kwargs):
        _do_sh(
            ['/Users/Raynor/Downloads', 'ls', '-la'],
            ['/Users/Raynor/Downloads', 'ls', '-la']
        )
        return HttpResponse('Hello, World!')
