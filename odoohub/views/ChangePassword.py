from django.contrib.auth import authenticate
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .Base import _get_response


@csrf_exempt
@require_http_methods(['POST'])
def password(request):
    """
    Change Password
    :param request:
    :return:
    """
    old_password = request.POST.get('old_password')
    new_password = request.POST.get('old_password')
    username = request.POST.get('username')
    if old_password and new_password and username:
        user_obj = authenticate(username=username, password=old_password)
        if user_obj:
            try:
                user_obj.set_password(new_password)
            except Exception as e:
                return _get_response(message='fail', data={})
            return _get_response(message='success', data={'username': username, 'password': new_password})
    else:
        return _get_response(message='fail', data={})
