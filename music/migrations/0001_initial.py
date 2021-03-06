# Generated by Django 2.1.5 on 2019-04-05 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('amount', models.IntegerField()),
                ('price', models.IntegerField(default=100)),
            ],
        ),
        migrations.CreateModel(
            name='webpage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100, unique='True')),
                ('name', models.CharField(max_length=100, unique='True')),
                ('url', models.URLField(max_length=100, unique='True')),
            ],
        ),
    ]
