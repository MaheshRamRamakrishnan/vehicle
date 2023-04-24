from django.shortcuts import render, redirect
from .models import *


def v_home(request):
    return render(request, 'index.html')
