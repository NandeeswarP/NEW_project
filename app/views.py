from django.shortcuts import render

# Create your views here.
def condition(request):
    D={'a':10,'b':20,'c':10}
    return render(request,'condition.html',D)

def loop(request):
    A={'L':['NANDEESWAR']}
    return render(request,'loop.html',A)
