# Generated by Django 4.2.6 on 2023-10-16 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulas', '0003_alter_formulavalidator_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulavalidator',
            name='formula',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
