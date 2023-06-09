# Generated by Django 4.2 on 2023-05-19 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_contact_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='static/images/')),
            ],
            options={
                'verbose_name': 'Projects',
            },
        ),
    ]
