# Generated by Django 4.0.5 on 2022-06-30 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgmgt', '0009_stock_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
