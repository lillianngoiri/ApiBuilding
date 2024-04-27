import requests
from random import choice
from django.shortcuts import render

def index(request):
    response = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
    data = response.json()
    fact = data['text']

    #r3 = requests.get('https://dog.ceo/api/breeds/image/random')
    #res3 = r3.json()
    #dog = res3['message']

    #response = requests.get('https://freetestapi.com/api/v1/students')
    #data = response.json()

    # Selecting one random student
    #random_student = choice(data)

    return render(request, 'index.html', {'fact': fact})

def facts(request): 
    response = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
    data = response.json()
    fact = data['text']
    return render(request, 'facts.html', {'fact': fact })

def dogs(request):
    r3 = requests.get('https://dog.ceo/api/breeds/image/random')
    res3 = r3.json()
    dog = res3['message']
    return render(request, 'dogs.html', {'dog': dog })

def students(request):
    response = requests.get('https://freetestapi.com/api/v1/students')
    data = response.json()

    # Selecting one random student
    random_student = choice(data)
    return render(request, 'portal.html', {'student': random_student })