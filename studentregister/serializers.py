from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['StudentID', 'StudentName', 'StudentFace']

    def create(self, validated_data):
        return Student.objects.create(
            StudentID=validated_data['StudentID'],
            StudentName=validated_data['StudentName'],
            StudentFace=validated_data['StudentFace']
        )