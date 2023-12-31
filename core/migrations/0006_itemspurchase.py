# Generated by Django 4.2.3 on 2023-07-19 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_purchase'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemsPurchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantify', models.IntegerField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='core.book')),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Items', to='core.purchase')),
            ],
        ),
    ]
