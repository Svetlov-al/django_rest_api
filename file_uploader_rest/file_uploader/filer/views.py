from typing import List

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from filer.models import File
from filer.serializers import FileSerializer
from filer.tasks import process_file


@api_view(['POST'])
def upload_file(request: Request) -> Response:
    if request.method == 'POST':
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            process_file.delay(serializer.instance.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({"detail": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def list_files(request: Request) -> Response:
    files: List[File] = File.objects.all()
    serializer = FileSerializer(files, many=True)
    return Response(serializer.data)
