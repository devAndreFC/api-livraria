from django.http import HttpResponse, JsonResponse
from django.views import View 
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

import json

from .models import Category


@method_decorator(csrf_exempt, name='dispatch')
class CategoriesView(View):
    def get(self, request, id=None):
        if id:
            qs = Category.objects.get(id=id)
            data = {}
            data['id'] = qs.id
            data['name'] = qs.name
            data['description'] = qs.description
            return JsonResponse(data)

        data = list(Category.objects.values())
        formatted_data = json.dumps(data, ensure_ascii=False)
        return HttpResponse(formatted_data, content_type="application/json")
    
    def post(self, request):
        json_data = json.loads(request.body)
        new_category = Category.objects.create(**json_data)
        data = {
            "id": new_category.id,
            "name": new_category.name,
            "description": new_category.description
            }
        return JsonResponse(data)
    
    def patch(self, request, id):
        json_data = json.loads(request.body)
        qs = Category.objects.get(id=id)
        qs.name = json_data['name'] # if 'name' in json_data else qs.name
        qs.description = json_data['description'] # if 'description' in json_data else qs.description
        qs.save()
        data = {}
        data['id'] = qs.id
        data['name'] = qs.name
        data['description'] = qs.description
        
        return JsonResponse(data)
        
    def delete(self, request, id):
        qs = Category.objects.get(id=id)
        qs.delete()
        data = {'mensagem': 'Item excluído com sucesso!'}
        return JsonResponse(data)