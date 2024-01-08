import sys
from collections import defaultdict

class Station:
    min: float = None
    max: float = None
    sum: float = 0
    count: int = 0

    def mean(self):
        return self.sum / self.count


measurements = defaultdict(Station)

# python main "./1brc/measurements.txt"
if __name__ == "__main__":
    filename = sys.argv[1]

    with open(filename, 'r') as infile:
        for line in infile:
            station, temp = line.split(";")
            temp = float(temp)

            if measurements[station].min is None or temp < measurements[station].min:
                measurements[station].min = temp
            if measurements[station].max is None or temp > measurements[station].max:
                measurements[station].max = temp


            measurements[station].sum += temp
            measurements[station].count += 1

    count = len(measurements)
    print("{", end="")
    for n, (station, data) in enumerate(sorted(measurements.items())):
        suffix = ","
        if n == count - 1:
            suffix = ""
        print(f"{station}={data.min}/{data.mean():.1f}/{data.max}" ,end=suffix)
    print("}", end="")
