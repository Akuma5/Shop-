# Generated by Django 4.1 on 2022-08-25 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MagazineImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Фото')),
                ('image_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photo', to='magazine.magazine', verbose_name='Ссылка на объект')),
            ],
        ),
    ]