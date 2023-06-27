# Generated by Django 4.1.2 on 2023-06-27 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lpanalysis', '0006_rename_scroll_position_attentiondata_attention_position'),
    ]

    operations = [
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
            ],
        ),
    ]