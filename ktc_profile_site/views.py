#  -*- coding: utf-8 -*-
# coding: utf-8
from django.shortcuts import render
import sys


def index(request):
    return render(request, 'main/index.html')


def test(request):
    return render(request, 'test.html')


def test2(request):
    return render(request, 'test2.html')
