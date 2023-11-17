# Generated by Django 4.2.4 on 2023-11-17 09:22

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the movie name', max_length=50)),
                ('description', models.TextField(help_text='Enter the movie description')),
                ('imdb_rating', models.FloatField(help_text='Enter the IMDb rating')),
                ('movie_duration', models.CharField(help_text='Enter the movie duration Ex: 2h 34min', max_length=20)),
                ('movie_year', models.IntegerField(help_text='Ex: 2024')),
                ('movie_trailler', models.CharField(help_text='Enter the youtube trailler video id Ex: aR_JzBGdGvM', max_length=200)),
                ('movie_match', models.CharField(help_text='Ex: 67% Match ,Enter only number', max_length=100)),
                ('movie_grade', models.CharField(help_text='Ex: U/A 18+', max_length=200)),
                ('poster_portrait', models.URLField(help_text='Enter the movie poster URL Ex: http://...', max_length=900)),
                ('director', models.CharField(help_text='Ex: Mark • David Hammer • Chris Green', max_length=200)),
                ('distibuted_by', models.CharField(help_text='Ex: Warner Bros. Entertainment • Marvel Studio', max_length=200)),
                ('cast', models.CharField(help_text='Ex: Chris hamesworth • Scarllet johnson', max_length=200)),
                ('language', models.CharField(help_text='Ex: English • Hindi', max_length=200)),
                ('subtitle', models.CharField(help_text='Ex: English • Hindi • Spanish', max_length=200)),
                ('quality', models.CharField(help_text='Ex: 720p • 1080p • 2160p 60fps', max_length=200)),
                ('screenshot_1', models.URLField(help_text='Enter the Screenshot 1 URL', max_length=900)),
                ('screenshot_2', models.URLField(help_text='Enter the Screenshot 2 URl', max_length=900)),
                ('screenshot_3', models.URLField(help_text='Enter the Screenshot 3 URL', max_length=900)),
                ('screenshot_4', models.URLField(help_text='Enter the Screenshot 4 URL', max_length=900)),
                ('screenshot_5', models.URLField(help_text='Enter the Screenshot 5 URL', max_length=900)),
                ('screenshot_6', models.URLField(help_text='Enter the Screenshot 6 URL', max_length=900)),
                ('update', models.CharField(default='No Updates', help_text='Ex: Episode 3 Added', max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='movie_title', unique=True)),
                ('movie_title', models.CharField(help_text='Ex: Loki full hd movie download', max_length=300)),
                ('released_at', models.DateField(blank=True, help_text=' Ex: 23/09/2021', null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ManyToManyField(related_name='categories', to='detail.categories')),
            ],
            options={
                'verbose_name_plural': 'Add movies',
            },
        ),
        migrations.CreateModel(
            name='trending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster_landscape', models.URLField(max_length=900)),
                ('movies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trending_movies', to='detail.movie')),
            ],
            options={
                'verbose_name_plural': 'Trending Silder',
            },
        ),
        migrations.CreateModel(
            name='poster3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_wallpaper', models.ImageField(upload_to='movie_media')),
                ('movies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poster3_movies', to='detail.movie')),
            ],
            options={
                'verbose_name_plural': 'Recommanded posters 3',
            },
        ),
        migrations.CreateModel(
            name='poster2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_wallpaper', models.ImageField(upload_to='movie_media')),
                ('movies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poster2_movies', to='detail.movie')),
            ],
            options={
                'verbose_name_plural': 'Recommanded posters 2',
            },
        ),
        migrations.CreateModel(
            name='poster1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_wallpaper', models.ImageField(upload_to='movie_media')),
                ('movies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poster1_movies', to='detail.movie')),
            ],
            options={
                'verbose_name_plural': 'Recommanded posters 1',
            },
        ),
        migrations.CreateModel(
            name='hot_thrills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=200)),
                ('name_color', models.CharField(default='grey', max_length=100)),
                ('clip', models.FileField(upload_to='movie_media')),
                ('movies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hot_thrills_movies', to='detail.movie')),
            ],
            options={
                'verbose_name_plural': 'Hot Slideshow',
            },
        ),
    ]
