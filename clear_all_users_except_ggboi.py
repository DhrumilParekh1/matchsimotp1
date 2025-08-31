import sqlite3

def clear_users_except_ggboi():
    conn = sqlite3.connect('match_simulator.db')
    cursor = conn.cursor()
    
    try:
        # Delete all users except 'ggboi'
        cursor.execute("DELETE FROM users WHERE username != 'ggboi'")
        
        # Reset ggboi's data to default admin
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
        
        # Clear all related data
        cursor.execute("DELETE FROM transfer_bids")
        cursor.execute("DELETE FROM squad_uploads")
        cursor.execute("DELETE FROM user_inventory")
        
        conn.commit()
        print("Successfully cleared all user data except 'ggboi' admin account.")
        print("'ggboi' account has been reset with default admin privileges.")
        print("Password: admin123")
    except Exception as e:
        print(f"Error clearing user data: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    clear_users_except_ggboi()
