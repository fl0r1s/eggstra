# Generated by Django 3.2.5 on 2021-09-13 17:06

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
            name='EggsAvailable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gather_amount', models.IntegerField(verbose_name='Gather amount')),
                ('gather_notes', models.CharField(blank=True, max_length=256, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Egg_posts', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]