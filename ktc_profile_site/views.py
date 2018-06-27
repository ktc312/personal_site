#  -*- coding: utf-8 -*-
# coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse
import os
import logging
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.decorators.csrf import csrf_exempt
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class LoginRequiredMixin(View):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


def index(request):
    return render(request, 'main/index.html')


def stock_project(request):
    logging.info(request)
    with open(os.path.join(BASE_DIR, 'static/main/data/Stock_forecasting_example.pdf'), 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=ktc_project.pdf'
        return response


def resume(request):
    logging.info(request)
    with open(os.path.join(BASE_DIR, 'static/main/Resume_KTC.pdf'), 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=resume_ktc.pdf'
        return response


@csrf_exempt
@login_required(login_url='/login/')
def data(request):
    return render(request, 'main/data.html', {'title': 'Personal Network-Attached Storage'})

