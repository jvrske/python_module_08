import sys
import importlib


if __name__ == "__main__":
    # List of packages that the program depends on
    packages = ["pandas", "numpy", "matplotlib", "requests"]
    # Dictionary to store successfully imported modules
    modules = {}

    print("\nLOADING STATUS: Loading programs...\n")

    print("Checking dependencies:")
    for package in packages:
        try:
            # Dynamically import each package using importlib
            module = importlib.import_module(package)
            modules[package] = module
            # Print specific messages depending on the module
            if module.__name__ == "pandas":
                print(f"[OK] {module.__name__} ({module.__version__}) \
                      - Data manipulation ready")
            elif module.__name__ == "requests":
                print(f"[OK] {module.__name__} ({module.__version__}) \
                      - Network access ready")
            elif module.__name__ == "matplotlib":
                print(f"[OK] {module.__name__} ({module.__version__}) \
                      - Visualization ready")
        # If the module is not installed, show a warning
        except ImportError:
            print(f"[MISSING] {package} - Not installed")

    print("\nAnalyzing Matrix data...")

    # Generate 1000 random numbers using numpy
    data = modules["numpy"].random.normal(0, 1, 1000)
    # Create a pandas DataFrame with the generated data
    df = modules["pandas"].DataFrame({"signal": data})
    # Calculate a rolling mean with a window of 20 values
    df["rolling_mean"] = df["signal"].rolling(window=20).mean()

    # Import matplotlib.pyplot separately to create the plot
    plt = importlib.import_module("matplotlib.pyplot")

    # Plot the original signal data
    plt.plot(df["signal"])
    # Plot the rolling mean line
    plt.plot(df["rolling_mean"])

    # Save the generated visualization to the current environment path
    plt.savefig(f"{sys.prefix}/matrix_analysis.png")

    print(f"Processing {len(df)} data points...")
    print("Generating visualization...")

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")
