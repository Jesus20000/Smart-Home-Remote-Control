class RemoteControl:
    def __init__(self):
        self._buttons = {}
        self._last_command = None

    def set_command(self, button_name, command):
        self._buttons[button_name] = command

    def press_button(self, button_name):
        command = self._buttons.get(button_name)
        if command:
            command.execute()
            self._last_command = command
        else:
            print(f"No command assigned to button '{button_name}'.")

    def press_undo(self):
        if self._last_command:
            print("Undoing last command...")
            self._last_command.undo()
        else:
            print("Nothing to undo.")
