# Generated by Django 4.1.5 on 2023-02-02 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_review_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='porject',
            name='featured_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]
