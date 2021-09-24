import json
import jwt

from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from api.models import Boleta


# Create your views here. 
def get(request, id=0):
    if (id > 0):
        ticket = list(Boleta.objects.filter(id=id).values())

        if len(ticket) > 0:
            boleta = ticket[0]
            encode = jwt.encode({'game': 'data'}, 'bolt', algorithm='HS256')
            print(encode)
            data = {'message': "Success", 'boleta': boleta, 'encode': encode}
            value = jwt.decode(encode, 'bolt', algorithms=['HS256'])
            print(value)
        else:
            data = {'message': "Boleta not found..."}
        return JsonResponse(data)
    else:
        ticket = list(Boleta.objects.values())
        if len(ticket) > 0:
            data = {'message': 'Success', 'ticket': ticket}
        else:
            data = {'message': 'ticket not found...'}
        return JsonResponse(data)


@csrf_exempt
def post(request):
    jd = json.loads(request.body)
    Boleta.objects.create(usuario_id=jd['usuario'], fecha=jd['fecha'], detalle=jd['detalle'], total=jd['total'])
    data = {'message': "Success"}
    return JsonResponse(data)


@csrf_exempt
def put(request, id):
    jd = json.loads(request.body)
    ticket = list(Boleta.objects.filter(id=id).values())

    if len(ticket) > 0:
        boleta = Boleta.objects.get(id=id)
        boleta.usuario_id = jd['usuario']
        boleta.fecha = jd['fecha']
        boleta.detalle = jd['detalle']
        boleta.total = jd['total']
        boleta.save()
        data = {'message': "Boleta updated..."}
    else:
        data = {'message': "Boleta not found..."}
    return JsonResponse(data)


@csrf_exempt
def delete(request, id):
    ticket = list(Boleta.objects.filter(id=id).values())

    if len(ticket) > 0:
        Boleta.objects.get(id=id).delete()
        data = {'message': "Success"}
    else:
        data = {'message': "Boleta not found..."}
    return JsonResponse(data)
