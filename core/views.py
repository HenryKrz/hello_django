from django.shortcuts import render, HttpResponse

# Create your views here.


def hello(request, nome):
    return HttpResponse('<h1>Hello {}</h1>'.format(nome))


def soma(request, num1, num2):
    return HttpResponse('<h1>A soma é {}</h1>'.format(num1 + num2))


def subtracao(request, num1, num2):
    return HttpResponse('<h1>A subtração é {}</h1>'.format(num1 - num2))


def multiplicacao(request, num1, num2):
    return HttpResponse('<h1>A multiplicação é {}</h1>'.format(num1 * num2))


def divisao(request, num1, num2):
    return HttpResponse('<h1>A divisao é {}</h1>'.format(num1 / num2))