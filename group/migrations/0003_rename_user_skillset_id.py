<<<<<<< HEAD
# Generated by Django 4.2.16 on 2024-09-20 19:13
=======
# Generated by Django 4.2.16 on 2024-09-20 19:06
>>>>>>> bc1b342eed4a9af3017bc2801dda710b66885507

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0002_rename_id_skillset_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skillset',
            old_name='user',
            new_name='id',
        ),
    ]
