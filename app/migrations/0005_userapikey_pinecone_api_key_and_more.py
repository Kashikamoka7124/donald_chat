# Generated by Django 5.0.1 on 2024-03-17 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alloweduser'),
    ]

    operations = [
        migrations.AddField(
            model_name='userapikey',
            name='pinecone_api_key',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='userapikey',
            name='pinecone_index_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
