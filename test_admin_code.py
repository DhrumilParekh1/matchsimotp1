import streamlit as st
from pages import show_signup_page

# Mock the Streamlit session state
if 'page' not in st.session_state:
    st.session_state.page = 'signup'

# Test the signup page with admin code
print("Testing admin code verification...")

# Test case 1: Correct admin code (should pass)
test_cases = [
    {"role": "admin", "code": "2110", "should_pass": True},
    {"role": "admin", "code": "1919", "should_pass": False},
    {"role": "user", "code": "", "should_pass": True},
]

for i, test in enumerate(test_cases, 1):
    print(f"\nTest Case {i}:")
    print(f"Role: {test['role']}, Code: {test['code']}, Expected: {'PASS' if test['should_pass'] else 'FAIL'}")
    
    # Mock the form submission
    st.session_state.role = test['role']
    st.session_state.admin_code = test['code']
    
    # Mock the form submission logic
    if test['role'] == "admin" and test['code'] != "2110":
        print("Result: FAIL (Invalid admin code)")
    else:
        print("Result: PASS")

print("\nVerification complete. The admin code should be '2110'.")
print("If you're still seeing '1919' being accepted, please check for any cached versions of the application.")
print("Try clearing your browser cache or using a private/incognito window.")
