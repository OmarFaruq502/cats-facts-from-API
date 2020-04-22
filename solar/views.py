from django.shortcuts import render
from django.http import HttpResponse
import requests
import base64
import io
import urllib
from datetime import datetime

import matplotlib.pyplot as plt

# Create your views here.
def covid(request):
    dates = range(1,31)
    spain = []
    italy = []

    Spain_response = requests.get('https://api.covid19api.com/country/spain/status/confirmed?from=2020-03-01T00:00:00Z&to=2020-04-01T00:00:00Z')
    Italy_response = requests.get('https://api.covid19api.com/country/italy/status/confirmed?from=2020-03-01T00:00:00Z&to=2020-04-01T00:00:00Z')

    spain_data = Spain_response.json()
    italy_data = Italy_response.json()

    for i in range(30):
        spain.append(spain_data[i]["Cases"])
        italy.append(italy_data[i]["Cases"])


    # plot the data
    plt.title("Spain vs Italy covid-19 Toatl Cases")

    plt.plot(dates, spain, 'ro-', linewidth=5, markersize=5, alpha=0.35)
    plt.plot(dates, italy, 'go-', linewidth=5, markersize=5, alpha=0.35)

    plt.legend(["Spain", "Italy"])

    plt.xlabel('Date')
    plt.ylabel('Cases')
    
    plt.gcf().autofmt_xdate()

    # generate figure and send it to the html template
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return render(request, 'home.html', {'data': uri})