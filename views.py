from django.shortcuts import render
from app.models import *

from django.http import HttpResponse
# Create your views here.


def default_topic(request):
    QLTO=Topic.objects.all()
    d={'topic':QLTO}
    return render(request,'default_topic.html',context=d)

def default_webpage(request):
    QLWO=Webpages.objects.all()
    d={'webpages':QLWO}
    return render(request,'default_webpage.html',context=d)

def default_Accessrecoard(request):
    QLAO=AccessRecoard.objects.all()
    d={'Access_recoard':QLAO}
    return render(request,'default_Access recoard.html',context=d)

def insert_topic(request):
    tn=input()
    NTO=Topic.objects.get_or_create(topic_name=tn)[0]
    NTO.save()
    return HttpResponse('topic is created')

def insert_webpage(request):
    tn=input('enter the topic name')
    n=input('enter the name')
    u=input('enter the URL')
    e=input('enter the Email ')
    TO=Topic.objects.get(topic_name=tn)
    NWO=Webpages.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
    NWO.save()
    return HttpResponse('webpages is created')

def insert_Accessrecord(request):
    n=input('enter the name')
    d=input('enter the date')
    a=input('enter the author')
    WO=Webpages.objects.get(name=n)
    NAO=AccessRecoard.objects.get_or_create(name=WO,date=d,author=a)[0]
    NAO.save()
    return HttpResponse('access record is created')
