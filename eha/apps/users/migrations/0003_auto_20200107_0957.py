# Generated by Django 3.0.2 on 2020-01-07 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_deleted_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.URLField(default='https://res.cloudinary.com/health-id/image/upload/v1554552278/Profile_Picture_Placeholder.png', null=True),
        ),
    ]
