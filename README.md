# Inventory Control System for a Small Market

## What this project is:
A simple inventory control system developed in Python, using Python libraries like `Tkinter` and `PySimpleGUI` for interface creation and `MySQL` for the relational database.

## How to use:
## 1. Open your terminal (Vscode or Linux) and run:
```
git clone https://github.com/rogerrgab/Inventory-Control-System-Py.git
```

## 2. Make sure you have the following Python dependencies installed: `pip` | `tkinter` | `PySimpleGUI` | `mysql.connector`.
* Note: MySQL must be installed on your Operating System.

## 3. How to install the dependencies:
## Note: If you don't have `pip` installed, then run the following commands in your terminal:

## Ubuntu-based systems:
```
sudo apt update
sudo apt upgrade
sudo apt install python3-pip
```
Verify if it was installed correctly:
```
pip3 --version
```

## Fedora-based systems:
```
sudo dnf update
sudo dnf install python3-pip
```
Verify if it was installed correctly:
```
pip3 --version
```

## Installing Tkinter:
## Ubuntu systems:
```
sudo apt update
sudo apt install python3-tk
python3 -m tkinter
```
## Fedora systems:
```
sudo dnf update
sudo dnf install python3-tkinter
python3 -m tkinter
```

## Installing PySimpleGUI:
```
pip3 install pysimplegui
```
or
```
pip3 install PySimpleGUI
```  

## Installing MySQL Connector for Python:
```
pip install mysql-connector-python
```

## 4. Run this command on your terminal in the  `./InventoryControl-py` folder:
```
python3 app.py
```

## Note: If any error occurs due to package dependencies, follow the steps below and then repeat the three steps mentioned above:
1. Install `python3-venv` (if not installed):
```
sudo apt install python3-venv
```

2. Create a virtual environment:
```
python3 -m venv myenv
```

3. Activate the created virtual environment:
```
source myenv/bin/activate
```

4. Install `PySimpleGUI` within this separate virtual environment:
```
pip install PySimpleGUI
```

5. To deactivate the virtual environment, run:
```
deactivate
```
