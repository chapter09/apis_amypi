# coding=UTF-8

from django.http import HttpResponse
from django.http import Http404
from django.views.generic import View
from django.shortcuts import render_to_response
import urllib, urllib2, json

def search(request):
    #print request 

    keywords = request.GET.get('q').strip().encode('utf-8')
    num = request.GET.get('count').strip()
    # input check

    if int(num) > 5000 or len(keywords) > 200:
        return HttpResponse('Please enter valid params!', mimetype='text/plain')

    #if tel.isdigit() and len(tel) == 11:
    
    params = {'q': keywords, 'count': num}

    r = urllib2.\
            urlopen('http://api.douban.com/v2/music/search?%s'%urllib.urlencode(params))
    html = r.read()
    data = json.loads(html)

    #    if data['queryresult'] == "True":
    return HttpResponse(json.dumps(data, encoding="utf-8", ensure_ascii=False), mimetype='application/json')
    #    else:
    #        return HttpResponse("The phone number does not exist.", mimetype='text/plain')
    #else:
    #    return HttpResponse("Please enter a valid phone number!", mimetype='text/plain')

def id(request):
    
    id = request.GET.get('id').strip()
    
    if len(id) > 10:
        return HttpResponse('Please enter valid params!', mimetype='text/plain')

    r = urllib2.\
            urlopen('http://api.douban.com/v2/music/%s'%id)
    html = r.read()
    data = json.loads(html)

    #    if data['queryresult'] == "True":
    return HttpResponse(json.dumps(data, encoding="utf-8", ensure_ascii=False), mimetype='application/json')
