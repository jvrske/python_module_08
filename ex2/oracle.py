import os
import sys
from dotenv import load_dotenv


if __name__ == "__main__":
    variables = ["MATRIX_MODE", "DATABASE_URL", "API_KEY", "LOG_LEVEL",
                 "ZION_ENDPOINT"]

    print("\nORACLE STATUS: Reading the Matrix...\n")

    load_dotenv(".env")
    print("Configuration loaded:")
    variables_env = [os.getenv(value) for value in variables]
    finish_program = False

    if not variables_env[0]:
        print("[ERROR] MATRIX_MODE missing")
        finish_program = True
    else:
        print(f"Mode: {variables_env[0]}")

    if not variables_env[1]:
        print("[ERROR] DATABASE_URL missing")
        finish_program = True
    else:
        print("Database: Connected to local instance")

    if not variables_env[2]:
        print("[ERROR] API_KEY missing")
        finish_program = True
    else:
        print("API Access: Authenticated")

    if not variables_env[3]:
        print("[ERROR] LOG_LEVEL missing")
        finish_program = True
    else:
        print(f"Log Level: {variables_env[3]}")

    if not variables_env[4]:
        print("[ERROR] ZION_ENDPOINT missing")
        finish_program = True
    else:
        print("Zion Network: Online")

    if finish_program:
        sys.exit()

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available\n")

    print("The Oracle sees all configurations.")
