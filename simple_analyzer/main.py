def read_config():
    config = {}
    with open("config/config.txt") as f:
        for line in f:
            if "=" in line:
                key, value = line.strip().split("=")
                config[key] = int(value)
    return config

if __name__ == "__main__":
    cfg = read_config()
    print("Interval:", cfg["interval"])
    print("Sequence length:", cfg["sequence_length"])
