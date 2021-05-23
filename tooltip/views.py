from django.shortcuts import render
from django.http import HttpResponse
import googletrans
from googletrans import Translator
# 'en': 'english', 'vi': 'vietnamese'

# Create your views here.


def index(request):
    # return HttpResponse("fu")
    return render(request, 'tooltip/index.html')


def tooltip(request):
    f = request.POST["input"]
    n = f.split()
    m = trans(n)
    l = len(m)
    i = 0
    full = []
    context = zip(n, m) 
    while i < l:
        x = str(m[i])
        y = str(i)
        z = str(n[i])
        u = "<a class='change' data-toggle='tooltip' data-placement='bottom' data-original-title='"+x+"' id='"+y+"' >"+z+"</a>"
        full.append(u)
        i = i+1
        

    # context = {'value':n,'tooltip':m,'l':l}
    # return render(request, "tooltip/tooltip.html", context )
    return render(request, "tooltip/tooltip.html", {'full' :full} )
    # return HttpResponse(context)


def trans(x):
    b=[]
    for i in x:
        t = Translator()
        a = t.translate(i, src="en", dest="vi")
        b.append(a.text)
    return b
