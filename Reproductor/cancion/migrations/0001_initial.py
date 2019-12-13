# Generated by Django 2.2.7 on 2019-12-13 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cancion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('track_file', models.FileField(upload_to='Cancion')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='album.Album')),
            ],
            options={
                'db_table': 'cancion',
            },
        ),
    ]
