from django.shortcuts import render

# Create your views here.
def ever(request):
    return render(request, 'Andex.html')

def com(request):
    return render(request,'compras.html')
