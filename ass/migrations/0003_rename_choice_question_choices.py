# Generated by Django 3.2 on 2022-04-25 00:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ass', '0002_alter_question_assignment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='choice',
            new_name='choices',
        ),
    ]
