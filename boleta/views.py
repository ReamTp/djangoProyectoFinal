import json
import jwt

from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from api.models import Boleta, DetalleExtra, DetalleProducto


# Create your views here. 
def get(request, id=0):
    try:
        if id > 0:
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
    except:
        return HttpResponse(status=400)


@csrf_exempt
def post(request):
    try:
        jd = json.loads(request.body)
        newBallot = Boleta.objects.create(usuario_id=jd['usuario'], fecha=jd['fecha'], detalle=jd['detalle'], total=jd['total'])
        ballot = newBallot.id

        products = list(jd['productos'])
        pResult = insertProductsBallot(ballot, products)

        extras = list(jd['extras'])
        eResult = insertExtraBallot(ballot, extras)

        if not eResult or not pResult:
            return HttpResponse(status=400)

        data = {'message': "Success"}
        return JsonResponse(data)
    except:
        return HttpResponse(status=400)


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


def insertProductsBallot(bill, products):
    try:
        if len(products) > 0:
            for prod in products:
                DetalleProducto.objects.create(boleta_id=bill, producto_id=prod['producto'], cantidad=prod['cantidad'])

        return True
    except:
        return False


def insertExtraBallot(bill, extras):
    try:
        if len(extras) > 0:
            for extra in extras:
                DetalleExtra.objects.create(boleta_id=bill, extra_id=extra["extra"], cantidad=["cantidad"])

        return True
    except:
        return False
