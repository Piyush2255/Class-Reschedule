# Generated by Django 2.2.6 on 2019-11-11 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_auto_20191111_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='t12_1',
            name='friday_copy',
            field=models.CharField(default='empty', max_length=20),
        ),
        migrations.AddField(
            model_name='t12_1',
            name='monday_copy',
            field=models.CharField(default='empty', max_length=20),
        ),
        migrations.AddField(
            model_name='t12_1',
            name='thursday_copy',
            field=models.CharField(default='empty', max_length=20),
        ),
        migrations.AddField(
            model_name='t12_1',
            name='tuesday_copy',
            field=models.CharField(default='empty', max_length=20),
        ),
        migrations.AddField(
            model_name='t12_1',
            name='wednesday_copy',
            field=models.CharField(default='empty', max_length=20),
        ),
    ]
