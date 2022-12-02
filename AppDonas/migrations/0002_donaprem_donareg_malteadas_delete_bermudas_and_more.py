# Generated by Django 4.1.3 on 2022-12-01 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppDonas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donaprem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sabor', models.CharField(max_length=30)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Donareg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sabor', models.CharField(max_length=30)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Malteadas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sabor', models.CharField(max_length=20)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Bermudas',
        ),
        migrations.DeleteModel(
            name='Kimonos',
        ),
        migrations.DeleteModel(
            name='Rashguards',
        ),
    ]