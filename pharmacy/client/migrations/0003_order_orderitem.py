# Generated by Django 4.2.7 on 2023-12-07 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacist', '0001_initial'),
        ('client', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('total_price', models.PositiveIntegerField(default=0)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('PROCESSING', 'Processing'), ('SHIPPED', 'Shipped'), ('DELIVERED', 'Delivered')], default='PENDING', max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='client.client')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('medicine', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_items', to='pharmacist.medicine')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='client.order')),
            ],
        ),
    ]
