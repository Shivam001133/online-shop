# Generated by Django 4.2 on 2024-01-27 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='user.jpg', upload_to='profile_icon.png'),
        ),
    ]
