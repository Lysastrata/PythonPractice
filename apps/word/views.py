from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
def index(request):
    return render(request,'word/index.html')
def post(request):
    request.session['word'] = {
        'rand': get_random_string(length=14)
        }
    try:
        request.session['count'] += 1
    except:
        request.session['count'] = 0
    return redirect('/randomword')
def reset(request):
    request.session['word'] = {}
    request.session['count'] = 0
    return redirect('/randomword')
