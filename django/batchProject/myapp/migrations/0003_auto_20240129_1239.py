# Generated by Django 3.0.5 on 2024-01-29 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_usersignup_user_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotesClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('myfile', models.FileField(upload_to='User_Notes')),
                ('discription', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='user_register',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
