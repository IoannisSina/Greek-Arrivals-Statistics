import csv 
import xlrd
import re
import os

def create_csv():
    year = 2011
    months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
    header = ["country", "air", "railway", "sea", "road", "total"]
    current_directory = os.path.dirname(os.path.realpath(__file__))
    while(year != 2016):
        current_book = current_directory + "\\XLS\\" + str(year) + ".xls"
        workbook = xlrd.open_workbook(current_book)

        # for every xls open every sheet of it (12 months)
        for i in range(len(months)):
            record = []
            table = []
            csv_name = current_directory + "\\CSV\\" + months[i] + "_" + str(year) + ".csv"
            current_worksheet = workbook.sheet_by_index(i)

            total_rows = current_worksheet.nrows
            total_cols = current_worksheet.ncols
            #
            for x in range(total_rows):
                #takes lines that stars with int number and a dot
                match = re.match(r"[0-9]+\.", current_worksheet.cell(x,0).value, flags=0)

                #stops when we find a * in the start of a line
                match_stop = re.search("Source", current_worksheet.cell(x,0).value)
                if match_stop:
                   break
                if match:
                    #if we have the match we want
                    country = current_worksheet.cell(x, 1).value
                    if country == "Croatia (2)":
                        country = "Croatia"
                    record.append(country)
                    # iterate the row and append to record list
                    for y in range(2, total_cols):
                        temp = current_worksheet.cell(x, y).value
                        if temp == "":
                            record.append(0)
                        else:
                            record.append(round(temp))
                    #append the record to the table list
                    table.append(record)
                    record = []
            # write every record in the table in the csv
            with open(csv_name, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(header)
                for rec in table:
                    writer.writerow(rec)
        year +=1
        

#create_csv()