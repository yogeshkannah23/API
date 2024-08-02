from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import requests
import json

# Create your views here.

def api_home(request,*args, **kwargs):
    body = request.body
    print(request.GET)
    print(request.POST)
    print(body)
    try:
        body = json.loads(body)
        print(body)
    except:
        pass
    data={} 
    data['headers'] = dict(request.headers) 
    data['content'] = request.content_type
    print(data)
    return JsonResponse({'name':'yogeshkannah'})
