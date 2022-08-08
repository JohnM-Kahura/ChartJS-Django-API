from rest_framework import generics
from  student.models import Student
from .serializers import StudentSerializer



class StudentList(generics.ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    
    
class StudentDetail(generics.RetrieveAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer