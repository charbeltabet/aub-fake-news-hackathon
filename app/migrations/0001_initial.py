# Generated by Django 3.0.7 on 2020-07-05 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Threat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('description', models.CharField(max_length=140)),
                ('who', models.CharField(max_length=140)),
                ('what', models.CharField(max_length=140)),
                ('where', models.CharField(max_length=140)),
                ('when', models.CharField(max_length=140)),
                ('why', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Testimony',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.BooleanField(choices=[(True, 'Approve'), (False, 'Disapprove')])),
                ('comment', models.TextField(max_length=100)),
                ('threat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Threat')),
            ],
        ),
    ]
