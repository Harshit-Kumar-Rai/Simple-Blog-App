# Generated by Django 4.1.7 on 2023-07-02 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_blogpost_model_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='model_cat',
            field=models.CharField(default='Tehnology', max_length=25),
        ),
    ]