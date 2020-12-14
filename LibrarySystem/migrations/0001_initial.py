# Generated by Django 3.1.2 on 2020-12-04 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=100)),
                ('publish_date', models.DateField()),
                ('description', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('remaining', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('cardID', models.CharField(max_length=100)),
                ('user_group', models.IntegerField()),
                ('account', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('major', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BorrowInfo',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('borrow_date', models.DateField()),
                ('return_date', models.DateField()),
                ('remark', models.CharField(max_length=100)),
                ('is_return', models.BooleanField()),
                ('bookID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LibrarySystem.book')),
                ('borrowerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LibrarySystem.user')),
            ],
        ),
    ]