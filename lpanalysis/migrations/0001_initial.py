# Generated by Django 4.1.2 on 2023-10-19 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AttentionData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attention_position', models.IntegerField(default=0)),
                ('stay_time', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ClickData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('click_position_x', models.IntegerField(default=0)),
                ('click_position_y', models.IntegerField(default=0)),
                ('click_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ScrollData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_scroll_position', models.IntegerField(default=0)),
                ('max_scroll_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Url_Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('web_site', models.URLField()),
                ('screenshot', models.ImageField(upload_to='screenshots/')),
            ],
        ),
    ]
