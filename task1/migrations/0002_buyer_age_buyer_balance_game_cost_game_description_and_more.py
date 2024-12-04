# Generated by Django 5.1.3 on 2024-12-02 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='buyer',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='game',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='game',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='game',
            name='size',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]