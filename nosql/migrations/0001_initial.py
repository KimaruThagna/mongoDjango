# Generated by Django 2.2.3 on 2020-03-15 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('views', models.IntegerField(default=0)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updatedOn', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]