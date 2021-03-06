# Generated by Django 3.2 on 2021-05-09 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(default='', max_length=50)),
                ('cartid', models.CharField(default='', max_length=50)),
                ('cartname', models.CharField(default='', max_length=20)),
                ('cartdecs', models.CharField(default='', max_length=50)),
                ('cartimage', models.ImageField(default='', upload_to='shop/cartimage')),
                ('cartprice', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('phone', models.CharField(default='', max_length=10)),
                ('desc', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loginid', models.CharField(default='', max_length=50)),
                ('loginname', models.CharField(default='', max_length=20)),
                ('password', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=20)),
                ('decs', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('ca', models.CharField(default='', max_length=50)),
                ('sca', models.CharField(default='', max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('image', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
    ]
