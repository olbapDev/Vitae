# Generated by Django 3.1.6 on 2021-02-24 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conocimiento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conocimiento',
            name='nivel',
            field=models.CharField(default='basico', max_length=100),
        ),
    ]
