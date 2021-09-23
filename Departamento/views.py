import json
import jwt
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from api.models import Departamento
# Create your views here.
#holaaaaa

def get(request, id=0):
    if id > 0:
        departamentos = list(Departamento.objects.filter(id=id).values())
        token = jwt.encode({'departamentos': departamentos}, 'aim25x', algorithm="HS256")
        value = jwt.decode(token, 'aim25x', algorithms=['HS256'])
        print(value)
        if len(departamentos) > 0:
            departamento = departamentos[0]
            data = {'message':'Success','departamento':departamento}
        else:
            data = {"message":"departamento not found..."}
        
        return JsonResponse(data)
    else:
        departamentos = list(Departamento.objects.values())
        if len(departamentos) > 0:
            data = {"message":"Success","departamento":departamentos}
        else:
            data = {"message": "Usuarios not found..."}
        return JsonResponse(data)

@csrf_exempt
def post(request):
    jd = json.loads(request.body)
    Departamento.objects.create(nombre=jd['nombre'],estado=jd['estado'])
    data = {"message":'Success'}
    return JsonResponse(data)

@csrf_exempt
def put(request,id):
    jd = json.loads(request.body)
    departamentos = list(Departamento.objects.filter(id=id).values())
    if len(departamentos) > 0:
        departamento = Departamento.objects.get(id=id)
        departamento.nombre = jd['nombre']
        departamento.estado = jd['estado']
        departamento.save()
        data = {"message":"departamento updated..."}
    else:
        data = {'message':'departamento not found...'}
    return JsonResponse(data)

@csrf_exempt
def acEstado(request,id):
    departamentos = list(Departamento.objects.filter(id=id).values())
    if len(departamentos) > 0:
        departamento = Departamento.objects.get(id=id)
        departamento.estado = 1
        departamento.save()
        data = {"message":"departamento estado activado..."}
    else:
        data = {'message':'departamento not found...'}
    return JsonResponse(data)

@csrf_exempt
def desEstado(request,id):
    departamentos = list(Departamento.objects.filter(id=id).values())
    if len(departamentos) > 0:
        departamento = Departamento.objects.get(id=id)
        departamento.estado = 0
        departamento.save()
        data = {"message":"departamento estado desactivado..."}
    else:
        data = {'message':'departamento not found...'}
    return JsonResponse(data)
