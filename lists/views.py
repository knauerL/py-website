from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    return HttpResponse('<html><title>Escape Game</title><body><h1>Welcome traveler</h1><p id="txt1">What is your name?</p><input type="text" id="nameInput"><a href="name.html"><button type="submit"id="btn1">Enter</button></a><br><p id="txt2">There is a dog and a cat. Which one will you follow?</p><a href="dog.html"><button type="submit"id="btn2">Dog</button></a><a href="cat.html"><button type="submit"id="btn3">Cat</button></a></body></html>')
    #return render(request, 'home.html')

def name_page(request):
    return HttpResponse('<html><title>Name Input</title><body><h1>Thank you (name here)</h1><p id="txt2">There is a dog and a cat. Which one will you follow?</p><a href="dog.html"><button type="submit"id="btn2">Dog</button></a><a href="cat.html"><button type="submit"id="btn3">Cat</button></a></body></html>')

def dog_page(request):
    return HttpResponse('<html><title>Dog Choice</title><body><h1>You chose the dog to follow, what next?</h1><p>CODE TO BE WRITTEN HERE</p></body></html>')

def cat_page(request):
    return HttpResponse('<html><title>Cat Choice</title><body><h1>You chose the dog to follow, what next?</h1><p>CODE TO BE WRITTEN HERE</p></body></html>')