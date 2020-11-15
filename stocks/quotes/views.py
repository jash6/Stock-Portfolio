from django.shortcuts import render

# Create your views here.
def home(request):
    import requests
    import json


    if request.method == 'POST':
        ticker= request.POST['ticker']
        #pk_873df7d7e66c4c1fac2b36e03ab53d51
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_873df7d7e66c4c1fac2b36e03ab53d51")

        try:
            api =json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        return render(request, 'home.html',{'api': api})

    else:
        return render(request, 'home.html',{'ticker': "Enter a Ticker Symbol Above..."})


def about(request):
    return render(request, 'about.html',{})

def dashboard(request):
    return render(request, 'dashboard.html',{})