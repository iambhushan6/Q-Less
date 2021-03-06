# Generated by Django 3.2.4 on 2021-06-11 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('token', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=254)),
                ('gr_no', models.IntegerField()),
                ('branch', models.CharField(max_length=10)),
                ('year', models.CharField(max_length=12)),
                ('query', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
