# 🏠 Smart Home Remote Control

This project demonstrates the **Command Design Pattern** in Python by simulating a smart home remote control system. Devices like lights can be controlled via button-mapped command objects with support for undoing actions.

---

## 🛠️ Technologies Used

- Python 3.x  
- Object-Oriented Programming  
- Command Design Pattern

---

## 🧠 Design Pattern: Command

The **Command Pattern** encapsulates requests as objects, allowing you to parameterize methods, queue commands, and implement features like undo. It decouples the sender of a request (remote control) from the object that performs the action (e.g., light).

---

## 📁 Project Structure

- `command.py` – Abstract Command interface  
- `receiver.py` – Contains device logic (e.g., `Light`)  
- `commands.py` – Concrete command classes (`LightOnCommand`, `LightOffCommand`)  
- `remote_control.py` – Invoker that maps buttons to commands  
- `main.py` – Simulates device control via button presses  
- `README.md` – Project documentation

---

## 🚀 Features

- Assign commands to remote control buttons  
- Execute commands (e.g., turn lights on/off)  
- Undo the last command  
- Easily extendable for more devices like fans, thermostats, etc.

---

## 📌 Sample Output

```

Living Room Light is ON
Undoing last command...
Living Room Light is OFF
Living Room Light is OFF
Kitchen Light is ON

````

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/yourusername/smart-home-remote-control.git
cd smart-home-remote-control
````

2. Run the main script:

```bash
python main.py
```
