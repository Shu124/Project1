# Generated by Django 3.2.5 on 2021-12-05 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('prod_id', models.AutoField(primary_key=True, serialize=False)),
                ('prod_name', models.CharField(max_length=50)),
                ('catagory', models.CharField(default='', max_length=50)),
                ('sub_catagory', models.CharField(default='', max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('desc', models.CharField(max_length=300)),
                ('pub_date', models.DateField()),
                ('image', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
    ]
