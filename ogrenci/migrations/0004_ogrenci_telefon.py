# Generated by Django 2.2.2 on 2019-06-18 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ogrenci', '0003_auto_20190618_0639'),
    ]

    operations = [
        migrations.AddField(
            model_name='ogrenci',
            name='telefon',
            field=models.CharField(default='+90 (222) 555 55 55', max_length=19),
        ),
    ]