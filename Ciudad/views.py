import json
import jwt
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from api.models import Ciudad
# Create your views here.

def get(request, id=0):
    if id > 0:
        ciudades = list(Ciudad.objects.filter(id=id).values())
        token = jwt.encode({'ciudades': ciudades}, 'aim25x', algorithm="HS256")
        value = jwt.decode(token, 'aim25x', algorithms=['HS256'])
        print(value)
        if len(ciudades) > 0:
            ciudad = ciudades[0]
            data = {'message':'Success','ciudad':ciudad,'token':token}
        else:
            data = {"message":"ciudad not found..."}
        
        return JsonResponse(data)
    else:
        ciudades = list(Ciudad.objects.values())
        if len(ciudades) > 0:
            data = {"message":"Success","ciudades":ciudades}
        else:
            data = {"message": "ciudades not found..."}
        return JsonResponse(data)

@csrf_exempt
def post(request):
    jd = json.loads(request.body)
    Ciudad.objects.create(nombre=jd['nombre'],codigoPostal=jd['codigoPostal'],estado=jd['estado'], departamento_id=jd['departamento'])
    data = {"message":'Success'}
    return JsonResponse(data)

@csrf_exempt
def put(request,id):
    jd = json.loads(request.body)
    ciudades = list(Ciudad.objects.filter(id=id).values())
    if len(ciudades) > 0:
        ciudad = Ciudad.objects.get(id=id)
        ciudad.nombre = jd['nombre']
        ciudad.codigoPostal = jd['codigoPostal']
        ciudad.estado = jd['estado']
        ciudad.departamento_id = jd['departamento']
        ciudad.save()
        data = {"message":"ciudad updated..."}
    else:
        data = {'message':'ciudad not found...'}
    return JsonResponse(data)

@csrf_exempt
def acEstado(request,id):
    ciudades = list(Ciudad.objects.filter(id=id).values())
    if len(ciudades) > 0:
        ciudad = Ciudad.objects.get(id=id)
        ciudad.estado = 1
        ciudad.save()
        data = {"message":"ciudad estado activado..."}
    else:
        data = {'message':'ciudad not found...'}
    return JsonResponse(data)

@csrf_exempt
def desEstado(request,id):
    ciudades = list(Ciudad.objects.filter(id=id).values())
    if len(ciudades) > 0:
        ciudad = Ciudad.objects.get(id=id)
        ciudad.estado = 0
        ciudad.save()
        data = {"message":"ciudad estado desactivado..."}
    else:
        data = {'message':'diudad not found...'}
    return JsonResponse(data)
