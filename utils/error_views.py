from django.http import JsonResponse


def handler404(request,exception):
    message = ('Url introvable')
    response = JsonResponse(data={'error': message})
    response.status_code = 404
    return response

def handler500(request):
    message = ('une errer est survenue')
    response = JsonResponse(data={'error': message})
    response.status_code = 500
    return response