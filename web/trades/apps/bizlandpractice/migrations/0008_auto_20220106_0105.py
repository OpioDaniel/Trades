# Generated by Django 2.1.10 on 2022-01-05 22:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bizlandpractice', '0007_auto_20211209_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutfl',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='abfl', to='bizlandpractice.BizlandMainWeb'),
        ),
        migrations.AlterField(
            model_name='featuredservices',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fs', to='bizlandpractice.BizlandMainWeb'),
        ),
    ]
