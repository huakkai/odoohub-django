from django.http import JsonResponse, HttpResponse


def _get_response(message=None, data=None):
    if message == 'success' and isinstance(data, dict):
        return JsonResponse({'code': 0, 'message': 'success', 'data': data}, status=200, safe=False, json_dumps_params={"ensure_ascii": False})
    elif message == 'fail' and isinstance(data, dict):
        return JsonResponse({'code': 1, 'message': 'fail', 'data': data}, status=400, safe=False, json_dumps_params={"ensure_ascii": False})
    else:
        return JsonResponse({}, status=400, safe=False, json_dumps_params={"ensure_ascii": False})
