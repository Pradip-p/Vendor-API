# Generated by Django 3.1.7 on 2021-03-05 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provinces',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provinces_number', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_id', models.CharField(max_length=20)),
                ('vendor_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('telephone', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('fax_no', models.CharField(blank=True, max_length=100, null=True)),
                ('create_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('owner_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('type_of_business', models.CharField(max_length=100)),
                ('year_of_establishment', models.CharField(max_length=100)),
                ('vat_number', models.CharField(max_length=100)),
                ('pan_number', models.CharField(max_length=100)),
                ('service_tax_reg_number', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VendorBankDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_branch', models.CharField(max_length=200)),
                ('branch_address', models.CharField(max_length=200)),
                ('type_of_account', models.CharField(max_length=200)),
                ('bank_branch_ifsc_code', models.CharField(max_length=200)),
                ('bank_name', models.CharField(max_length=100)),
                ('account_holder_name', models.CharField(max_length=100)),
                ('vendor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='vendor.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='VenderContactPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_contact_person', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=100)),
                ('email_id', models.EmailField(blank=True, max_length=200, null=True)),
                ('vendor', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='vendor.vendor')),
            ],
        ),
    ]
