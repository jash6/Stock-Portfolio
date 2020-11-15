from django.shortcuts import render,redirect
from .models import Stock
from django.contrib import messages
from .forms import StockForm

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
    import requests
    import json

    if request.method == 'POST':
        form =StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request,("Stock has been Added!"))
            return redirect('dashboard')
        
    else:  
        ticker =Stock.objects.all()
        output =[]
        for ticker_item in ticker:
            api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=pk_873df7d7e66c4c1fac2b36e03ab53d51")

            try:
                api =json.loads(api_request.content)
                output.append(api)
            except Exception as e:
                api = "Error..."
        return render(request, 'dashboard.html',{'ticker':ticker,'output': output})



def delete(request, stock_id):
    item= Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request,("Stock has been deleted"))
    return redirect(deletestock)

def deletestock(request):
    ticker = Stock.objects.all()
    return render(request, 'deletestock.html',{'ticker': ticker})