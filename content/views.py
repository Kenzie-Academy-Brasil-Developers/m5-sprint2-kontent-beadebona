from urllib.request import Request

from django.forms import model_to_dict
from rest_framework.views import APIView, Response

from content.models import Content

from .content_serializer import ContentSerializer


class ContentView(APIView):
    def get(self, request):
        contents = Content.objects.all()
        content_list = []
        for cont in contents:
            content_list.append(model_to_dict(cont))
        return Response(content_list, 200)

    def post(self, request):
        serial_content = ContentSerializer(**request.data)
        if serial_content.is_valid():
            content = Content.objects.create(**serial_content.data)
            content.save()
            content_dict = model_to_dict(content)
            return Response(content_dict, 201)
        else:
            return Response(serial_content.errors, 400)

class ContentDetailView(APIView):
    def get(self, request, content_id):
        try:
            content = Content.objects.get(id=content_id)
        except Content.DoesNotExist:
            return Response({"message": "Content not found."},404)
        content_dict = model_to_dict(content)
        return Response(content_dict, 200)

    def patch(self, request, content_id):
        try:
            content = Content.objects.get(id=content_id)
        except Content.DoesNotExist:
            return Response({"message": "Content not found."},404)

        content.title = request.data.get("title", content.title)
        content.module = request.data.get("module", content.module)
        content.students = request.data.get("students", content.students)
        content.description = request.data.get("description", content.description)
        content.is_active = request.data.get("is_active", content.is_active)

        content.save()

        content_dict = model_to_dict(content)

        return Response(content_dict, 200)

        
    def delete(self, request, content_id):
        try:
            content = Content.objects.get(id=content_id)
        except Content.DoesNotExist:
            return Response({"message": "Content not found."},404)
        
        content.delete()
        
        return Response(204)

class ContentFilterView(APIView):
    def get(self, request):
        title_param = request.query_params.get("title")

        contents = Content.objects.filter(title__contains=title_param)

        filtered_contents = [model_to_dict(content) for content in contents]

        return Response(filtered_contents, 200)
