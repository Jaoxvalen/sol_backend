# Generated by Django 3.0.3 on 2020-10-11 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('peso', models.IntegerField()),
                ('talla', models.DecimalField(decimal_places=2, max_digits=4)),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
    ]