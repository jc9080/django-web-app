from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
import random


# Create your views here.
def index(request):
    now = datetime.now()
    context = {
        'current_date' : now
    }
    return render(request, 'yelplist/index.html', context)


def select(request):
    context = {}
    return render(request, 'yelplist/select.html', context)


def result(request):
    input = int(request.GET['number'])
    result = []
    if input >=1 and input <= 45:
        result.append(input)
    box = []
    for i in range(0, 45):
        if input != i+1:
            box.append(i+1)

    random.shuffle(box)
    while len(result) < 6:
        result.append(box.pop())

    context = {
        'numbers':result
    }
    return render(request, 'yelplist/result.html', context)
