# Generated by Django 4.1.5 on 2023-03-06 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_alter_posts_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='greenposts',
            name='image',
            field=models.ImageField(default='/media/posts/default.jpg', upload_to='posts'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(default='/media/posts/default.jpg', upload_to='posts'),
        ),
    ]
