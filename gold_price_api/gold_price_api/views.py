# coding=UTF-8

from django.http import HttpResponse
from django.http import Http404
from django.views.generic import View
from django.shortcuts import render_to_response
import httplib, urllib, json, urllib2


def query(request):
    url = 'services.packetizer.com'

    headers = {
            "Accept": "application/json",
            }

    conn = httplib.HTTPConnection(url, 80)
    conn.request('GET', '/spotprices/', '', headers)
     
    response = conn.getresponse()
    
    ret = response.read()

    print ret

    return HttpResponse(ret, mimetype='application/json')

