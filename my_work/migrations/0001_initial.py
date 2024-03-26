# Generated by Django 5.0 on 2024-03-06 07:54

import django.db.models.deletion
import my_work.manager
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('full_name', models.CharField(max_length=60)),
                ('phone', models.CharField(max_length=13, unique=True)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('address', models.TextField()),
                ('user_type', models.CharField(choices=[('admin', 'Admin'), ('customer', 'customer'), ('driver', 'driver')], default='customer', max_length=20)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', my_work.manager.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='GarbageBin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.PositiveBigIntegerField()),
                ('assigned', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CollectionRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('filled', 'filled'), ('half', 'half')], default='filled', max_length=20)),
                ('request_status', models.CharField(choices=[('pending', 'pending'), ('approved', 'approved')], default='pending', max_length=20)),
                ('driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CollectionStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_status', models.CharField(choices=[('collected', 'collected'), ('not_collected', 'not collected'), ('on_the_way', 'on the way')], default='not_collected', max_length=20)),
                ('collectonrequest', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='my_work.collectionrequest')),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserGarbageBin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bin', models.ManyToManyField(to='my_work.garbagebin')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='collectionrequest',
            name='garbage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='my_work.usergarbagebin'),
        ),
    ]