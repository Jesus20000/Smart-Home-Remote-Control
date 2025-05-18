from receiver import Light
from commands import LightOnCommand, LightOffCommand
from remote_control import RemoteControl

def main():
    living_room_light = Light("Living Room")
    kitchen_light = Light("Kitchen")

    remote = RemoteControl()
    remote.set_command("A", LightOnCommand(living_room_light))
    remote.set_command("B", LightOffCommand(living_room_light))
    remote.set_command("C", LightOnCommand(kitchen_light))

    remote.press_button("A")
    remote.press_undo()
    remote.press_button("B")
    remote.press_button("C")

if __name__ == "__main__":
    main()