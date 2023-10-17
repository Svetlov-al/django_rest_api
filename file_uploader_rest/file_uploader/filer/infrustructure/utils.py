from PIL import Image
from filer.models import File
from moviepy.editor import VideoFileClip


def get_file_type(file: File.file):
    """Функция определения типа файла"""
    file_extension = file.name.split('.')[-1].lower()
    if file_extension in ['jpg', 'jpeg', 'png']:
        return 'image'
    elif file_extension in ['txt', 'md', 'csv']:
        return 'text'
    elif file_extension in ['mp4', 'avi', 'mkv', 'flv']:
        return 'video'
    else:
        return 'unknown'


def process_uploaded_file(file_id: int):
    """Функция обработки файла"""
    file_instance = File.objects.get(id=file_id)
    file_type = get_file_type(file_instance.file)

    if file_type == 'image':
        with Image.open(file_instance.file.path) as img:
            img = img.resize((800, 600))
            img.save(file_instance.file.path)
            file_instance.processed = True

    elif file_type == 'text':
        file_instance.processed = True

    elif file_type == 'video':
        clip = VideoFileClip(file_instance.file.path)
        clip_resized = clip.resize(height=360)
        clip_resized.write_videofile(file_instance.file.path, codec='libx264')
        file_instance.processed = True

    file_instance.save()
