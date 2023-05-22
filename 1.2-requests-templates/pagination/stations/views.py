from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from pagination.settings import BUS_STATION_CSV
import csv

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    data_file = BUS_STATION_CSV
    print(data_file)
    with open (data_file, newline='', encoding = 'utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        CONTENT = [{'Name':row['StationName'], 'Street':row['Street'], 'District':row['District']} for row in reader]
        page_num = int(request.GET.get("page", 1))
        paginator = Paginator(CONTENT, 10)
        page = paginator.get_page(page_num)
        #также передайте в контекст список станций на странице
        bus_stations = [{'bus_station':line['Name']} for line in page]
        print('---'*10)
        print(bus_stations)
    context = {
        'bus_stations': CONTENT,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
