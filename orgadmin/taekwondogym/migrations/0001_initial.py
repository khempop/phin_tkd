# Generated by Django 4.2.6 on 2023-10-15 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gym', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('level_name', models.CharField(max_length=200)),
                ('update_at', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gym', models.CharField(max_length=150)),
                ('course_name', models.CharField(max_length=150)),
                ('course_type', models.CharField(choices=[('SINGLE', 'SINGLE'), ('CONTINUE', 'CONTINUE')], max_length=50)),
                ('course_fee', models.IntegerField(blank=True, null=True)),
                ('open_course', models.DateField(blank=True, null=True)),
                ('close_course', models.DateField(blank=True, null=True)),
                ('update_at', models.DateTimeField(null=True)),
                ('classes', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='taekwondogym.classes', verbose_name='member level')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gym', models.CharField(max_length=150)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='images/contact')),
                ('name', models.CharField(max_length=150)),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
                ('parent_name', models.CharField(blank=True, max_length=150, null=True)),
                ('email_id', models.EmailField(max_length=150, unique=True)),
                ('phone', models.CharField(blank=True, max_length=13, null=True)),
                ('line_id', models.CharField(blank=True, max_length=150, null=True)),
                ('member_status', models.CharField(blank=True, choices=[('Active', 'Active'), ('Disabled', 'Disabled')], max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('join_at', models.DateTimeField(auto_now_add=True)),
                ('leave_at', models.DateTimeField()),
                ('point', models.IntegerField()),
                ('update_at', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gym', models.CharField(max_length=150)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='images/contact')),
                ('name', models.CharField(max_length=150)),
                ('address', models.CharField(blank=True, max_length=25, null=True)),
                ('email_id', models.EmailField(max_length=150, unique=True)),
                ('phone', models.CharField(blank=True, max_length=13, null=True)),
                ('line_id', models.CharField(blank=True, max_length=150, null=True)),
                ('member_status', models.CharField(blank=True, choices=[('Active', 'Active'), ('Disabled', 'Disabled')], max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('join_at', models.DateTimeField(auto_now_add=True)),
                ('leave_at', models.DateTimeField(blank=True, null=True)),
                ('update_at', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StaffAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gym', models.CharField(max_length=150)),
                ('active_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(null=True)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='taekwondogym.course', verbose_name='course')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taekwondogym.staff', verbose_name='staff')),
            ],
        ),
        migrations.CreateModel(
            name='Payroll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gym', models.CharField(max_length=150)),
                ('amount', models.FloatField(blank=True, null=True)),
                ('bonus', models.FloatField(blank=True, null=True)),
                ('pay', models.FloatField(blank=True, null=True)),
                ('hour_amount', models.FloatField(blank=True, null=True)),
                ('pay_at', models.DateTimeField(blank=True, null=True)),
                ('update_at', models.DateTimeField(null=True)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taekwondogym.staff', verbose_name='staff')),
            ],
        ),
        migrations.CreateModel(
            name='MemberAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gym', models.CharField(max_length=150)),
                ('active_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(null=True)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='taekwondogym.course', verbose_name='course')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taekwondogym.member', verbose_name='member')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('invoice_number', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('gym', models.CharField(max_length=150)),
                ('invoice_status', models.CharField(choices=[('PAID', 'PAID'), ('HOLD', 'HOLD'), ('FAILED', 'FAILED'), ('CANCEL', 'CANCEL')], max_length=50)),
                ('amount', models.FloatField(blank=True, null=True)),
                ('discount', models.FloatField(blank=True, null=True)),
                ('pay', models.FloatField(blank=True, null=True)),
                ('remark', models.TextField(blank=True, null=True)),
                ('payment_type', models.CharField(choices=[('ONLINE', 'ONLINE'), ('PROMPTPAY', 'PROMPTPAY'), ('CASH', 'CASH')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('pay_at', models.DateTimeField(blank=True, null=True)),
                ('update_at', models.DateTimeField(null=True)),
                ('courses', models.ManyToManyField(to='taekwondogym.course')),
                ('students', models.ManyToManyField(to='taekwondogym.member')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='taekwondogym.staff', verbose_name='staff'),
        ),
        migrations.AddField(
            model_name='classes',
            name='students',
            field=models.ManyToManyField(to='taekwondogym.member'),
        ),
    ]