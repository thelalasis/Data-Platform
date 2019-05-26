# Generated by Django 2.1.5 on 2019-01-24 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='accident',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, verbose_name='标题')),
                ('date', models.DateField()),
                ('content', models.TextField(verbose_name='正文')),
            ],
        ),
    ]