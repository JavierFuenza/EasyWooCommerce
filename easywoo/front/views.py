from django.shortcuts import render
from django.http import HttpResponse
from api.views import wcapi, getProd
# Create your views here.



def index(request):
    return HttpResponse(getProd(65))