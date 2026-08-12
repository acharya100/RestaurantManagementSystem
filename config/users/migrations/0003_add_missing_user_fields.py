from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_bio'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            DO $$
            BEGIN
                IF NOT EXISTS (
                    SELECT 1
                    FROM information_schema.columns
                    WHERE table_name = 'users_user'
                      AND column_name = 'date_of_birth'
                ) THEN
                    ALTER TABLE users_user ADD COLUMN date_of_birth date;
                END IF;
            END
            $$;
            """,
            reverse_sql="""SELECT 1;""",
        ),
        migrations.RunSQL(
            sql="""
            DO $$
            BEGIN
                IF NOT EXISTS (
                    SELECT 1
                    FROM information_schema.columns
                    WHERE table_name = 'users_user'
                      AND column_name = 'bio'
                ) THEN
                    ALTER TABLE users_user ADD COLUMN bio text DEFAULT '';
                END IF;
            END
            $$;
            """,
            reverse_sql="""SELECT 1;""",
        ),
    ]
