import csv

#there are 16642 lines of data in this csv
pressures = []
num_of_lines_to_process = 1000
biggestNumber = 0
with open('pressure_full.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
            
        else:
          #Set biggest number to the first row of data
          if(line_count == 1):
            biggestNumber = float(row[1])
            biggestTime = ""
            smallestNumber = float(row[1])
            smallestTime = ""
          #print(f'Pressure: \t{row[1]}')
          pressures.append([row[1],row[3]])
          #If the current value of the data is bigger than the previous biggestNumber, set biggestNumber equal to the new data value.
          if(biggestNumber<float(row[1])):
            biggestNumber = float(row[1])
            biggestTime = row[3]
          if(smallestNumber>float(row[1])):
            smallestNumber = float(row[1])
            smallestTime = row[3]
            
          line_count += 1
    print(f'Processed {line_count} lines.')
print(len(pressures))
print("Largest pressure is " + str(biggestNumber) + " at " + biggestTime)
print("Smallest pressure is " + str(smallestNumber) + " at " + smallestTime)
print(f'pressure is {pressures[0][0]} at {pressures[0][1]}' )
