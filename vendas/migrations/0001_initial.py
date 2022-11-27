# Generated by Django 3.2.9 on 2022-11-25 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valorVenda', models.DecimalField(decimal_places=2, max_digits=8)),
                ('quantidadeVenda', models.IntegerField()),
                ('dataVenda', models.DateField()),
            ],
        ),
    ]
