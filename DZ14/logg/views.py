import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Bug
from .serializers import BugSerializer

logger = logging.getLogger('bugs')

class BugListCreateAPIView(APIView):
    
    def get(self, request):
        bugs = Bug.objects.all()
        serializer = BugSerializer(bugs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BugSerializer(data=request.data)
        if serializer.is_valid():
            bug = serializer.save()
            logger.info(f"Баг створено успішно: ID {bug.id}")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        
        logger.warning(f"Помилка валідації при створенні: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BugDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            bug = Bug.objects.get(pk=pk)
            serializer = BugSerializer(bug)
            return Response(serializer.data)
        except Bug.DoesNotExist:
            logger.error(f"Спроба доступу до неіснуючого бага ID {pk}")
            return Response({"error": "Баг не знайдено"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        bug = get_object_or_404(Bug, pk=pk)
        serializer = BugSerializer(bug, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info(f"Баг ID {pk} оновлено")
            return Response(serializer.data)
        
        logger.warning(f"Помилка валідації при оновленні бага {pk}: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        bug = get_object_or_404(Bug, pk=pk)
        bug.delete()
        logger.info(f"Баг ID {pk} видалено")
        return Response(status=status.HTTP_204_NO_CONTENT)