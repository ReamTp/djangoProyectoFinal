import jwt
import json
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from api.models import Usuario
# Create your views here.

def get(request, id=0):
    if id > 0:
        usuarios = list(Usuario.objects.filter(id=id).values())
        token = jwt.encode({'usuarios': usuarios}, 'aim25x', algorithm="HS256")
        value = jwt.decode(token, 'aim25x', algorithms=['HS256'])
        print(value)
        if len(usuarios) > 0:
            usuario = usuarios[0]
            data = {'message':'Success','Usuario':usuario}
        else:
            data = {"message":"usuario not found..."}
        
        return JsonResponse(data)
    else:
        usuarios = list(Usuario.objects.values())
        if len(usuarios) > 0:
            data = {"message":"Success","usuarios":usuarios}
        else:
            data = {"message": "Usuarios not found..."}
        return JsonResponse(data)

@csrf_exempt
def post(request):
    jd = json.loads(request.body)
    Usuario.objects.create(nombres=jd['nombres'],apellidos=jd['apellidos'],telefono=jd['telefono'],direccion=jd['direccion'],ciudad_id=jd['ciudad'],correo=jd['correo'],genero=jd['genero'],avatar=jd['avatar'],contraseña=jd['contraseña'],estado=jd['estado'])
    data = {"message":'Success'}
    return JsonResponse(data)

@csrf_exempt
def put(request,id):
    jd = json.loads(request.body)
    usuarios = list(Usuario.objects.filter(id=id).values())
    if len(usuarios) > 0:
        usuario = Usuario.objects.get(id=id)
        usuario.nombres = jd['nombres']
        usuario.apellidos = jd['apellidos']
        usuario.telefono = jd['telefono']
        usuario.direccion = jd['direccion']
        usuario.ciudad_id = jd['ciudad']
        usuario.correo = jd['correo']
        usuario.genero = jd['genero']
        usuario.avatar = jd['avatar']
        usuario.contraseña = jd['contraseña']
        usuario.estado = jd['estado']
        usuario.save()
        data = {"message":"usuario updated..."}
    else:
        data = {'message':'usuario not found...'}
    return JsonResponse(data)

@csrf_exempt
def acEstado(request,id):
    usuarios = list(Usuario.objects.filter(id=id).values())
    if len(usuarios) > 0:
        usuario = Usuario.objects.get(id=id)
        usuario.estado = 1
        usuario.save()
        data = {"message":"usuario estado activado..."}
    else:
        data = {'message':'usuario not found...'}
    return JsonResponse(data)

@csrf_exempt
def desEstado(request,id):
    usuarios = list(Usuario.objects.filter(id=id).values())
    if len(usuarios) > 0:
        usuario = Usuario.objects.get(id=id)
        usuario.estado = 0
        usuario.save()
        data = {"message":"usuario estado desactivado..."}
    else:
        data = {'message':'usuario not found...'}
    return JsonResponse(data)



