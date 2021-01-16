import time

from django.http import HttpResponse


def function_middleware(get_response):
    print('One time function middleware initialization')

    def my_function(request):
        print('Its before view function')
        time.sleep(3)
        response = get_response(request)
        print('Its after view function')
        return response

    return my_function


class BrotherMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        print('One time Brother class middleware initialization')

    def __call__(self, request):
        print('Its Brother before view function')

        time.sleep(3)
        response = self.get_response(request)
        print('Its Brother after view function')
        return response


class FatherMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        print('One time Father class middleware initialization')

    def __call__(self, request):
        print('Its Father before view function',
              '\n MotherMiddleware will not be called')

        time.sleep(3)
        # response = self.get_response(request)
        response = HttpResponse('You have to stop.'
                                '\n MotherMiddleware will not be called')
        print('Its Father after view function')
        return response


class MotherMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        print('One time Mother class middleware initialization')

    def __call__(self, request):
        print('Its Mother before view function')

        time.sleep(3)
        response = self.get_response(request)
        print('Its Mother after view function')
        return response

