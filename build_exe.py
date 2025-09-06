#!/usr/bin/env python3
"""
Build script for creating Astragalomancy executable using PyInstaller
"""

import subprocess
import sys
import os

def build_executable():
    """Build the game executable using PyInstaller"""
    
    # PyInstaller command
    cmd = [
        "C:/msys64/ucrt64/bin/python.exe",
        "-m", "PyInstaller",
        "--onefile",  # Create a single executable file
        "--windowed",  # Don't show console window (for GUI apps)
        "--name", "Astragalomancy",
        "--add-data", "src;src",  # Include src directory
        "--distpath", "dist",  # Output directory
        "--workpath", "build",  # Temporary build directory
        "--specpath", ".",  # Where to put the .spec file
        "src/main.py"
    ]
    
    print("Building Astragalomancy executable...")
    print(f"Command: {' '.join(cmd)}")
    
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("Build successful!")
        print("Executable created in: dist/Astragalomancy.exe")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Build failed with error: {e}")
        print(f"stdout: {e.stdout}")
        print(f"stderr: {e.stderr}")
        return False

if __name__ == "__main__":
    success = build_executable()
    if success:
        print("\n✅ Build completed successfully!")
        print("You can now run: dist/Astragalomancy.exe")
    else:
        print("\n❌ Build failed!")
        sys.exit(1)

