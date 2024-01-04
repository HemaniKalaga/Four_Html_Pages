from django.shortcuts import render

# Create your views here.
def templates1(request):
    return render(request,'templates1.html')

def templates2(request):
    return render(request,'templates2.html')

def templates3(request):
    return render(request,'templates3.html')

def templates4(request):
    return render(request,'templates4.html')

