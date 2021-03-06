# Generated by Django 3.1.5 on 2021-11-30 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Careers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Jobtitle', models.CharField(max_length=300)),
                ('description', models.TextField(max_length=5000)),
                ('salary', models.IntegerField(default=0)),
                ('is_available', models.BooleanField(default=True)),
                ('contact', models.IntegerField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=3000)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField(default=91)),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=2000)),
                ('image', models.ImageField(upload_to='uploads/memberships')),
                ('price', models.IntegerField(default=2000)),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
    ]
