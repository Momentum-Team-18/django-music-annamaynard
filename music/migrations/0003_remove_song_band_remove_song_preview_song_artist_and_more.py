# Generated by Django 4.2.1 on 2023-05-31 01:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_delete_albumart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='band',
        ),
        migrations.RemoveField(
            model_name='song',
            name='preview',
        ),
        migrations.AddField(
            model_name='song',
            name='artist',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='music.artist'),
        ),
        migrations.AddField(
            model_name='song',
            name='song',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='music.album'),
        ),
    ]