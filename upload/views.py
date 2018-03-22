# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Person
# from django.contrib.gis import geoip2
# from django.contrib.gis.geoip2 import GeoIP2
# Create your views here.

def login(request):
	# return HttpResponse('sff')
	return render(request,'upload/upload_form.html')


def filled(request):
# 	if request.method == "POST":
# 		name = request.POST['name']
# 		email = request.POST['e-mail']
# 		phone = request.POST['phone']
# 		client_ip = request.META['REMOTE_ADDR']
# 		print client_ip
# 		g=GeoIP2()
# 		city=g.city(client_ip)


# 		if 'file' in request.FILES:
# 			myfile=request.FILES['file']
# 		else:
# 			myfile = None
# 		x=Person(name=name,email=email,phone=phone,file=myfile,ip_addr=client_ip,country=city['country_name'],
# 			country_code=city['country_code'],
# 			city=city['city'],
# 			city_postal_code=city['postal_code'],
# 			latitude=city['latitude'],
# 			longitude=city['longitude'],
# 			dma_code=city['dma_code'],)
# 		x.save()

# 		return render(request,'upload/success.html',{'country':city['country_name'],
# 			'country_code':city['country_code'],
# 			'city':city['city'],
# 			'city_postal_code':city['postal_code'],
# 			'latitude':city['latitude'],
# 			'longitude':city['longitude'],
# 			'dma_code':city['dma_code'],

# 			})