# Generated by Django 5.1 on 2024-08-21 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='descripcion',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='evento',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='eventos/'),
        ),
    ]
