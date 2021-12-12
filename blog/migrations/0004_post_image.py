# Generated by Django 3.2.7 on 2021-09-07 11:06

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='posts/default.jpg', upload_to=blog.models.upload_to, verbose_name='Image'),
        ),
    ]