from django.shortcuts import render
from django.http import HttpResponse

from .models import Candidate
# Create your views here.


def index(request):
    candidates= Candidate.objects.all()
    # str=''
    # for candidate in candidates: 
    #     str+= "<p>{} 기호 {}번({})<br>".format(
    #         candidate.name,
    #     candidate.party_number,
    #     candidate.Area)
    #     str+=candidate.intoduction+"</p>"
    return render(request,'elections/index.html')
    # return HttpResponse(str)
