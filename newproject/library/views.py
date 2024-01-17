from django.shortcuts import render
from . models import Bookinfo

from django.http import HttpResponse
from django.shortcuts import render
from . forms import Bookform
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required



# Create your views here.






@never_cache
@login_required(login_url='login')
def create(request):
    frm=Bookform()
    if request.POST:
        title=(request.POST.get('title'))
        year=(request.POST.get('year'))
        summary=(request.POST.get('summary'))
        bookobj=Bookinfo(title=title,year=year,summary=summary)
        bookobj.save()
    return render (request,'create.html',{'frm':frm})


@never_cache
@login_required(login_url='login')
def list(request):
    book=Bookinfo.objects.all()
    return render (request ,'list.html',{'books':book})
