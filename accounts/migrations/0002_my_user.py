# Generated by Django 4.2 on 2023-07-31 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='my_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('is_superuser', models.CharField(max_length=5)),
            ],
        ),
    ]
