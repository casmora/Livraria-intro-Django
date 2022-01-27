
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

from core.models import Categoria

import json


@method_decorator(csrf_exempt, name ="dispatch")
class CategoriaView(View):
    def get(self,request, id =None):
        if id:
            qs = Categoria.objects.get(id=id)
            data = {}
            data['id'] = qs.id
            data['descrição'] = qs.descrição
            return JsonResponse(data)
        else:
            data = list(Categoria.objects.values())
            formatted_data = json.dumps(data, ensure_ascii=False)
            return HttpResponse(formatted_data, content_type="application/json")

    def post(self, request):
        json_data = json.loads(request.body)
        nova_categoria = Categoria.objects.create(**json_data)
        data = {"id": nova_categoria.id, "descrição": nova_categoria.descrição}
        return JsonResponse(data)

    def patch(self, request, id):
        json_data = json.loads(request.body)
        qs = Categoria.objects.get(id=id)
        qs.descrição = json_data[ 'descrição'] #if 'descrição' in json_data else qs.descrição 
        qs.save()
        data = {}
        data['id'] = qs.id
        data['descrição'] = qs.descrição
        return JsonResponse(data)

    def delete(self, request, id):
        qs = Categoria.objects.get(id=id)     
        qs.delete()
        data = {'mensagem': "Item ecluido com sucesso."}
        return JsonResponse(data)        