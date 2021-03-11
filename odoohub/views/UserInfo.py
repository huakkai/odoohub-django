from django.contrib.auth import authenticate
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .Base import _get_response


@csrf_exempt
@require_http_methods(['POST'])
def get_user_info(request):
    """
    Get Info
    :param request:
    :return:
    """
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username and password:
        user_obj = authenticate(username=username, password=password)
        if user_obj:
            return _get_response(message='success', data={'username': username, 'password': password, 'email': user_obj.email})
    else:
        return _get_response(message='fail', data={})
