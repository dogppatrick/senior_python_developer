# Generated by Django 3.2.10 on 2022-01-04 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='coffee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('bean_from', models.TextField()),
                ('price', models.FloatField()),
            ],
        ),
    ]
