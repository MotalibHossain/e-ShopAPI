# Generated by Django 4.0.5 on 2022-07-24 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('category_img', models.ImageField(upload_to='shop/image/category/')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('category_img', models.ImageField(upload_to='shop/image/Subcategory/')),
                ('Subcatagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_store.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, null=True)),
                ('slug', models.SlugField(max_length=80, unique=True)),
                ('description', models.TextField()),
                ('Product_img', models.ImageField(upload_to='shop/images/Product/')),
                ('old_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('new_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('is_active', models.BooleanField(default=True)),
                ('is_stock', models.BooleanField(default=True)),
                ('published_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now_add=True)),
                ('catagory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Product_catagory', to='App_store.category')),
                ('sub_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App_store.subcategory')),
            ],
            options={
                'ordering': ['-published_date'],
            },
        ),
    ]
