# Generated by Django 5.1.4 on 2024-12-07 03:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='store.basemodel')),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=20)),
                ('payment_method', models.CharField(choices=[('COD', 'COD'), ('ONLINE', 'ONLINE')], default='COD', max_length=15)),
                ('is_paid', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
            bases=('store.basemodel',),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='store.basemodel')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('price', models.FloatField()),
                ('order_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderitems', to='store.order')),
                ('product_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
            bases=('store.basemodel',),
        ),
    ]
