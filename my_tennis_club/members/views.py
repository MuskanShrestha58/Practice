from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member


# Create your views here.


def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))


def details(request, id):  # gets the id as an argument
    # uses id to locate the correct record in the Member table
    mymember = Member.objects.get(id=id)
    # loads the details.html template
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember  # creates an object containing the member
    }
    return HttpResponse(template.render(context, request))
# kunai naya view banaune bittikai teslai tei view bhako app ko urls.py ma gayera connect gardinuparcha url patterns ma halera


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def testing(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('template.html')
    context = {
        'mymembers': mymembers,

    }
    return HttpResponse(template.render(context, request))
