# Generated by Django 3.1.7 on 2021-03-26 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('rank', models.IntegerField()),
                ('image', models.ImageField(upload_to='media')),
                ('description', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('passive', 'passive')], max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='media')),
                ('status', models.CharField(choices=[('active', 'active'), ('passive', 'passive')], max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('image', models.CharField(max_length=300)),
                ('slug', models.CharField(max_length=300, unique=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('passive', 'passive')], max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='media')),
                ('description', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('passive', 'passive')], max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('price', models.IntegerField()),
                ('discounted_price', models.IntegerField(default=0)),
                ('label', models.CharField(choices=[('new', 'new'), ('hot', 'hot'), ('sale', 'sale'), ('', 'default')], max_length=200)),
                ('image', models.ImageField(upload_to='media')),
                ('status', models.CharField(choices=[('active', 'active'), ('passive', 'passive')], max_length=300)),
                ('slug', models.CharField(max_length=200, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
        ),
    ]
