import sqlite3

def clean_users():
    conn = sqlite3.connect('match_simulator.db')
    cursor = conn.cursor()
    
    try:
        # Delete all users except 'ggboi'
        cursor.execute("DELETE FROM users WHERE username != 'ggboi'")
        
        # Reset ggboi's data to default admin if it exists
        cursor.execute('''
            UPDATE users 
            SET role = 'admin', 
                status = 'active',
                cash = 1000000,
                email = 'ggboi@admin.com',
                club_name = 'Admin FC'
            WHERE username = 'ggboi'
        ''')
        
        # If ggboi doesn't exist, create it
        cursor.execute("SELECT COUNT(*) FROM users WHERE username = 'ggboi'")
        if cursor.fetchone()[0] == 0:
            from app import hash_password
            password_hash = hash_password('admin123')  # Default password
            cursor.execute('''
                INSERT INTO users (username, password_hash, role, status, email, club_name, cash)
                VALUES (?, ?, 'admin', 'active', 'ggboi@admin.com', 'Admin FC', 1000000)
            ''', ('ggboi', password_hash))
        
        conn.commit()
        print("Successfully cleaned up users. Only 'ggboi' admin remains.")
    except Exception as e:
        print(f"Error cleaning users: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    clean_users()
