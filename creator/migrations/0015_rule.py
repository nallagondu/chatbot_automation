# Generated by Django 3.2 on 2021-07-06 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('creator', '0014_remove_responses_response'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='creator.responses')),
                ('chatbot', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Chatbot_rule', to='creator.chatbot')),
                ('intent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='creator.intent')),
            ],
        ),
    ]
