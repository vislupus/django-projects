from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


def animal(request):
    return HttpResponse("Give me some animal!")


def animals(request, animal):
    if not animal.isdigit():
        return HttpResponse(f"<h1>This is a {animal}!</h1>")
    else:
        return HttpResponseNotFound("<h1>Strange animal!</h1>")


def pet(request, pet):
    # return HttpResponseRedirect(f"/animal-red/{pet}")

    redirect_path = reverse("animal-red", args=[pet])
    return HttpResponseRedirect(redirect_path)


def pet_red(request, pet):
    return HttpResponse(f'<h1 style="color:red;">This is a {pet}!</h1>')


monthly_challenges = {
    "january": "It is January!",
    "february": "It is February!",
    "march": "It is March!",
    "april": "It is April!",
    "may": "It is May!",
    "june": "It is June!",
    "july": "It is July!",
    "august": "It is August!",
    "september": "It is September!",
    "october": "It is October!",
    "november": "It is November!",
    "december": "It is December!",
}


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f'<li><a href="{month_path}">{capitalized_month}</a></li>'

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse(
        "month-challenge", args=[redirect_month]
    )  # /challenge/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
