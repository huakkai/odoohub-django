from django.shortcuts import render, HttpResponse
from avatar import models
import uuid


def upload(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        avatar = request.FILES.get('avatar')
        filename = avatar.name
        if filename.split('.')[-1] not in ['jpeg', 'jpg', 'png']:
            return HttpResponse('error')
        filename = '{}.{}'.format(uuid.uuid4().hex, filename.split('.')[-1])
        avatar.name = filename
        models.User.objects.create(username=name, avatar=avatar)
        return HttpResponse('ok')

    return render(request, 'avatar/upload.html')
