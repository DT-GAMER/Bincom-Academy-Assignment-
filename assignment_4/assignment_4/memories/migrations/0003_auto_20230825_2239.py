# Generated by Django 3.1.7 on 2023-08-25 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memories', '0002_auto_20230824_0219'),
    ]

    operations = [
        migrations.AddField(
            model_name='memory',
            name='title',
            field=models.CharField(default='Untitled Memory', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='memory',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='memories/videos/'),
        ),
    ]
