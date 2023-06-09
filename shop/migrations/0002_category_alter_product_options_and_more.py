# Generated by Django 4.2.1 on 2023-05-21 20:58

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название категории', max_length=70, unique=True, verbose_name='Название категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['id'],
            },
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-date'], 'verbose_name': 'Тоавр', 'verbose_name_plural': 'Товары'},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='cast',
        ),
        migrations.RemoveField(
            model_name='product',
            name='country',
        ),
        migrations.RemoveField(
            model_name='product',
            name='director',
        ),
        migrations.RemoveField(
            model_name='product',
            name='play',
        ),
        migrations.RemoveField(
            model_name='product',
            name='section',
        ),
        migrations.RemoveField(
            model_name='product',
            name='year',
        ),
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(50), django.core.validators.MaxValueValidator(10000)]),
        ),
        migrations.AlterField(
            model_name='order',
            name='discount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.discount', verbose_name='Скидка'),
        ),
        migrations.DeleteModel(
            name='Section',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.category', verbose_name='Категория'),
        ),
    ]
