# Generated by Django 2.2.7 on 2019-12-03 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PrimeMinister',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('bod', models.DateField()),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('imgurl', models.CharField(default='', max_length=500)),
                ('party', models.CharField(default='', max_length=500)),
            ],
        ),
    ]
