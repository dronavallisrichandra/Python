# Generated by Django 3.2.18 on 2023-11-18 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_jobpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.CharField(max_length=50)),
                ('education', models.CharField(max_length=50)),
                ('job_role', models.CharField(max_length=50)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.jobuser')),
            ],
        ),
    ]