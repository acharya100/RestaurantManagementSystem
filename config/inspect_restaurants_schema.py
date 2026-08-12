import os
import django
from django.db import connection
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
print('=== SHOWMIGRATIONS ===')
call_command('showmigrations', 'restaurants')
print('=== COLUMNS ===')
with connection.cursor() as cursor:
    cursor.execute("SELECT column_name,data_type,is_nullable,column_default FROM information_schema.columns WHERE table_name='restaurants_restaurant' ORDER BY ordinal_position")
    for row in cursor.fetchall():
        print(row)
print('=== MIGRATIONS TABLE ===')
with connection.cursor() as cursor:
    cursor.execute("SELECT app,name,applied FROM django_migrations WHERE app='restaurants' ORDER BY name")
    for row in cursor.fetchall():
        print(row)
