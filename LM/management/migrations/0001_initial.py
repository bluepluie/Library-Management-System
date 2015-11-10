# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('price', models.FloatField()),
                ('author', models.CharField(max_length=128)),
                ('pubDate', models.DateField()),
                ('typ', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='BookEval',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rate', models.CharField(default=b'ex', max_length=2, choices=[(b'ex', b'Excellent'), (b'go', b'Good'), (b'av', b'Average'), (b'fa', b'Fair'), (b'po', b'Poor')])),
                ('book', models.ForeignKey(to='management.Book')),
            ],
        ),
        migrations.CreateModel(
            name='BookT',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('avail', models.BooleanField(default=True)),
                ('desc', models.CharField(max_length=1000)),
                ('isbn', models.CharField(max_length=200)),
                ('borrowPeriod', models.DurationField()),
                ('publisher', models.CharField(max_length=128, blank=True)),
                ('book', models.ForeignKey(to='management.Book')),
            ],
        ),
        migrations.CreateModel(
            name='BorrowInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('BorrowDate', models.DateField()),
                ('ReturnDate', models.DateField(default=None)),
                ('book', models.ForeignKey(to='management.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('desc', models.TextField()),
                ('img', models.ImageField(upload_to=b'image')),
                ('book', models.ForeignKey(to='management.Book')),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nickname', models.CharField(max_length=16)),
                ('permission', models.IntegerField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('resDate', models.DateField()),
                ('book', models.ForeignKey(to='management.Book')),
                ('user', models.ForeignKey(to='management.MyUser')),
            ],
        ),
        migrations.AddField(
            model_name='borrowinfo',
            name='user',
            field=models.ForeignKey(to='management.MyUser'),
        ),
        migrations.AddField(
            model_name='bookeval',
            name='user',
            field=models.ForeignKey(to='management.MyUser'),
        ),
    ]
