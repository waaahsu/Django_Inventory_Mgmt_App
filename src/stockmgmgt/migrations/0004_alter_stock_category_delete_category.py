# Generated by Django 4.0.5 on 2022-06-28 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgmgt', '0003_alter_stock_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='category',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
