# Generated by Django 4.1.1 on 2022-09-16 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('vessel', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Fish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commonName', models.CharField(max_length=100)),
                ('sciName', models.CharField(max_length=100)),
                ('habitat', models.TextField(max_length=250)),
                ('quantity', models.IntegerField()),
                ('collectors', models.ManyToManyField(to='main_app.collector')),
            ],
        ),
        migrations.CreateModel(
            name='Surveys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('age', models.CharField(choices=[('L', 'Larval'), ('J', 'Juvenile'), ('S', 'Subadult'), ('A', 'Adult')], default='A', max_length=1)),
                ('fish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.fish')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
