# Generated by Django 3.1.7 on 2021-04-11 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210410_1622'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentquestion',
            old_name='comment_question',
            new_name='detail',
        ),
    ]
