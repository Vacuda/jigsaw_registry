# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-24 20:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('log_and_reg_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('belongs_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brands', to='log_and_reg_app.User')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('belongs_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='log_and_reg_app.User')),
            ],
        ),
        migrations.CreateModel(
            name='Puzzle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('desc', models.TextField(blank=True, max_length=100)),
                ('pieces_labeled', models.PositiveSmallIntegerField()),
                ('pieces_actual', models.PositiveSmallIntegerField()),
                ('width', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('height', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('missing_pieces', models.PositiveSmallIntegerField(default=0)),
                ('notes', models.TextField(blank=True, max_length=100)),
                ('owned', models.BooleanField(default=True)),
                ('completed', models.BooleanField(default=False)),
                ('completions', models.PositiveSmallIntegerField(default=0)),
                ('initial_complete', models.DateTimeField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('belongs_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='puzzles', to='log_and_reg_app.User')),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='puzzles', to='puzzle_app.Brand')),
                ('categories', models.ManyToManyField(related_name='puzzles', to='puzzle_app.Category')),
            ],
        ),
        migrations.CreateModel(
            name='PuzzleImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='puzzle_images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='puzzle',
            name='picture',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='puzzle', to='puzzle_app.PuzzleImage'),
        ),
    ]
