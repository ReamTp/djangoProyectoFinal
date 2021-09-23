from django.http import JsonResponse
from .models import Departamento
import jwt


# Create your views here.
def getData(request):
    departs = list(Departamento.objects.values())
    token = jwt.encode({'departments': departs}, 'asd', algorithm="HS256")
    value = jwt.decode(token, 'asd', algorithms=['HS256'])
    print(value)
    data = {'data': token, 'response': True}
    return JsonResponse(data)

