import subprocess, re


class Detect:
    def adb(self):
        result = subprocess.run(
            ["adb devices -l"], shell=True, capture_output=True, text=True
        )
        connected = re.search(r"device:(\w+)", result.stdout)
        if connected:
            device = connected.group(1)
            print(f"{device} connected")
        else:
            print("ADB not det")

    def fastboot(self):
        result = subprocess.run(
            ["fastboot getvar all"], shell=True, capture_output=True, text=True
        )
        connected = re.search(r"product:(\w+)", result.stderr)
        if connected:
            device = connected.group(1)
            print(f"{device} connected")
        else:
            print("FB not det")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgrammed stopped with CTRL+C")
    finally:
        exit()
