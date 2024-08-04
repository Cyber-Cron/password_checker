import re

def check_password_strength(password):
	"""

	Check the strength of the provided password.
	"""
	if len(password) < 8:
		return "Password is too short. It must be at least 8 characters long."
	if not re.search(r"[A-Z]", password):
		return "Password must include at least one uppercase letter."
	if not re.search(r"[a-z]", password):
		return "Password must include at least one lowercase letter."
	if not re.search(r"[0-9]", password):
		return "Password must include at least one number."
	if not re.search(r"[!@#$%^&*()_+{}\[\]:;,.<>?]", password):
		return "Password must include at least one special character."
	return "Password is strong."

if __name__ == "__main__":
	password = input("Enter a password to check: ")
	print(check_password_strength(password))
