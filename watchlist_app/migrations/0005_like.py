# Generated by Django 4.1.5 on 2023-04-20 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0004_alter_page_page_publish_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='watchlist_app.page')),
                ('likes', models.IntegerField()),
            ],
            bases=('watchlist_app.page',),
        ),
    ]
