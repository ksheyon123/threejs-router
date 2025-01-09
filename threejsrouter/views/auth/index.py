from django.http import HttpResponse
from django.shortcuts import render 

def sign_in(request):
    context = {
        'with_header' : 'false'
    } 
    return render(request, 'auth/sign_in.html', context)


def sign_up(request):
    return HttpResponse("Hello, world. You're at the polls index.")