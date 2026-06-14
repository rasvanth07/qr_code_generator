# QR Code Generator

Python scripts for QR code generation, QR code scanning, and barcode generation.

## Files

- **qrcodegenerator.py** - Generate QR codes from URLs with custom filename
- **qrscanner.py** - Scan QR codes using webcam and open in browser
- **barcodegenerator.py** - Generate barcodes (code128)

## Create & Activate Python Virtual Environment

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows (Command Prompt)

```cmd
python -m venv venv
venv\Scripts\activate
```

### Windows (PowerShell)

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

To deactivate the virtual environment:

```bash
deactivate
```

## Requirements

```bash
pip install pyqrcode pypng opencv-python python-barcode
```

## Usage

```bash
python qrcodegenerator.py   # Generate QR code
python qrscanner.py         # Scan QR code via webcam
python barcodegenerator.py  # Generate barcode
```

> Made with rasvanth07 and vignesh0x — Feel free to fork and improve this guide!




## 🤝 Contributing

Pull requests are welcome! If you'd like to add new services or suggest new features, feel free to fork the repository and open a PR.
