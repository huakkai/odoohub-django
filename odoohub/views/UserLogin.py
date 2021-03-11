import jwt
import datetime
from django.contrib.auth import authenticate
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .Base import _get_response


HEADERS = {
    "type": "jwt",
    "algorithms": "HS256"
}


@csrf_exempt
@require_http_methods(['POST'])
def login(request):
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
        #             'expire': (datetime.datetime.utcnow() + datetime.timedelta(seconds=10)).strftime("%Y-%m-%d %H:%M:%S")
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
