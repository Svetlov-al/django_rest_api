from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
from rest_framework.test import APIClient
from filer.models import File


class FileAPITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_upload_file(self):
        file = SimpleUploadedFile("test_file.txt", b"file_content", content_type="text/plain")
        response = self.client.post('/upload/', {'file': file}, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        uploaded_file_id = response.data['id']
        self.assertTrue(File.objects.filter(id=uploaded_file_id).exists())

    def test_list_files(self):
        File.objects.create(file="test_file1.txt")
        File.objects.create(file="test_file2.txt")

        response = self.client.get('/files/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
