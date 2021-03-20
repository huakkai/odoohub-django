from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'site': 'adminLTE',
        'desc0': 'Django AdminLTE2 provides extensible templates for making use of the general purpose AdminLTE2 theme.',
        'desc1': 'The base AdminLTE template provides much of what you need, but you’ll need to customise it in some ways to meet your needs. In particular, no navigation is provided (we’ll cover this shortly).',
        'docs': 'https://django-adminlte2.readthedocs.io/en/latest/index.html',
    }
    return render(request, 'adminlte/index.html', context=context)
