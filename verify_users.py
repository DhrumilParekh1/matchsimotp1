import sqlite3

def verify_users():
    conn = sqlite3.connect('match_simulator.db')
    cursor = conn.cursor()
    
    try:
        # Get all users
        cursor.execute("SELECT id, username, role, status, email, club_name, cash FROM users")
        users = cursor.fetchall()
        
        if not users:
            print("No users found in the database!")
            return
            
        print("\nCurrent Users in Database:")
        print("-" * 80)
        print(f"{'ID':<5} {'Username':<20} {'Role':<10} {'Status':<10} {'Email':<25} {'Club':<20} {'Cash'}")
        print("-" * 80)
        
        for user in users:
            print(f"{user[0]:<5} {user[1]:<20} {user[2]:<10} {user[3]:<10} {user[4] or 'N/A':<25} {user[5] or 'N/A':<20} {user[6] or 0}")
        
        # Check if ggboi exists and is admin
        cursor.execute("SELECT COUNT(*) FROM users WHERE username = 'ggboi' AND role = 'admin'")
        ggboi_exists = cursor.fetchone()[0] > 0
        
        print("\nVerification:")
        print(f"- Total users found: {len(users)}")
        print(f"- 'ggboi' admin account exists: {'✅' if ggboi_exists else '❌'}")
        
        if len(users) > 1:
            print("\n⚠️  Warning: More than one user found. Expected only 'ggboi' admin account.")
        
        if not ggboi_exists:
            print("\n❌ Error: 'ggboi' admin account is missing or doesn't have admin role!")
        
    except Exception as e:
        print(f"Error verifying users: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    verify_users()
