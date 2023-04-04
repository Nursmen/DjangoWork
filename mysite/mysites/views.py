from django.http import JsonResponse
import json
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Person
from django.shortcuts import redirect
from .forms import NameForm
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def main(request):
    user = authenticate(username='Nurs', password='Nurs')
    person = Person.objects.get(myself=user)
    
    if request.method == 'GET':
        form = NameForm()

        return render(request, 'mysites/main.html', {'person':person, 'form':form})
    
    if request.method == 'POST':
        
        form = NameForm(request.POST)
        if form.is_valid():

            person.phone=form.cleaned_data['phone']
            person.password=form.cleaned_data['password']

            person.save()

            return redirect('/')
    
    return HttpResponse('errorrrr')

def login(request):
    return render(request, 'mysites/login.html')

@csrf_exempt
def ajax_post_view(request):
        user = authenticate(username='Nurs', password='Nurs')
        person = Person.objects.get(myself=user)

        data_from_post = json.load(request)

        person.phone=data_from_post['phone']
        person.password=data_from_post['password']

        person.save()   

        return redirect('/')
