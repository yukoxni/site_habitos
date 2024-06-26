# Generated by Django 5.0.2 on 2024-03-24 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=200)),
                ('sobrenome', models.TextField(max_length=200)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('senha_hash', models.CharField(max_length=128)),
            ],
        ),
    ]
