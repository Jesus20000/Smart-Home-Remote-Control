Smart Home Remote Control - Command Design Pattern

Overview:
This project demonstrates the Command Design Pattern using a simulated smart home system.
A central RemoteControl object sends command objects to devices like lights. It supports flexible mappings and undo operations.

Files:
- command.py: Abstract Command interface.
- receiver.py: Light class (receiver that performs the action).
- commands.py: Concrete commands for turning lights on/off.
- remote_control.py: Invoker that maps buttons to commands and triggers execution.
- main.py: Demonstrates assigning commands and executing them via simulated remote control.
- README.md: Project description and instructions.

How to Run:
1. Save all files in the same folder.
2. Open terminal and navigate to the folder.
3. Run the program using:

   python main.py

Expected Output:
Button presses simulate light operations, and undo functionality reverses the last action.

Example:
Living Room Light is ON  
Undoing last command...  
Living Room Light is OFF  
Living Room Light is OFF  
Kitchen Light is ON

Author:
Isa Zeynalov
