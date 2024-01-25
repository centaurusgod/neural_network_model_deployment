from django.shortcuts import render
from .ml_model import predictClassLabel
import os

from django.conf import settings

from django.shortcuts import render
from .ml_model import predictClassLabel

def index(request):
    return render(request, 'index.html')



