from django.shortcuts import render
from.models import TeamMembers


def index(request):
    members = TeamMembers.objects.all()
    return render(request, 'sampleapp/index.html', {'members': members})

# Create your views here.
