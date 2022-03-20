# Generated by Django 2.1.10 on 2021-08-30 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogCategorySections',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_id', models.CharField(max_length=50, null=True)),
                ('section_name', models.CharField(max_length=50, null=True)),
                ('section_description', models.CharField(max_length=1020, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CatalogCategorySectionsSub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_id', models.CharField(max_length=10, null=True)),
                ('data_date', models.CharField(max_length=15, null=True)),
                ('left', models.SmallIntegerField(default=0)),
                ('Image', models.ImageField(upload_to='catalogs/')),
                ('data_caption', models.CharField(max_length=50, null=True)),
                ('data_caption_link', models.CharField(max_length=50, null=True)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='catalog_category_sections_sub', to='fabhouse.CatalogCategorySections')),
            ],
        ),
        migrations.CreateModel(
            name='CatalogCategorySectionsSubTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, null=True)),
                ('sub_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections_sub_title', to='fabhouse.CatalogCategorySectionsSub')),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_name', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PageGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.SmallIntegerField(default=0)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page_gallery', to='fabhouse.Page')),
            ],
        ),
        migrations.CreateModel(
            name='PageInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=50, null=True)),
                ('value', models.CharField(max_length=1020, null=True)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page_infos', to='fabhouse.Page')),
            ],
        ),
        migrations.CreateModel(
            name='TitleImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_title', models.CharField(max_length=250, null=True)),
                ('Image', models.ImageField(upload_to='catalogs/title/')),
                ('sub_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_titles', to='fabhouse.CatalogCategorySectionsSubTitle')),
            ],
        ),
        migrations.AddField(
            model_name='catalogcategorysections',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='catalog_category_sections', to='fabhouse.Page'),
        ),
    ]
