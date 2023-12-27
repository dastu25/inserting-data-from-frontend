from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *

def htmlpage(request):
    
    if request.method=='POST':
        tn=request.POST['tn']
        TN=Topic.objects.get_or_create(topic_name=tn)[0]
        TN.save()
        
        return HttpResponse('htmlpage')
    
    
    
    
    return render(request,'htmlpage.html')


