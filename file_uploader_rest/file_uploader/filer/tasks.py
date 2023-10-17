from celery import shared_task

from filer.infrustructure.utils import process_uploaded_file


@shared_task
def process_file(file_id):
    process_uploaded_file(file_id)
