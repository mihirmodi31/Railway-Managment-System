# Generated by Django 3.1.5 on 2021-04-02 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0004_auto_20210402_1538'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pnr', models.CharField(max_length=15)),
                ('seat', models.IntegerField()),
            ],
        ),
    ]
