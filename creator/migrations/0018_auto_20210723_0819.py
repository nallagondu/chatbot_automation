# Generated by Django 3.2 on 2021-07-23 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('creator', '0017_auto_20210721_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='intent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='creator.intent'),
        ),
        migrations.AlterField(
            model_name='slot',
            name='form',
            field=models.ManyToManyField(blank=True, to='creator.Form'),
        ),
    ]
