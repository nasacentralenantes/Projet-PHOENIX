# BMP280 Temperature and Pressure Project

This project reads temperature and pressure from a BMP280 sensor using a Raspberry Pi.

## Files included

- `alt_press_temp.py` – Python script.
- `bmp280/` – Local BMP280 library included.
- `requirements.txt` – External dependencies (`smbus2`).
- `.envrc` – Automatically activates virtual environment (requires `direnv`).

## Why include the library folder?

Including the `bmp280/` folder makes the project **self-contained**.  
Users don’t need to install `pimoroni-bmp280` via pip.

## Recommended: Use a virtual environment

Keeps dependencies isolated, avoids conflicts, and allows easy installation via `requirements.txt`.
