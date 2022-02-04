# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2022-01-25 17:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import otree.db.models
import otree_save_the_change.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='riskandfairness_espanol_group', to='otree.Session')),
            ],
            options={
                'db_table': 'RiskAndFairness_espanol_group',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_gbat_arrived', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('_gbat_grouped', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('mode', otree.db.models.StringField(max_length=10000, null=True)),
                ('partner_a', otree.db.models.FloatField(null=True)),
                ('partner_b', otree.db.models.FloatField(null=True)),
                ('me_a', otree.db.models.FloatField(null=True)),
                ('me_b', otree.db.models.FloatField(null=True)),
                ('prob_a', otree.db.models.FloatField(null=True)),
                ('prob_b', otree.db.models.FloatField(null=True)),
                ('outcome', otree.db.models.StringField(max_length=10000, null=True)),
                ('cq_failed_attempts', otree.db.models.IntegerField(null=True)),
                ('cq_a1', otree.db.models.LongStringField(null=True)),
                ('cq_a2', otree.db.models.LongStringField(null=True)),
                ('time_InitialInstructions', otree.db.models.LongStringField(null=True)),
                ('time_TaskInstructions', otree.db.models.LongStringField(null=True)),
                ('time_ControlQuestions', otree.db.models.LongStringField(null=True)),
                ('time_Graph', otree.db.models.LongStringField(null=True)),
                ('time_Results', otree.db.models.LongStringField(null=True)),
                ('m', otree.db.models.FloatField(null=True)),
                ('px', otree.db.models.FloatField(null=True)),
                ('py', otree.db.models.FloatField(null=True)),
                ('a', otree.db.models.FloatField(null=True)),
                ('b', otree.db.models.FloatField(null=True)),
                ('ax', otree.db.models.FloatField(null=True)),
                ('ay', otree.db.models.FloatField(null=True)),
                ('bx', otree.db.models.FloatField(null=True)),
                ('by', otree.db.models.FloatField(null=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='RiskAndFairness_espanol.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='riskandfairness_espanol_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='riskandfairness_espanol_player', to='otree.Session')),
            ],
            options={
                'db_table': 'RiskAndFairness_espanol_player',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='riskandfairness_espanol_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'RiskAndFairness_espanol_subsession',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.AddField(
            model_name='player',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RiskAndFairness_espanol.Subsession'),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RiskAndFairness_espanol.Subsession'),
        ),
    ]
