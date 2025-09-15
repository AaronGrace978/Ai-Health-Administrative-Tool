#!/usr/bin/env python3
"""
Check database status and tables
"""

import sqlite3
import os

def check_database():
    db_path = "health_admin.db"
    
    if not os.path.exists(db_path):
        print("❌ Database file 'health_admin.db' not found!")
        return False
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Check tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()
        
        print("✅ Database found!")
        print(f"📊 Tables in database: {[table[0] for table in tables]}")
        
        # Check if we have the new billing tables
        table_names = [table[0] for table in tables]
        billing_tables = ['bills', 'payments', 'payment_methods']
        
        missing_tables = [table for table in billing_tables if table not in table_names]
        if missing_tables:
            print(f"⚠️  Missing billing tables: {missing_tables}")
            print("   The billing tables need to be created.")
        else:
            print("✅ All billing tables present!")
        
        # Check patients table
        if 'patients' in table_names:
            cursor.execute("SELECT COUNT(*) FROM patients")
            patient_count = cursor.fetchone()[0]
            print(f"👥 Patients in database: {patient_count}")
            
            if patient_count == 0:
                print("⚠️  No patients found! This is why the GUI shows 'Failed to load patients'")
                print("   You need to create some patients first.")
        else:
            print("❌ Patients table not found!")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"❌ Error checking database: {e}")
        return False

if __name__ == "__main__":
    print("🔍 Checking Health Admin Database...")
    print("=" * 40)
    check_database()
