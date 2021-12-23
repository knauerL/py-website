from django.shortcuts import render
from django.http import HttpResponse
from lists.models import player

# Create your views here.
def home_page(request):
    #return HttpResponse('<html><title>Escape Game</title><body><h1>Welcome traveler</h1><p id="txt1">What is your name?</p><input type="text" id="nameInput"><a href="name.html"><button type="submit"id="btn1">Enter</button></a><br><p id="txt2">There is a dog and a cat. Which one will you follow?</p><a href="dog.html"><button type="submit"id="btn2">Dog</button></a><a href="cat.html"><button type="submit"id="btn3">Cat</button></a></body></html>')
    #return render(request, 'home.html')
    if request.method == 'POST':
        thePlayer = player('', request.POST.get("plName"))
        return render(request, 'name.html', {'thePlayer' : thePlayer})
    else:
        return render(request, 'home.html')

#def name_page(request):
    #return HttpResponse('<html><title>Name Input</title><body><h1>Thank you (name here)</h1><p id="txt2">There is a dog and a cat. Which one will you follow?</p><a href="dog.html"><button type="submit"id="btn2">Dog</button></a><a href="cat.html"><button type="submit"id="btn3">Cat</button></a></body></html>')
    #return render(request, 'name.html')

def dog_page(request):
    #return HttpResponse('<html><title>Dog Choice</title><body><h1>You chose the dog to follow, what next?</h1><p>CODE TO BE WRITTEN HERE</p></body></html>')
    return render(request, 'dog.html')

def cat_page(request):
    #return HttpResponse('<html><title>Cat Choice</title><body><h1>You chose the cat to follow, what next?</h1><p>CODE TO BE WRITTEN HERE</p></body></html>')
    return render(request, 'cat.html')

def right_page(request):
    #return HttpResponse('{% load static %}<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>RIGHT PATH</title></head><body><div class="row"><div class="col-md-3"><p>DUMMY TEXT</p></div><div class="col-md-6"><h1>You chose the path on the right..</h1><h3>Now you face </h3></div><div class="col-md-3"><p>DUMMY TEXT</p></div></div></body></html>')
    return render(request, 'right.html')

def left_page(request):
    #return HttpResponse('{% load static %}<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>LEFT PATH</title></head><body><div class="row"><div class="col-md-3"><p>DUMMY TEXT</p></div><div class="col-md-6"><h1>You chose the path on the left..</h1><h3>Now you face </h3></div><div class="col-md-3"><p>DUMMY TEXT</p></div></div></body></html>')
    return render(request, 'left.html')