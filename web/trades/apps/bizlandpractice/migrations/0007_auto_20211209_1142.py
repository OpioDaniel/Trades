# Generated by Django 2.1.10 on 2021-12-09 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bizlandpractice', '0006_auto_20211209_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutFL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon_name', models.CharField(max_length=20, null=True)),
                ('title', models.CharField(max_length=30, null=True)),
                ('description', models.CharField(max_length=500, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='abfl', to='bizlandpractice.BizlandMainWeb')),
            ],
        ),
        migrations.AlterField(
            model_name='featuredservices',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fs', to='bizlandpractice.BizlandMainWeb'),
        ),
    ]
