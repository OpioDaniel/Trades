from django.shortcuts import render


def home(request):
    return render(request, 'bless/home.html')


def acquisition(request):
    return render(request, 'bless/M$A.html')


def practise(request):
    return render(request, 'bless/practise.html')