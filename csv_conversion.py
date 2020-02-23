import csv

csv_file = input('Zadejte jméno vstupního souboru (včetně .csv): ')
txt_file = 'open.txt'
txt_file2 = 'close.txt'

with open(txt_file, "w") as output_file:
    with open(csv_file, "r") as input_file:
        reading = csv.DictReader(input_file)
        for row in reading:
            output_file.write(row['Open']+'\n')
        output_file.close()
        
with open(txt_file2, "w") as output_file:
    with open(csv_file, "r", newline='') as input_file:
        reading = csv.DictReader(input_file)
        for row in reading:
            output_file.write(row['Close']+'\n')
        output_file.close()      