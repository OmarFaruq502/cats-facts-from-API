from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import Fact

# Create your views here.

def random(request):

    json_req = requests.get('https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=2')
    
    fact = json_req.json()

    text = fact[0]["text"]

    model_fact = Fact(fact = text)
    model_fact.save()

    return render(request, 'facts/facts.html', {'text':text})

def viewall(request):
    
    # Django Documentation Referenence
    # https://docs.djangoproject.com/en/3.0/ref/models/querysets/#order-by

    facts = Fact.objects.order_by('-id')[:5]

    # # The lastest 5 entries
    # facts = facts[-5:]

    return render(request, 'facts/viewall.html', {'facts':facts})

