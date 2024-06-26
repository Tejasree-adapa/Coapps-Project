from django.db import migrations

def create_data(apps, schema_editor):
    Customer = apps.get_model('customers', 'Customer')
    Customer(first_name="Customer 001", last_name="Customer 001", email="customer@email.com", phone="000999000", address="Customer 000 address", description="Customer 000 description").save()

class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_data),
    ]
