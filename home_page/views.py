from django.shortcuts import render
from django.http import FileResponse, Http404

# Create your views here.
def home_page(request):
    return render(request,'home_page.html',)

def self_discovery(request):
    return render(request,'self_discovery.html',)
def global_warming(request):
    return render(request,'global_warming.html',)
def water(request):
    return render(request,'water.html',)


def human_body(request):
    try:
        return FileResponse(open('ProdutoFinal.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()
