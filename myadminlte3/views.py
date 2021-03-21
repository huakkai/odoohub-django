from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'site': 'adminLTE3',
    }
    return render(request, 'adminlte/index.html', context=context)
