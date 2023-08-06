from django.http import HttpResponse


class HttpResponseEmpty(HttpResponse):
    status_code = 204
