import jwt
import datetime
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, logout
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

# Create your views here.

HEADERS = {
    "type": "jwt",
    "algorithms": "HS256"
}


def _get_response(message=None, data=None):
    if message == 'success' and isinstance(data, dict):
        return JsonResponse({'code': 0, 'message': 'success', 'data': data}, status=200, safe=False, json_dumps_params={"ensure_ascii": False})
    elif message == 'fail' and isinstance(data, dict):
        return JsonResponse({'code': 1, 'message': 'fail', 'data': data}, status=400, safe=False, json_dumps_params={"ensure_ascii": False})
    else:
        return JsonResponse({}, status=400, safe=False, json_dumps_params={"ensure_ascii": False})


@csrf_exempt
@require_http_methods(['POST'])
def user_login(request):
    """
    User Login
    :param request:
    :return:
    """
    username = request.POST.get('username')
    password = request.POST.get('password')
    user_data = {}
    if username and password:

        # normal
        user_obj = authenticate(username=username, password=password)
        if user_obj and user_obj.is_active:
            return _get_response(message='success', data={
                        'uid': user_obj.id,
                        'username': user_obj.username,
                        'password': password,
                    })
        # JWT
        # if not request.META.get('HTTP_AUTHORIZATION', ''):
        #     user_obj = authenticate(username=username, password=password)
        #     if user_obj and user_obj.is_active:
        #         payload = {
        #             'user_data': {
        #                 'id': user_obj.id,
        #                 'username': user_obj.username,
        #                 'password': password,
        #             },
        #             'expire': (datetime.datetime.utcnow() + datetime.timedelta(seconds=10)).strftime("%Y-%m-%d %H:%M:%S"),
        #         }
        #         token = jwt.encode(payload, settings.SECRET_KEY, headers=HEADERS).encode('utf-8').decode()
        #         return _get_response(message='success', data={'token': token})
        # else:
        #     authorization = request.META.get('HTTP_AUTHORIZATION', '')
        #     auth = authorization.split()
        #     if not auth or len(auth) != 1:
        #         pass
        #     else:
        #         token = auth[0]
        #         payload = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')
        #         # 刷新token失效日期
        #         token = jwt.encode(payload, settings.SECRET_KEY, headers=HEADERS).encode('utf-8').decode()
        #         return _get_response(message='success', data={'token': token})

    else:
        return _get_response(message='fail', data=user_data)


@csrf_exempt
@require_http_methods(['POST'])
def change_password(request):
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


@csrf_exempt
@require_http_methods(['POST'])
def get_info(request):
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


@csrf_exempt
@require_http_methods(['GET'])
def login_logout(request):
    """
    Logout
    :param request:
    :return:
    """
    logout(request)
    return _get_response(message='success', data={})
