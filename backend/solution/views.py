from requests import Response
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework import status
from rest_framework.response import Response
from .models import Solution
# from task.models import Task
from .serializers import SolutionSerializer, SolutionSerializerUpdate


class SolutionCreateView(generics.CreateAPIView):
    queryset = Solution.objects.all()
    # serializer_class = SolutionSerializerUpdate

    def post(self, request):
        serializer = SolutionSerializerUpdate(data=request.data)
        if serializer.is_valid():
            solution_result = serializer.set_result(request.data.get('solution_code'))
            serializer.save(result=solution_result)
            message = serializer.data
            return Response(message, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SolutionDetailView(generics.RetrieveAPIView):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer