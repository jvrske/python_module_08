import sys
import os
import site


# This program checks whether Python is running inside a virtual environment
# or in the global system environment.

if __name__ == "__main__":
    # sys.prefix != sys.base_prefix means that Python is running inside a
    #  virtual environment
    if sys.prefix != sys.base_prefix:
        print("\nMATRIX STATUS: Welcome to the construct\n")

        # Show the full path to the Python executable currently being used
        print(f"Current Python: {sys.executable}")
        # Display the name of the virtual environment folder
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        # Display the path where the virtual environment is located
        print(f"Environment Path: {sys.prefix}")

        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")

        print("\nPackage installation path:")
        # Show where Python packages will be installed inside this environment
        print(site.getsitepackages()[0])
    else:
        # This block runs if Python is not in a virtual environment
        print("\nMATRIX STATUS: You're still plugged in\n")

        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")

        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.")

        print("\nTo enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # on Unix")
        print("matrix_env")
        print("Scripts")
        print("activate   # On Windows")

        print("\nThen run this program again.")
