# Generated by Django 4.1.7 on 2023-03-06 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolPlanners', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('description', models.TextField(default='')),
                ('start', models.DateTimeField(default='')),
                ('end', models.DateTimeField(default='')),
                ('location', models.CharField(default='School', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='subject',
            name='current_summary',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='subject',
            name='class_name',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='subject',
            name='teacher',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('description', models.TextField(default='')),
                ('due_date', models.DateTimeField(default='')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolPlanners.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('description', models.TextField(default='')),
                ('date', models.DateTimeField(default='')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolPlanners.subject')),
            ],
        ),
    ]