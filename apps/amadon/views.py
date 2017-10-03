from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return render(request, 'amadon/index.html')
def process(request):
    if request.POST['id'] == "1":
        request.session['amount'] = 19.99*int(request.POST['quantity'])
        try:
            request.session['count'] += int(request.POST['quantity'])
        except:
            request.session['count'] = 0
    elif request.POST['id'] == "2":
        request.session['amount'] = 29.99*int(request.POST['quantity'])
        try:
            request.session['count'] += int(request.POST['quantity'])
        except:
            request.session['count'] = 0
    elif request.POST['id'] == "3":
        request.session['amount'] = 4.99*int(request.POST['quantity'])
        try:
            request.session['count'] += int(request.POST['quantity'])
        except:
            request.session['count'] = 0
    elif request.POST['id'] == "4":
        request.session['amount'] = 49.99*int(request.POST['quantity'])
        try:
            request.session['count'] += int(request.POST['quantity'])
        except:
            request.session['count'] = 0
    try:
        request.session['total'] += request.session['amount']
    except:
        request.session['total'] = 0
    return redirect('/amadon/checkout')
def checkout(request):
    return render(request, 'amadon/checkout.html')
