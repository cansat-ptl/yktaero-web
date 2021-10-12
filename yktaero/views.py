from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render


def index(request):
    return render(request, 'yktaero/index.html')


def news(request):
    return render(request, 'yktaero/news.html')


def contacts(request):
    return render(request, 'yktaero/about/contacts.html')


def staff(request):
    return render(request, 'yktaero/about/staff.html')


def partners(request):
    return render(request, 'yktaero/about/partners.html')


def payloads(request):
    return render(request, 'yktaero/projects/payloads.html')


def yktsat(request):
    return render(request, 'yktaero/projects/yktsat.html')


def rockets(request):
    return render(request, 'yktaero/projects/sounding-rockets.html')


def ground(request):
    return render(request, 'yktaero/projects/ground-equipment.html')