# Generated by Django 2.1.4 on 2019-02-19 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0002_auto_20190219_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='evening',
            field=models.CharField(default=0, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='lunch',
            field=models.CharField(default=0, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='morning',
            field=models.CharField(default=0, max_length=50, null=True),
        ),
    ]