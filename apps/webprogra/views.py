from django.shortcuts import render, redirect

from .models import *
# Create your views here.



def index(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        naci = request.POST.get('naci')
        salario = request.POST.get('salario')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')

        print("su nombre es " + nombre + ' '+ apellido +' ' + " y nacio " + naci
              +" con un sueldo de "+ salario + "  su direccion "+ direccion + "su numero de telefono es "+telefono)

        model_employee = employee(name=nombre,
                                lastname=apellido,
                                date_bo=naci,
                                Salary=salario,
                                telefono=telefono,
                                direcciono=direccion)
        model_employee.save()
        return redirect('webprogra:index')

    elif request.method == "GET":
        return render(request, 'index.html')

def tablas(request):
    allemployee = employee.objects.all()
    return render(request, 'tablas.html', {'allemployee': allemployee})
