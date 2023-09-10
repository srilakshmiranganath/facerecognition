from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializers import StudentSerializer
from django.core.files.storage import FileSystemStorage
from .models import Student
from face_recognition import compare_faces, face_encodings, load_image_file
import os

class UploadViewSet(ViewSet):
    serializer_class = StudentSerializer
    
    def create(self, request):
        if request.method == 'POST':
            serializer = StudentSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()

            response = "POST API and you have uploaded and saved a file"
            return Response(response)
        respones = "Invalid request method"
        return Response(response)

