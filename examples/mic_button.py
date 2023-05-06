import evdev

device = evdev.InputDevice('/dev/input/event15')

print(device)

for event in device.read_loop():
    if event.type == evdev.ecodes.EV_KEY:
        # Print the event code and value (1 for keydown, 0 for keyup)
        print(evdev.categorize(event))
