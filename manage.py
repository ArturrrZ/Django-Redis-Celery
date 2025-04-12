#!/usr/bin/env python
import os
import sys
import time
import psycopg2

MAX_RETRIES = 10

# ✅ SET THIS EARLY!
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

def wait_for_db():
    retries = 0
    while retries < MAX_RETRIES:
        try:
            conn = psycopg2.connect(
                dbname=os.environ.get("POSTGRES_DB"),
                user=os.environ.get("POSTGRES_USER"),
                password=os.environ.get("POSTGRES_PASSWORD"),
                host=os.environ.get("POSTGRES_HOST", "db"),
                port=os.environ.get("POSTGRES_PORT", 5432),
            )
            conn.close()
            print("✅ Database is ready!")
            return
        except psycopg2.OperationalError:
            retries += 1
            wait = 2 * retries
            print(f"⏳ Waiting for database... (attempt {retries}/{MAX_RETRIES})")
            time.sleep(wait)
    print("❌ Database not ready after several retries. Exiting.")
    sys.exit(1)

if __name__ == "__main__":
    if os.environ.get("RUN_MAIN") != "true":
        wait_for_db()
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
