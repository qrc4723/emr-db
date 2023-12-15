# Generated by Django 4.2.8 on 2023-12-06 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patman', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('admin_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('admin_name', models.CharField(max_length=10)),
                ('admin_pw', models.CharField(max_length=100)),
                ('admin_tel', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'admin',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Calender',
            fields=[
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='patman.patient')),
                ('treatment_plan', models.CharField(blank=True, max_length=255, null=True)),
                ('plan_date', models.DateTimeField()),
                ('plan_diet', models.CharField(blank=True, max_length=255, null=True)),
                ('plan_more_detail', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'calender',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('diag_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('doctor_id', models.CharField(blank=True, max_length=50, null=True)),
                ('diseases', models.CharField(blank=True, max_length=100, null=True)),
                ('main_pain', models.CharField(blank=True, max_length=255, null=True)),
                ('d_of_diseases', models.CharField(blank=True, max_length=100, null=True)),
                ('therapy_select', models.IntegerField(blank=True, null=True)),
                ('field', models.CharField(blank=True, max_length=100, null=True)),
                ('diseases_time', models.CharField(blank=True, max_length=17, null=True)),
            ],
            options={
                'db_table': 'diagnosis',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ExcerTherapy',
            fields=[
                ('treatment_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('reh_goal', models.CharField(max_length=255)),
                ('reh_therapy_date', models.CharField(max_length=17)),
                ('use_drug', models.CharField(max_length=255)),
                ('therapy_plan', models.CharField(max_length=255)),
                ('therapy_point', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'excer_therapy',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Hospitalization',
            fields=[
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='patman.patient')),
                ('patient_date', models.CharField(max_length=17)),
                ('hospital_room_id', models.CharField(max_length=50)),
                ('hospital_room_info', models.CharField(blank=True, max_length=100, null=True)),
                ('hospital_bed_id', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'hospitalization',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PersonTherapy',
            fields=[
                ('treatment_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('reh_goal', models.CharField(max_length=255)),
                ('reh_therapy_date', models.CharField(max_length=17)),
                ('use_drug', models.CharField(max_length=255)),
                ('therapy_plan', models.CharField(max_length=255)),
                ('therapy_point', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'person_therapy',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('record_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('medical_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'record',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('res_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('res_type', models.CharField(max_length=100)),
                ('res_time', models.DateTimeField()),
                ('pick_up', models.IntegerField()),
                ('pick_place', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'reservation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Therapist',
            fields=[
                ('therapist_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('therapist_salery', models.IntegerField()),
                ('therapist_nm', models.CharField(max_length=10)),
                ('therapist_tel', models.CharField(max_length=20)),
                ('therapist_gender', models.CharField(max_length=10)),
                ('therapist_m_work', models.CharField(max_length=40)),
                ('therapist_pw', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'therapist',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cardiopulmonary',
            fields=[
                ('treatment', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='patman.excertherapy')),
                ('cardi_health', models.CharField(max_length=50)),
                ('cardi_trial', models.IntegerField()),
                ('cardi_value', models.IntegerField()),
                ('cardi_zvalue', models.IntegerField()),
                ('cardi_number', models.IntegerField()),
                ('cardi_media', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'cardiopulmonary',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DailyLife',
            fields=[
                ('treatment', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='patman.persontherapy')),
                ('daily_wash', models.CharField(blank=True, max_length=50, null=True)),
                ('daily_eat', models.CharField(blank=True, max_length=50, null=True)),
                ('daily_clothes', models.CharField(blank=True, max_length=50, null=True)),
                ('daily_toilet', models.CharField(blank=True, max_length=50, null=True)),
                ('daily_move', models.CharField(blank=True, max_length=50, null=True)),
                ('daily_yn', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'daily_life',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Flexibility',
            fields=[
                ('treatment', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='patman.excertherapy')),
                ('flex_health', models.CharField(max_length=50)),
                ('flex_trial', models.IntegerField()),
                ('flex_value', models.IntegerField()),
                ('flex_zvalue', models.IntegerField()),
                ('flex_number', models.IntegerField()),
                ('flex_media', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'flexibility',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Muscular',
            fields=[
                ('treatment', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='patman.excertherapy')),
                ('mus_health', models.CharField(max_length=50)),
                ('mus_trial', models.IntegerField()),
                ('mus_value', models.IntegerField()),
                ('mus_zvalue', models.IntegerField()),
                ('mus_number', models.IntegerField()),
                ('mus_media', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'muscular',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Perception',
            fields=[
                ('treatment', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='patman.persontherapy')),
                ('percep_see', models.CharField(blank=True, max_length=50, null=True)),
                ('percep_body', models.CharField(blank=True, max_length=50, null=True)),
                ('percep_con', models.CharField(blank=True, max_length=50, null=True)),
                ('percep_re', models.CharField(blank=True, max_length=50, null=True)),
                ('percep_jud', models.CharField(blank=True, max_length=50, null=True)),
                ('percep_solve', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'perception',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Physical',
            fields=[
                ('treatment', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='patman.persontherapy')),
                ('phy_range', models.CharField(blank=True, max_length=50, null=True)),
                ('phy_strong', models.IntegerField(blank=True, null=True)),
                ('phy_ability', models.CharField(blank=True, max_length=50, null=True)),
                ('phy_degree', models.IntegerField(blank=True, null=True)),
                ('phy_hand', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'physical',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Quickness',
            fields=[
                ('treatment', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='patman.excertherapy')),
                ('quick_health', models.CharField(max_length=50)),
                ('quick_trial', models.IntegerField()),
                ('quick_value', models.IntegerField()),
                ('quick_zvalue', models.IntegerField()),
                ('quick_number', models.IntegerField()),
                ('quick_media', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'quickness',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sense',
            fields=[
                ('treatment', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='patman.persontherapy')),
                ('sense_touch', models.IntegerField(blank=True, null=True)),
                ('sense_ache', models.IntegerField(blank=True, null=True)),
                ('sense_loc', models.IntegerField(blank=True, null=True)),
                ('sense_origin', models.IntegerField(blank=True, null=True)),
                ('sense_see', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sense',
                'managed': False,
            },
        ),
    ]
