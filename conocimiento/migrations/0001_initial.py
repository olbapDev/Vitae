# Generated by Django 3.1.6 on 2021-02-24 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conocimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('nivel', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
        ),
    ]
