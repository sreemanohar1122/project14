from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

class Home(View):
    def get(self,request):
        return render(request,'home.html')
class Input(View):
    def get(self,request):
        x=int(request.GET["t1"])
        y=int(request.GET["t2"])
        z=int(x)+int(y)
        resp=HttpResponse("data submitted successfully")
        resp.set_cookie('c1',str(z),max_age=100)
        return resp
class Display(View):
    def get(self,request):
        if 'c1' in request.COOKIES:
            p=request.COOKIES['c1']
            return HttpResponse("the sum is"+p)
        else:
            return render(request,'home.html')

# Create your views here.
