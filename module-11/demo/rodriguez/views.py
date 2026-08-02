# Jose Rodriguez
# 8/2/2026
# Module 11.2 Assignment
# Django Basics

from django.http import HttpResponse


def home(request):
    return HttpResponse("Rodriguez says Hello!")