# Generated by Django 4.2.1 on 2023-07-08 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_login_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='static/media/settings')),
            ],
            options={
                'verbose_name_plural': 'Settings',
            },
        ),
    ]
