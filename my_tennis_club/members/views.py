# from django.shortcuts import render
# from django.http import HttpResponse

# def members(request):
#     return HttpResponse("Hello world!")

# from django.http import HttpResponse
# from django.template import loader

# def members(request):
#   template = loader.get_template('myfirst.html')
#   return HttpResponse(template.render())

from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.db.models import Q


def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template("all_members.html")
    context = {
        "mymembers": mymembers,
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template("details.html")
    context = {
        "mymember": mymember,
    }
    return HttpResponse(template.render(context, request))


def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())


def testing(request):
    #mymembers = Member.objects.filter(firstname='Emil', id=2).order_by('firstname').values() #AND
    mymembers = Member.objects.filter(Q(firstname='Emil') | Q(firstname='Tobias') | Q(firstname__startswith='L')).values() #OR
    template = loader.get_template("template.html")
    context = {
        "mymembers": mymembers,
    }
    return HttpResponse(template.render(context, request))

# def testing(request):
#     mydata = Member.objects.all()
#     # mydata = Member.objects.all().values()
# mydata = Member.objects.values_list('firstname')
#     template = loader.get_template('template.html')
#     context = {
#         'mymembers': mydata,
#     }
#     return HttpResponse(template.render(context, request))