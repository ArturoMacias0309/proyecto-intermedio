from django.shortcuts import render
from AppDonas.forms import *
from AppDonas.models import *

def inicio(request):
    return render(request, "inicio.html",{"mensaje_inicio":"Bienvenidos a Donatopia!"})


def donareg(request):
    if request.method == "POST":
        form = FormDonareg(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            donareg_ingresada= Donareg(sabor = info["sabor"], precio = info["precio"])
            donareg_ingresada.save()
            return render(request, "inicio.html", {"mensaje_inicio":"Dona regular ingresada con éxito!"})
        else:
            formulario = FormDonareg()
            return render(request, "donareg.html", {"form" : formulario})
    
    return render(request, "donareg.html")


def donaprem(request):
    if request.method == "POST":
        form = FormDonaprem(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            donaprem_ingresada= Donaprem(sabor = info["sabor"], precio = info["precio"])
            donaprem_ingresada.save()
            return render(request, "inicio.html", {"mensaje_inicio":"Dona premium ingresada con éxito!"})
        else:
            formulario = FormDonaprem()
            return render(request, "donaprem.html", {"form" : formulario})
    
    return render(request, "donaprem.html")


def malteadas(request):
    if request.method == "POST":
        form = FormMalteadas(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            malteada_ingresada= Malteadas(sabor = info["sabor"], precio = info["precio"])
            malteada_ingresada.save()
            return render(request, "inicio.html", {"mensaje_inicio":"Malteada ingresada con éxito!"})
        else:
            formulario = FormMalteadas()
            return render(request, "malteadas.html", {"form" : formulario})
    
    return render(request, "malteadas.html")


def busqueda_donaprem(request):
    
    return render (request, "busqueda_donaprem.html")



def resultado_busqueda_donaprem(request):
    valor_url = request.GET["sabor"]
    if valor_url != "":
        donaprem_filtrado = Donaprem.objects.filter(sabor = valor_url)  
        print(donaprem_filtrado)
        print('----------------------------------------------------------------------------------------')
        return render(request, "resultado_busqueda_donaprem.html", {'donaprem_seleccionados': donaprem_filtrado })
    else:
        return render(request, "busqueda_donaprem.html")