from django.shortcuts import render
import markdown
import random

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
    
def md_a_html(nombre): 
    texto = util.get_entry(nombre)
    mark = markdown.Markdown()
    if texto == None:
        return None
    else:
        return mark.convert(texto)

def entry(request, nombre):
    contenido = md_a_html(nombre)
    if contenido == None:
        return render(request, "encyclopedia/error.html",{
            "message": "Eso no existe"
        })
    else:
        return render(request, "encyclopedia/entry.html",{
            "nombre": nombre,
            "contenido": contenido
        })
        
def buscar(request):
    if request.method == "POST":
        x = request.POST['q']
        contenido = md_a_html(x)
        if contenido != None:
            return render(request, "encyclopedia/entry.html",{
            "nombre": x,
            "contenido": contenido
        })
        else:
            all_entries = util.list_entries()
            sugerencias = []
            for one_entry in all_entries:
                if x.lower() in one_entry.lower():
                    sugerencias.append(one_entry)
            return render(request, "encyclopedia/search.html",{
                "sugerencias":sugerencias
            })
            
def new(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new.html")
    else:
        nombre = request.POST['nombre']
        contenido = request.POST['contenido']
    if util.get_entry(nombre) is not None:
        return render(request, "encyclopedia/error.html",{
            "message":"Ya existe"
        })
    else:
        util.save_entry(nombre,contenido)
        x = md_a_html(nombre)
        return render(request, "encyclopedia/entry.html",{
            "nombre": nombre,
            "contenido": x
        })
    
def edit(request):
    if request.method == "POST":
        nombre = request.POST['nombre']
        contenido=util.get_entry(nombre)
        return render(request, "encyclopedia/edit.html",{
            "nombre":nombre,
            "contenido":contenido
        })
def save(request):
    if request.method == "POST":
        nombre = request.POST['nombre']
        contenido=request.POST['contenido']
        util.save_entry(nombre,contenido)
        x = md_a_html(nombre)
        return render(request, "encyclopedia/entry.html",{
            "nombre": nombre,
            "contenido": x
        })
        
def random_page(request):
    all_entries = util.list_entries()
    random_entry = random.choice(all_entries)
    x = md_a_html(random_entry)
    return render(request, "encyclopedia/entry.html",{
        "nombre": random_entry,
        "contenido": x
    })