# Astragalomancy Game Makefile
# Make sure you have MSYS2 installed with Python and pygame

# Variables
PYTHON = C:/msys64/ucrt64/bin/python.exe
GAME_DIR = src
MAIN_FILE = main.py

# Default target
.PHONY: all run clean install test help

# Run the game
run:
	@echo "Starting Astragalomancy..."
	$(PYTHON) $(GAME_DIR)/$(MAIN_FILE)

# Install dependencies (pygame)
install:
	@echo "Installing pygame via MSYS2..."
	C:/msys64/usr/bin/pacman.exe -S mingw-w64-ucrt-x86_64-python-pygame

# Clean up temporary files
clean:
	@echo "Cleaning up temporary files..."
	@if exist __pycache__ rmdir /s /q __pycache__
	@if exist src\__pycache__ rmdir /s /q src\__pycache__
	@if exist src\core\__pycache__ rmdir /s /q src\core\__pycache__
	@if exist src\entities\__pycache__ rmdir /s /q src\entities\__pycache__
	@if exist src\rooms\__pycache__ rmdir /s /q src\rooms\__pycache__
	@if exist src\systems\__pycache__ rmdir /s /q src\systems\__pycache__
	@if exist *.pyc del /q *.pyc
	@if exist src\*.pyc del /q src\*.pyc
	@if exist src\core\*.pyc del /q src\core\*.pyc
	@if exist src\entities\*.pyc del /q src\entities\*.pyc
	@if exist src\rooms\*.pyc del /q src\rooms\*.pyc
	@if exist src\systems\*.pyc del /q src\systems\*.pyc

# Check Python and pygame versions
check:
	@echo "Checking Python version..."
	$(PYTHON) --version
	@echo "Checking pygame version..."
	$(PYTHON) -c "import pygame; print(f'Pygame version: {pygame.version.ver}')"

# Run with verbose output
debug:
	@echo "Running game with debug output..."
	$(PYTHON) -u $(GAME_DIR)/$(MAIN_FILE)

# Build executable
build:
	@echo "Building executable..."
	$(PYTHON) build_exe.py

# Install PyInstaller
install-pyinstaller:
	@echo "Installing PyInstaller..."
	$(PYTHON) -m pip install pyinstaller

# Help
help:
	@echo "Available commands:"
	@echo "  make run     - Run the game"
	@echo "  make install - Install pygame dependencies"
	@echo "  make build   - Build executable"
	@echo "  make clean   - Clean up temporary files"
	@echo "  make check   - Check Python and pygame versions"
	@echo "  make debug   - Run game with verbose output"
	@echo "  make help    - Show this help message"

# Default target
all: run
