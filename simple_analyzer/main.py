import random
import time
from datetime import datetime
from simple_analyzer.analyzer import Analyzer

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
    interval = cfg["interval"]
    limit = cfg["sequence_length"]

    analyzer = Analyzer()

    while True:
        x = random.randint(1, 100)
        analyzer.add_number(x)

        if len(analyzer.numbers) > limit:
            analyzer.numbers.pop(0)

        print("Numbers:", analyzer.numbers)
        print("Even:", analyzer.even_count())
        print("Odd:", analyzer.odd_count())
        print("Highest:", analyzer.highest_number())
        print("Increasing pairs:", analyzer.increasing_pairs())
        print()

        now = datetime.now()
        if len(analyzer.numbers) == limit and now.second == 0:
            break

        time.sleep(interval)

