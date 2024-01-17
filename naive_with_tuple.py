"""
With simple tuple(min, max, sum, count)
"""
import sys


def mean(station):
    # sum/count
    # count cannot be zero, so not handling it.
    return station[2] / station[3]


measurements: dict = {}


def process(filename):
    with open(filename, 'r') as infile:
        for line in infile:
            name, temp_s = line.split(";")
            temp = float(temp_s)
            if (station := measurements.get(name)) is not None:
                _min = min(station.min, temp)
                _max = max(station.min, temp)
                _sum = station.sum + temp
                _count = station.count+1
                measurements[name] = (_min, _max, _sum, _count)
            else:
                measurements[name] = (temp, temp, temp, 1)


    count = len(measurements)
    print("{", end="")
    for n, (name, station) in enumerate(sorted(measurements.items())):
        suffix = ","
        if n == count - 1:
            suffix = ""
        print(f"{name}={station[0]}/{mean(station):.1f}/{station[1]}", end=suffix)
    print("}", end="")


# python main "./1brc/measurements.txt"
if __name__ == "__main__":
    filename = sys.argv[1]
    process(filename)
