from uuid import uuid4
import logging

logger = logging.getLogger(__name__)

def get_course_image(instance, filename):
    uid = str(uuid4()).split("-")[-1]
    return f"{instance.uid}{'image'}{instance.title}{uid}-{filename}"