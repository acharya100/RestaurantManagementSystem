from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_initial'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            DO $$
            BEGIN
                IF EXISTS (
                    SELECT 1
                    FROM information_schema.columns
                    WHERE table_name = 'restaurants_restaurant'
                      AND column_name = 'is_open'
                )
                AND NOT EXISTS (
                    SELECT 1
                    FROM information_schema.columns
                    WHERE table_name = 'restaurants_restaurant'
                      AND column_name = 'is_opened'
                ) THEN
                    ALTER TABLE restaurants_restaurant RENAME COLUMN is_open TO is_opened;
                END IF;
            END
            $$;
            """,
            reverse_sql="""
            DO $$
            BEGIN
                IF EXISTS (
                    SELECT 1
                    FROM information_schema.columns
                    WHERE table_name = 'restaurants_restaurant'
                      AND column_name = 'is_opened'
                )
                AND NOT EXISTS (
                    SELECT 1
                    FROM information_schema.columns
                    WHERE table_name = 'restaurants_restaurant'
                      AND column_name = 'is_open'
                ) THEN
                    ALTER TABLE restaurants_restaurant RENAME COLUMN is_opened TO is_open;
                END IF;
            END
            $$;
            """,
        ),
    ]
