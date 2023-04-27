# Generated by Django 3.2.16 on 2023-02-10 05:46

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0120_auto_20230210_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reactor',
            name='any_projections_on_tube_sheet_describe',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Any projections on tube sheet-describe'),
        ),
        migrations.AlterField(
            model_name='reactor',
            name='bottom_tube_sheet_thickness',
            field=models.CharField(blank=True, choices=[('INCH', 'INCH'), ('MM', 'MM')], max_length=128, null=True, verbose_name='Bottom Tube Sheet Thickness'),
        ),
        migrations.AlterField(
            model_name='reactor',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reactorclient+', to='client.client'),
        ),
        migrations.AlterField(
            model_name='reactor',
            name='ferrule_id',
            field=models.CharField(blank=True, choices=[('INCH', 'INCH'), ('MM', 'MM')], max_length=128, null=True, verbose_name='Ferrule ID'),
        ),
        migrations.AlterField(
            model_name='reactor',
            name='ferrule_length',
            field=models.CharField(blank=True, choices=[('INCH', 'INCH'), ('MM', 'MM')], max_length=128, null=True, verbose_name='Ferrule Length'),
        ),
        migrations.AlterField(
            model_name='reactor',
            name='input_bottomtube',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=999, null=True, verbose_name='INCH/MM'),
        ),
        migrations.AlterField(
            model_name='reactor',
            name='input_ferruleid',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=999, null=True, verbose_name='INCH/MM'),
        ),
        migrations.AlterField(
            model_name='reactor',
            name='input_ferrulelength',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=999, null=True, verbose_name='INCH/MM'),
        ),
        migrations.AlterField(
            model_name='reactor',
            name='input_toptube',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=999, null=True, verbose_name='INCH/MM'),
        ),
        migrations.AlterField(
            model_name='reactor',
            name='input_totaltube',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=999, null=True, verbose_name='INCH/MM'),
        ),
        migrations.AlterField(
            model_name='reactor',
            name='input_tubeid',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=999, null=True, verbose_name='INCH/MM'),
        ),
        migrations.AlterField(
            model_name='reactor',
            name='input_tubeprotude_bottom',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=999, null=True, verbose_name='INCH/MM'),
        ),
        migrations.AlterField(
            model_name='reactor',
            name='input_tubeprotude_top',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=999, null=True, verbose_name='INCH/MM'),
        ),
        migrations.AlterField(
            model_name='reactor',
            name='input_tubespacing',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=999, null=True, verbose_name='INCH/MM'),
        ),
        migrations.AlterField(
            model_name='reactor',
            name='is_there_ferrule_insert_in_tube',
            field=models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO')], max_length=128, null=True, verbose_name='Is There Ferrule Insert In Tube?'),
        ),
        migrations.AlterField(
            model_name='reactor',
            name='plant',
            field=smart_selects.db_fields.GroupedForeignKey(blank=True, group_field='client', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reactorplant+', to='client.plant'),
        ),
        migrations.AlterField(
            model_name='reactor',
            name='select_tube_protude_bottom',
            field=models.CharField(blank=True, choices=[('INCH', 'INCH'), ('MM', 'MM')], default='', max_length=128, null=True, verbose_name='Select INCH Or MM'),
        ),
        migrations.AlterField(
            model_name='reactor',
            name='select_tube_protude_top',
            field=models.CharField(blank=True, choices=[('INCH', 'INCH'), ('MM', 'MM')], default='', max_length=128, null=True, verbose_name='Select INCH Or MM'),
        ),
        migrations.AlterField(
            model_name='reactor',
            name='top_dome_removable',
            field=models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO')], max_length=128, null=True, verbose_name='Top Dom Removable'),
        ),
        migrations.AlterField(
            model_name='reactor',
            name='top_inlet_accessible',
            field=models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO')], max_length=128, null=True, verbose_name='Top Inlet Accessible'),
        ),
        migrations.AlterField(
            model_name='reactor',
            name='top_inlet_impingment_plate',
            field=models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO')], max_length=128, null=True, verbose_name='Top Inlet Impingment Plate'),
        ),
        migrations.AlterField(
            model_name='reactor',
            name='top_tube_sheet_thickness',
            field=models.CharField(blank=True, choices=[('INCH', 'INCH'), ('MM', 'MM')], max_length=128, null=True, verbose_name='Top Tube Sheet Thickness'),
        ),
        migrations.AlterField(
            model_name='reactor',
            name='total_tube_length',
            field=models.CharField(blank=True, choices=[('INCH', 'INCH'), ('MM', 'MM')], max_length=128, null=True, verbose_name='Total Tube Length'),
        ),
        migrations.AlterField(
            model_name='reactor',
            name='tube_id',
            field=models.CharField(blank=True, choices=[('INCH', 'INCH'), ('MM', 'MM')], max_length=128, null=True, verbose_name='Tube ID'),
        ),
        migrations.AlterField(
            model_name='reactor',
            name='tube_protude_out_of_bottom_tube_sheet',
            field=models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO')], max_length=128, null=True, verbose_name='Tube Protude Out Of Bottom Tube Sheet'),
        ),
        migrations.AlterField(
            model_name='reactor',
            name='tube_protude_out_of_top_tube_sheet',
            field=models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO')], max_length=128, null=True, verbose_name='Tube Protude Out Of Top Tube Sheet'),
        ),
        migrations.AlterField(
            model_name='reactor',
            name='tube_spacing_or_pitch',
            field=models.CharField(blank=True, choices=[('INCH', 'INCH'), ('MM', 'MM')], max_length=128, null=True, verbose_name='Tube Spacing Or Pitch'),
        ),
        migrations.AlterField(
            model_name='reactor',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reactorunit+', to='client.unit'),
        ),
    ]
