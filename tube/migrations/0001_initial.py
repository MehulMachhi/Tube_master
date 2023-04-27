# Generated by Django 4.1.1 on 2022-09-20 04:45

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BDD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BDD_SN', models.CharField(blank=True, max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='BDD_tube_seal_rack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(blank=True, max_length=128)),
                ('qty_rack', models.CharField(blank=True, max_length=128)),
                ('tube_seal_rack', models.CharField(blank=True, max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Calibration_orifice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(blank=True, max_length=128)),
                ('total_sets', models.CharField(blank=True, max_length=128)),
                ('in_sets', models.CharField(blank=True, max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='CALIBRATION_STAND',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cal_stand_size', models.CharField(blank=True, max_length=128)),
                ('calibration_orifice_set', models.ManyToManyField(to='tube.calibration_orifice')),
            ],
        ),
        migrations.CreateModel(
            name='Catalyst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catalyst_name', models.CharField(blank=True, max_length=128)),
                ('model_number', models.CharField(blank=True, max_length=128)),
                ('manufacturer', models.CharField(blank=True, max_length=128)),
                ('shape', models.CharField(choices=[('TQ', 'TQ'), ('TABLET', 'TABLET'), ('EXTRADIET', 'EXTRADIET'), ('CYLINDER', 'CYLINDER'), ('PENTERING_CYLINDER', 'PENTERING_CYLINDER'), ('SPHERE', 'SPHERE'), ('OTHER', 'OTHER')], default='TQ', max_length=20)),
                ('length', models.CharField(blank=True, max_length=128)),
                ('width', models.CharField(blank=True, max_length=128)),
                ('height', models.CharField(blank=True, max_length=128)),
                ('inner_diameter', models.CharField(blank=True, max_length=128)),
                ('outer_diameter', models.CharField(blank=True, max_length=128)),
                ('crush_strength', models.CharField(blank=True, max_length=128)),
                ('MSDS', models.FileField(blank=True, null=True, upload_to='MSDS_files/')),
            ],
        ),
        migrations.CreateModel(
            name='Loading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catalyst_to_be_loaded', models.CharField(blank=True, max_length=128)),
                ('layers_of_catalyst', models.CharField(blank=True, max_length=128)),
                ('layers_of_inerts', models.CharField(blank=True, max_length=128)),
                ('tube_loading_profile_drawing', models.FileField(blank=True, null=True, upload_to='tube_loading_profile_drawings/', verbose_name='Tube Loading Profile Drawings')),
                ('loaded_tube_length_in', models.CharField(blank=True, max_length=128)),
                ('loaded_tube_length_mm', models.CharField(blank=True, max_length=128)),
                ('tube_bottom_retainer', models.CharField(choices=[('SPRING', 'SPRING'), ('WIREMESH', 'WIREMESH'), ('OTHER', 'OTHER')], default='SPRING', max_length=20)),
                ('top_spring', models.BooleanField(blank=True, choices=[(True, 'yes'), (False, 'No')], default='True', verbose_name='top_spring')),
                ('spring_height', models.CharField(blank=True, max_length=128)),
                ('spring_drawing', models.FileField(blank=True, null=True, upload_to='spring_drawing/')),
            ],
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_name', models.CharField(blank=True, max_length=128)),
                ('part_no', models.CharField(blank=True, max_length=128)),
                ('part_function', models.CharField(blank=True, max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Pressure_senser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('range', models.CharField(blank=True, max_length=128)),
                ('quantity', models.CharField(blank=True, max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Supply_orifice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(blank=True, max_length=128)),
                ('total_sets', models.CharField(blank=True, max_length=128)),
                ('orifice_in_each_set', models.CharField(blank=True, max_length=128)),
                ('storage_case', models.CharField(blank=True, max_length=128)),
                ('notes', models.CharField(blank=True, max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='TTD_tube_seal_rack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(blank=True, max_length=128)),
                ('qty_rack', models.CharField(blank=True, max_length=128)),
                ('tube_seal_rack', models.CharField(blank=True, max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warehouse_name', models.CharField(blank=True, max_length=128)),
                ('warehouse_location', models.CharField(blank=True, max_length=128)),
                ('warehouse_contact', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('warehouse_email', models.EmailField(blank=True, max_length=128)),
                ('warehouse_manager', models.CharField(blank=True, max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='TTD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TTD_SN', models.CharField(blank=True, max_length=128)),
                ('TTD_tube_seal_rack', models.ManyToManyField(to='tube.ttd_tube_seal_rack')),
                ('pressure_senser', models.ManyToManyField(to='tube.pressure_senser')),
                ('supply_orifice_set', models.ManyToManyField(to='tube.supply_orifice')),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment_name', models.CharField(choices=[('TTD', 'TTD'), ('BDD', 'BDD'), ('CALIBRATIONSTAND', 'CALIBRATIONSTAND')], default='TTD', max_length=20)),
                ('abbreviation', models.CharField(blank=True, max_length=128)),
                ('alternate_name', models.CharField(blank=True, max_length=128)),
                ('serial_number', models.CharField(blank=True, max_length=128)),
                ('asset_number', models.CharField(blank=True, max_length=128)),
                ('pm_status', models.CharField(choices=[('RED', 'RED'), ('BLUE', 'BLUE'), ('GREEN', 'GREEN')], default='RED', max_length=20)),
                ('location_for_storage', models.CharField(blank=True, max_length=128)),
                ('packaging', models.CharField(blank=True, max_length=128)),
                ('is_this_part_of_set', models.CharField(blank=True, max_length=128)),
                ('if_yes_how_many_in_a_set', models.CharField(blank=True, max_length=128)),
                ('is_it_an_assembly', models.CharField(blank=True, max_length=128)),
                ('allow_to_add_sub_parts', models.CharField(blank=True, max_length=128)),
                ('bdd', models.ManyToManyField(blank=True, to='tube.bdd')),
                ('calibration_stand', models.ManyToManyField(blank=True, to='tube.calibration_stand')),
                ('ttd', models.ManyToManyField(blank=True, related_name='ttd', to='tube.ttd')),
            ],
        ),
        migrations.AddField(
            model_name='bdd',
            name='BDD_tube_seal_rack',
            field=models.ManyToManyField(to='tube.bdd_tube_seal_rack'),
        ),
    ]