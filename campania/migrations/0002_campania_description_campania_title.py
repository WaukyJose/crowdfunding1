# Generated by Django 5.0.6 on 2024-05-12 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campania', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='campania',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='campania',
            name='title',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
