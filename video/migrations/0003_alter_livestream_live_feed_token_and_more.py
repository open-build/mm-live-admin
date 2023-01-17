# Generated by Django 4.1.5 on 2023-01-16 23:44

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0002_livestream'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livestream',
            name='live_feed_token',
            field=models.FileField(blank=True, help_text='Video Stream Auth Token', max_length=255, null=True, storage=django.core.files.storage.FileSystemStorage(location='/Users/greglind/Projects/mediamash/mm-live-admin/media/videos/'), upload_to=''),
        ),
        migrations.AlterField(
            model_name='livestream',
            name='live_feed_url',
            field=models.FileField(blank=True, help_text='Video Stream Feed', max_length=255, null=True, storage=django.core.files.storage.FileSystemStorage(location='/Users/greglind/Projects/mediamash/mm-live-admin/media/videos/'), upload_to=''),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_file',
            field=models.FileField(blank=True, help_text='Upload Video', max_length=255, null=True, storage=django.core.files.storage.FileSystemStorage(location='/Users/greglind/Projects/mediamash/mm-live-admin/media/videos/'), upload_to=''),
        ),
    ]
