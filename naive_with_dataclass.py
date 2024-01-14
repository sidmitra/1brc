"""
With dataclasses
"""
import sys
from dataclasses import dataclass

@dataclass
class Station:
    min: float
    max: float
    sum: float
    count: int

    def mean(self):
        return self.sum / self.count

measurements: dict[str, Station] = {}


def process(filename):
    with open(filename, 'r') as infile:
        for line in infile:
            station, temp_s = line.split(";")
            temp: float = float(temp_s)

            if station not in measurements:
                measurements[station] = Station(min=temp, max=temp, sum=temp, count=1)
            else:
                if temp < measurements[station].min:
                    measurements[station].min = temp
                if temp > measurements[station].max:
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


# python main "./1brc/measurements.txt"
if __name__ == "__main__":
    filename = sys.argv[1]
    process(filename)
