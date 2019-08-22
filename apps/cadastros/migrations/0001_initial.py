# Generated by Django 2.2.4 on 2019-08-22 19:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(help_text='Informe seu nome completo', max_length=50, unique=True)),
                ('email', models.EmailField(help_text='Informe seu endereço de E-mail', max_length=50, unique=True)),
                ('telefone', models.CharField(blank=True, max_length=20, null=True)),
                ('cadastrado_em', models.DateTimeField(auto_now_add=True)),
                ('codigo', models.UUIDField(default=uuid.uuid4, editable=False)),
            ],
            options={
                'ordering': ['nome_completo'],
            },
        ),
    ]
