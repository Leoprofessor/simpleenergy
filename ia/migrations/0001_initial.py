# Generated by Django 3.2.18 on 2023-02-23 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Referencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arquivo_ia', models.FileField(blank=True, null=True, upload_to='')),
                ('codigo', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
