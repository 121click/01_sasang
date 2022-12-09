from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def map(request):
    return render(request, 'map.html')

from django.http import JsonResponse
from map.models import Point
from django.forms.models import model_to_dict


def map_data(request):
  data = Point.objects.all()
  print(data)
  lat = request.GET.get('lat')
  lng = request.GET.get('lng')
  map_list = []
  for d in data:
    d = model_to_dict(d)  # QuerySet -> Dict
    dist = distance(float(lat), float(lng), d['lat'], d['lng'])
    if(dist <= 100):  # 100km 이내의 장소만 응답결과로 저장
      map_list.append(d)
  # dict가 아닌 자료는 항상 safe=False 옵션 사용
  return JsonResponse(map_list, safe=False)


import math
def distance(lat1, lng1, lat2, lng2)  :
  theta = lng1 - lng2
  dist1 = math.sin(deg2rad(lat1)) * math.sin(deg2rad(lat2))

  dist2 = math.cos(deg2rad(lat1)) * math.cos(deg2rad(lat2)) 
  dist2 = dist2* math.cos(deg2rad(theta))

  dist = dist1 + dist2

  dist = math.acos(dist)
  dist = rad2deg(dist) * 60 * 1.1515 * 1.609344

  return dist

def deg2rad(deg):
  return deg * math.pi / 180.0

def rad2deg(rad):
  return rad * 180.0 / math.pi
