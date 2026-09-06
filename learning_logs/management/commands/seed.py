from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from learning_logs.models import Topic, Entry

class Command(BaseCommand):
    def handle(self, *a, **kw):
        if User.objects.exists(): self.stdout.write('Skip.'); return
        u = User.objects.create_superuser('admin','','admin123')
        t1 = Topic.objects.create(text='Python', owner=u)
        t2 = Topic.objects.create(text='Django', owner=u)
        Entry.objects.create(topic=t1, text='Python — интерпретируемый язык с динамической типизацией.')
        Entry.objects.create(topic=t2, text='Django использует паттерн MTV. Миграции через makemigrations.')
        self.stdout.write(self.style.SUCCESS('Seed OK'))
