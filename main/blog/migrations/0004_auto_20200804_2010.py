# Generated by Django 3.1 on 2020-08-04 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200804_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.ForeignKey(default='Undefined', on_delete=django.db.models.deletion.CASCADE, to='blog.category', unique=True),
        ),
    ]