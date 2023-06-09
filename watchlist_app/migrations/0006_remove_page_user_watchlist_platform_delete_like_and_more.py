# Generated by Django 4.1.5 on 2023-04-20 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0005_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='user',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='platform',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='watchlist', to='watchlist_app.streamplatform'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Like',
        ),
        migrations.DeleteModel(
            name='Page',
        ),
    ]
