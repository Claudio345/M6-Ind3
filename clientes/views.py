from django.shortcuts import render
from .models import Cliente

# Create your views here.
def index(request):
    clientes = Cliente.objects.all()
    return render(
        request, 
        'index.html', {'clientes':clientes}
    )
