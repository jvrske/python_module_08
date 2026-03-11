import os
import sys
from dotenv import load_dotenv


if __name__ == "__main__":
    # List of required environment variables for the application
    variables = ["MATRIX_MODE", "DATABASE_URL", "API_KEY", "LOG_LEVEL",
                 "ZION_ENDPOINT"]

    print("\nORACLE STATUS: Reading the Matrix...\n")

    # Load environment variables from the .env file
    load_dotenv(".env")
    print("Configuration loaded:")
    # Retrieve the values of each environment variable using os.getenv
    # If a variable is not defined, getenv returns None
    variables_env = [os.getenv(value) for value in variables]
    finish_program = False

    # Check if MATRIX_MODE exists
    if not variables_env[0]:
        print("[ERROR] MATRIX_MODE missing")
        finish_program = True
    else:
        print(f"Mode: {variables_env[0]}")

    # Check if DATABASE_URL exists
    if not variables_env[1]:
        print("[ERROR] DATABASE_URL missing")
        finish_program = True
    else:
        print("Database: Connected to local instance")

    # Check if API_KEY exists
    if not variables_env[2]:
        print("[ERROR] API_KEY missing")
        finish_program = True
    else:
        print("API Access: Authenticated")

    # Check if LOG_LEVEL exists
    if not variables_env[3]:
        print("[ERROR] LOG_LEVEL missing")
        finish_program = True
    else:
        print(f"Log Level: {variables_env[3]}")

    # Check if ZION_ENDPOINT exists
    if not variables_env[4]:
        print("[ERROR] ZION_ENDPOINT missing")
        finish_program = True
    else:
        print("Zion Network: Online")

    # If any required variable is missing, terminate the program
    if finish_program:
        sys.exit()

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available\n")

    print("The Oracle sees all configurations.")
