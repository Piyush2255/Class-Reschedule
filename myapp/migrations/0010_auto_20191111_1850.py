# Generated by Django 2.2.6 on 2019-11-11 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20191111_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='t8_9',
            name='friday_copy',
            field=models.CharField(default='empty', max_length=20),
        ),
        migrations.AddField(
            model_name='t8_9',
            name='monday_copy',
            field=models.CharField(default='empty', max_length=20),
        ),
        migrations.AddField(
            model_name='t8_9',
            name='thursday_copy',
            field=models.CharField(default='empty', max_length=20),
        ),
        migrations.AddField(
            model_name='t8_9',
            name='tuesday_copy',
            field=models.CharField(default='empty', max_length=20),
        ),
        migrations.AddField(
            model_name='t8_9',
            name='wednesday_copy',
            field=models.CharField(default='empty', max_length=20),
        ),
    ]
