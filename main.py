from src.detect import Detect as det

if __name__ == "__main__":
    try:
        det.adb_detect()
    except KeyboardInterrupt:
        print("\n\nProgrammed stopped with CTRL+C")
    finally:
        exit()
