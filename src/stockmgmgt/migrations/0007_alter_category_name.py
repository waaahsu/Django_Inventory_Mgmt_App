# Generated by Django 4.0.5 on 2022-06-28 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgmgt', '0006_alter_stock_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
