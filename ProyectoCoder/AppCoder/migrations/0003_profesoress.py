# Generated by Django 4.1.3 on 2022-12-01 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_curso_fecha_creacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profesoress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
            ],
        ),
    ]
