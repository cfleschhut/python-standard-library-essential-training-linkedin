import array
import csv
import statistics

sample_data1 = [1, 3, 5, 7]
sample_data2 = [2, 3, 5, 4, 3, 5, 3, 2, 5, 6, 4, 3]

print(statistics.mean(sample_data1))

print(statistics.median(sample_data1))
print(statistics.median_low(sample_data1))
print(statistics.median_high(sample_data1))

print(statistics.mode(sample_data2))


def readData():
    with open("StockQuotes.csv") as dataFile:
        data = array.array('f', [])
        reader = csv.reader(dataFile)

        for i, row in enumerate(reader):
            if i == 0:  # headers row
                continue

            item = float(row[4])
            data.append(item)

        print(f"Read {len(data)} rows of data.")

        return data


def calcStats():
    data = readData()
    # print(data)

    data_mean = statistics.mean(data)
    data_med = statistics.median(data)
    data_std = statistics.stdev(data)
    data_var = statistics.variance(data)

    print("Mean: ", data_mean)
    print("Median: ", data_med)
    print("Standard deviation: ", data_std)
    print("Variance: ", data_var)


calcStats()
