"""
With dataclasses
"""
import sys
from dataclasses import dataclass
from collections import namedtuple


Station = namedtuple("Station", "min max sum count")

def mean(station):
    return station.sum / station.count

measurements: dict[str, Station] = {}


def process(filename):
    with open(filename, 'r') as infile:
        for line in infile:
            name, temp_s = line.split(";")
            temp = float(temp_s)
            if (station := measurements.get(name)) is not None:
                station.min = min(s.min, temp)
                station.max = max(s.max, temp)
                station.sum += temp
                station.count += 1
            else:
                measurements[name] = Station(min=temp, max=temp, sum=temp, count=1)


    count = len(measurements)
    print("{", end="")
    for n, (name, data) in enumerate(sorted(measurements.items())):
        suffix = ","
        if n == count - 1:
            suffix = ""
        print(f"{name}={data.min}/{mean(data):.1f}/{data.max}", end=suffix)
    print("}", end="")


# python main "./1brc/measurements.txt"
if __name__ == "__main__":
    filename = sys.argv[1]
    process(filename)
