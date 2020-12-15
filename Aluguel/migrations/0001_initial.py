# Generated by Django 3.1.4 on 2020-12-15 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imovel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=200)),
                ('endereco', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=11)),
                ('rg', models.CharField(max_length=10)),
                ('telefone', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Aluguel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apartamento', models.CharField(max_length=200)),
                ('valor_aluguel', models.CharField(max_length=10)),
                ('valor_multa', models.CharField(max_length=10)),
                ('valor_agua', models.CharField(max_length=10)),
                ('valor_luz', models.CharField(max_length=10)),
                ('imovel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aluguel.imovel')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aluguel.pessoa')),
            ],
        ),
    ]
