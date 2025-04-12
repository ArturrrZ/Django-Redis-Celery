from __future__ import absolute_import, unicode_literals

# Так Celery будет автоматически находить задачи в этом приложении
from .tasks import celery_send