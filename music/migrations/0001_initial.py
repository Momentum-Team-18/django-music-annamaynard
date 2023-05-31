# Generated by Django 4.2.1 on 2023-05-31 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('genre', models.CharField(blank=True, max_length=30, null=True)),
                ('image', models.ImageField(upload_to='media/images/')),
            ],
        ),
        migrations.CreateModel(
            name='AlbumArt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'artists',
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('preview', models.CharField(max_length=5000)),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='music.album')),
                ('band', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='music.artist')),
            ],
        ),
    ]
