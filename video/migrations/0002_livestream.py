# Generated by Django 2.1.15 on 2020-09-29 18:05

from django.conf import settings
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LiveStream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Name of Channel', max_length=255, null=True)),
                ('link', models.CharField(blank=True, help_text='Link to Video Source', max_length=255, null=True)),
                ('live_feed_url', models.FileField(blank=True, help_text='Video Stream Feed', max_length=255, null=True, storage=django.core.files.storage.FileSystemStorage(location='/media//videos/'), upload_to='')),
                ('live_feed_token', models.FileField(blank=True, help_text='Video Stream Auth Token', max_length=255, null=True, storage=django.core.files.storage.FileSystemStorage(location='/media//videos/'), upload_to='')),
                ('description', models.TextField(blank=True, help_text='Description of Channel', null=True)),
                ('embed_code', models.CharField(blank=True, help_text='Code used to stream to ebeded player', max_length=255, null=True)),
                ('status', models.CharField(blank=True, help_text='Status of Streaming Channel', max_length=255, null=True)),
                ('stream_id', models.CharField(blank=True, help_text='Streaming Provider ID', max_length=255, null=True)),
                ('stream_url', models.CharField(blank=True, help_text='Streaming Provider URL', max_length=255, null=True)),
                ('playback_hls', models.CharField(blank=True, help_text='Streaming Provider URL for HLS stream', max_length=255, null=True)),
                ('playback_dash', models.CharField(blank=True, help_text='Streaming Provider URL for DASH stream', max_length=255, null=True)),
                ('is_live', models.BooleanField(default=False)),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('direct_provider', models.ManyToManyField(blank=True, help_text='Internal Streaming Host Provider Videos', related_name='stream_direct_provider', to='video.ProviderVideo')),
                ('external_provider', models.ManyToManyField(blank=True, help_text='External/Social Provider Shares', related_name='stream_external_provider', to='video.ProviderVideo')),
                ('owner', models.ForeignKey(blank=True, help_text='User who is the Owner of the Video', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'LiveStreams',
                'verbose_name_plural': 'LiveStreams',
                'ordering': ('name',),
            },
        ),
    ]
