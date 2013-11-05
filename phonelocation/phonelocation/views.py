# coding=UTF-8

from django.http import HttpResponse
from django.http import Http404
from django.views.generic import View
from django.shortcuts import render_to_response
import urllib2, json

def query(request):
    #print request 

    tel = request.GET.get('tel').strip()
    # input check
    if tel.isdigit() and len(tel) == 11:
        r = urllib2.\
                urlopen('http://cz.115.com/?ct=index&ac=get_mobile_local&mobile=%s'%tel)
        html = r.read()
        data = json.loads(html[1:-1].strip())
        
        if data['queryresult'] == "True":
            return HttpResponse(json.dumps(data, encoding="utf-8", ensure_ascii=False), mimetype='application/json')
        else:
            return HttpResponse("The phone number does not exist.", mimetype='text/plain')
    else:
        return HttpResponse("Please enter a valid phone number!", mimetype='text/plain')

