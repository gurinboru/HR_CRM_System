# Generated by Django 4.1.3 on 2022-11-25 18:43

from django.db import migrations, models
import start.models


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0008_jobseek_denial_status_alter_job_definition_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='actionhistory',
            name='comment',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='position',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='candidate',
            name='photo',
            field=models.ImageField(upload_to=start.models.userPhoto_directory_path),
        ),
    ]