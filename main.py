import os

TEXT = "I can stop time for exactly one second a year, and I always waste it blinking."


def main():
    assert 1 <= len(TEXT) <= 200 and TEXT.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
