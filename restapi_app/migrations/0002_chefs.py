# Generated by Django 5.0.2 on 2024-03-06 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chefs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Culinary_Background', models.TextField()),
                ('Profession', models.TextField()),
            ],
        ),
    ]
