from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
def index(request):
    return render (request, 'Session_words/index.html')
def color(request):
    if 'font' in request.POST:
        size = "24pt"
    else:
        size = "12pt"

    data = {
    'word': request.POST['word'],
    'color': request.POST['color'],
    'font': size,
    'time': strftime("%b %d, %Y %I:%M %p", gmtime()),
    }
    if 'data' not in request.session:
        request.session['data'] = []
    request.session['data'].append(data)
    request.session.modified = True
    return redirect('/words')
def reset(request):
    request.session['data'] = []
    return redirect('/words')
