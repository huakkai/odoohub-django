from django.contrib.auth import logout as _logout
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .Base import _get_response


@csrf_exempt
@require_http_methods(['GET'])
def logout(request):
    """
    Logout
    :param request:
    :return:
    """
    _logout(request)
    return _get_response(message='success', data={})
