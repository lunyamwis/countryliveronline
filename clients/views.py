# Create your views here.
import csv

import pandas as pd
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import FetchClientsForm
from .models import Client

base_uri = "http://yellowpageskenya.com"
base_url = "https://yellowpageskenya.com"
url = "https://yellowpageskenya.com/search-results?what=restaurant&\
    keywords=restaurant&where=Nairobi"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/96.0.4664.110 Safari/537.36"
}
links, businesses = [], []


def view_clients(request, *args, **kwargs):
    """
    - view clients from db
    """
    clients = Client.objects.all()
    return render(request, "clients/index.html", {"clients": clients})


def fetch_clients(request, *args, **kwargs):
    """
    - for fetching clients
    """
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = FetchClientsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            start = form.cleaned_data["start"]
            stop = form.cleaned_data["stop"]
            # start = 23 stop =33
            for x in range(start, stop):
                links.append(
                    f"https://yellowpageskenya.com/search-results?page={x}&\
                        what=restaurant&where=Nairobi"
                )
            enterprises_ = []
            for link in links:
                print(link)
                r = requests.get(link, headers=headers)
                soup = BeautifulSoup(r.content, "html.parser")
                enterprises_.append(soup.find_all("div", class_="results-display"))

            for enterprise in enterprises_:
                print(enterprise)
                for item in enterprise:
                    name = item.find("h2", {"itemprop": "name"}).text
                    address = (
                        item.find("span", class_="streetaddress")
                        .text.strip()
                        .replace("\n", "")
                    )
                    try:
                        link = item.find("a", class_="bizemail")["href"]
                    except Exception as e:
                        link = ""
                    try:
                        website = item.find("a", class_="bizwebsite")["href"]
                    except Exception as e:
                        website = ""

                    phone_numbers = []
                    if "business-email" in link:
                        link = link.replace("business-email", "business-details")
                        link = f"{base_url}{link}"
                        raw = requests.get(link, headers=headers)
                        soup_ = BeautifulSoup(raw.content, "html.parser")
                        phone_numbers_ = soup_.find_all(
                            "a", class_="dropdown-item secondary"
                        )
                        for phone_number in phone_numbers_:
                            phone_numbers.append(phone_number.text)

                    business = {
                        "name": name,
                        "address": address,
                        "website": website,
                        "link": link,
                        "phone_numbers": phone_numbers,
                    }
                    Client.objects.create(**business)
                    businesses.append(business)
            df = pd.DataFrame(businesses)
            df.to_csv("prospectives.csv", index=False)

            return HttpResponseRedirect("/clients/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FetchClientsForm()

    return render(request, "clients/fetch.html", {"form": form})


def export_users_csv(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="prospective_clients.csv"'

    writer = csv.writer(response)
    writer.writerow(["name", "address", "website", "link", "phone_numbers"])

    users = Client.objects.all().values_list(
        "name", "address", "website", "link", "phone_numbers"
    )
    for user in users:
        writer.writerow(user)

    return response
