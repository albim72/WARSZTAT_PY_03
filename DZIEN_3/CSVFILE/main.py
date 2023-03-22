import csv

with open("firma.csv",encoding="utf-8") as p:
    csv_reader = csv.reader(p,delimiter=";")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Nazwa kolumny: {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} pracuje na stanowisku: {row[1]} i ma urodziny w miesiącu '
                  f'{row[2]}, otrzymuje nagrodę finansową w wysokości {row[3]} zł.')
            line_count += 1

    print(f"dodano {line_count} linii")
    print(f"dodano {line_count-1} osób")
