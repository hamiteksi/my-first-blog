# Generated by Django 2.2.2 on 2019-07-14 18:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Baslik')),
                ('content', models.TextField(verbose_name='Icerik')),
                ('crt_date', models.DateTimeField(verbose_name='Olusturma Tarihi')),
                ('pub_date', models.DateTimeField(blank=True, null=True, verbose_name='Yayim Tarihi')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Yazar')),
            ],
        ),
    ]
