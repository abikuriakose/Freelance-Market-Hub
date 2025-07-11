# Generated by Django 5.1.5 on 2025-02-13 10:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0007_tbl_rating'),
        ('Guest', '0005_tbl_client_client_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_chat',
            name='client_from',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_from', to='Guest.tbl_client'),
        ),
        migrations.AlterField(
            model_name='tbl_chat',
            name='client_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_to', to='Guest.tbl_client'),
        ),
        migrations.AlterField(
            model_name='tbl_chat',
            name='freelancer_from',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='freelancer_from', to='Guest.tbl_freelancer'),
        ),
        migrations.AlterField(
            model_name='tbl_chat',
            name='freelancer_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='freelancer_to', to='Guest.tbl_freelancer'),
        ),
    ]
