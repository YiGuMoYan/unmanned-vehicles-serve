import hashlib
import os

from django.conf import settings

from utils.response import *
from video.models import Video


# Create your views here.
def upload(request):
    if request.method == "POST":
        file = request.FILES['file']
        filePath = os.path.join(settings.MEDIA_ROOT, file.name)
        print(file.name)
        file_data = file.read()
        md5_hash = hashlib.md5(file_data).hexdigest()
        if Video.objects.filter(md5=md5_hash).exists():
            return success_response({"url": settings.MEDIA_URL + file.name})
        # 保存文件
        with open(filePath, 'wb+') as fp:
            for info in file.chunks():
                fp.write(info)
        return success_response({"url": settings.MEDIA_URL + file.name})