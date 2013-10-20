# coding=UTF-8

from django.http import HttpResponse
from django.http import Http404
from django.views.generic import View
from django.shortcuts import render_to_response
import urllib2, json

keys = ['gid', 'name', 'todayStartPri', 'yestodEndPri', 'nowPri', 'todayMax', 'todayMin', 'competitivePri', 'reservePri', 'traNumber', 'traAmount', 'buyOne', 'buyOnePri', 'buyTwo', 'buyTwoPri', 'buyThree', 'buyThreePri', 'buyFour', 'buyFourPri', 'buyFive', 'buyFivePri', 'sellOne', 'sellOnePri', 'sellTwo', 'sellTwoPri', 'sellThree', 'sellThreePri', 'sellFour', 'sellFourPri', 'sellFive', 'sellFivePri', 'date', 'time']

values = []

def query(request):
    #print request 
    #if :
        # 404 address not found

    #r = urllib2.urlopen('http://hq.sinajs.cn/list=%s'%param)
    gid = request.GET.get('gid')
    values.append(gid)

    r = urllib2.urlopen('http://hq.sinajs.cn/list=%s'%gid)
    #html = r.read().decode('gb18030').encode('utf-8')
    html = r.read().decode('gb18030')
    
    # process those strings

    values.extend(html.split('=')[1][1:-3].split(','))

    data = {"result":[{"data":dict(zip(keys, values))}]}


    # return json object
    return HttpResponse(json.dumps(data, ensure_ascii=False), mimetype='application/json')

