# Generated by Django 4.0.5 on 2022-06-28 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgmgt', '0007_alter_category_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='export_to_CSV',
        ),
        migrations.AlterField(
            model_name='stock',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='stockmgmgt.category'),
        ),
    ]
