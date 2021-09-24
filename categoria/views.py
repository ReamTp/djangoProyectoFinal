import json
import jwt

from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from api.models import Categoria


# Create your views here. 
def get(request, id=0):
    if (id > 0):
        category = list(Categoria.objects.filter(id=id).values())

        if len(category) > 0:
            categoria = category[0]
            encode = jwt.encode({'game': 'data'}, 'cate', algorithm='HS256')
            print(encode)
            data = {'message': "Success", 'categoria': categoria, 'encode': encode}
            value = jwt.decode(encode, 'cate', algorithms=['HS256'])
            print(value)
        else:
            data = {'message': "Categoria not found..."}
        return JsonResponse(data)
    else:
        category = list(Categoria.objects.values())
        if len(category) > 0:
            data = {'message': 'Success', 'category': category}
        else:
            data = {'message': 'category not found...'}
        return JsonResponse(data)


@csrf_exempt
def post(request):
    jd = json.loads(request.body)
    Categoria.objects.create(nombre=jd['nombre'], descripcion=jd['descripcion'], estado=jd['estado'])
    data = {'message': "Success"}
    return JsonResponse(data)


@csrf_exempt
def put(request, id):
    jd = json.loads(request.body)
    category = list(Categoria.objects.filter(id=id).values())

    if len(category) > 0:
        categoria = Categoria.objects.get(id=id)
        categoria.nombre = jd['nombre']
        categoria.descripcion = jd['descripcion']
        categoria.estado = jd['estado']
        categoria.save()
        data = {'message': "Categoria updated..."}
    else:
        data = {'message': "Categoria not found..."}
    return JsonResponse(data)


@csrf_exempt
def delete(request, id):
    category = list(Categoria.objects.filter(id=id).values())

    if len(category) > 0:
        Categoria.objects.get(id=id).delete()
        data = {'message': "Success"}
    else:
        data = {'message': "Categoria not found..."}
    return JsonResponse(data)
