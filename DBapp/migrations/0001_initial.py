# Generated by Django 5.1.4 on 2024-12-23 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empno', models.IntegerField()),
                ('empname', models.CharField(max_length=20)),
                ('salary', models.IntegerField()),
            ],
        ),
    ]
