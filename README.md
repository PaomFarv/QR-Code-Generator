# QR Code Generator

## Description:
This project is a **QR Code Generator** built with `CustomTkinter` for a modern, user-friendly interface and `qrcode` for generating QR codes. The app allows users to input text, generate a QR code, and then save the QR code image to their system.

## Features:
- **QR Code Generation:** Converts the user input into a QR code.
- **Save Functionality:** Users can save the generated QR code as a `.png` file.
- **Dynamic UI:** The "Save Image" button appears only after the QR code is generated.
- **Simple and Clean UI:** Uses `CustomTkinter` for an appealing and modern design.

## Technologies:
- **Python:** The primary language used for building the application.
- **qrcode:** For generating the QR code.
- **CustomTkinter:** For building the graphical interface.
- **Tkinter:** For handling file dialogs and basic GUI elements.

## Installation:
1. Install required packages:
   ```bash
   pip install customtkinter qrcode Pillow
   ```

2. Run the script to open the QR Code Generator app.

## How it Works:
1. Input text into the provided entry field.
2. Click **Generate** to create the QR code.
3. After the QR code appears, click **Save Image** to save the QR code to your computer.

## License:
This project is open source and available under the [MIT License](LICENSE).
