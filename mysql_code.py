import sqlite3
import re 
import xlrd
import os

current_directory = os.path.dirname(os.path.realpath(__file__))
def db_create_tables():
    # Open database connection
    conn = sqlite3.connect("python_project.db")
    c = conn.cursor()


    year = 2011
    months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
    # create 60 tables  with all months and year
    while year != 2016:
        tables_atrr = "(country text, air INTEGER, railway INTEGER, sea INTEGER, road INTEGER, total INTEGER, primary key(country))"
        for i in range(0, len(months)):
            table_name = months[i] + "_" + str(year)
            sql = "CREATE TABLE " + table_name + tables_atrr
            c.execute(sql)
        year +=1
    
    conn.commit()
    conn.close()

def db_insert():
     # Open database connection
    conn = sqlite3.connect("python_project.db")

    # prepare a cursor object using cursor() method
    c = conn.cursor()

    year = 2011
    months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]

    # open every xls [2011-2015]
    while(year != 2016):
        current_book = current_directory + "\\XLS\\" + str(year) + ".xls"
        workbook = xlrd.open_workbook(current_book)

        # for every xls open every sheet of it (12 months)
        for i in range(0, len(months)):
            record = []
            current_db_table = months[i] + "_" + str(year)
            current_worksheet = workbook.sheet_by_index(i)
            total_rows = current_worksheet.nrows
            total_cols = current_worksheet.ncols
            # if the it matches the correct string insert it into the db
            for x in range(total_rows):
                #if we have the right match continue
                match = re.match(r"[0-9]+\.", current_worksheet.cell(x,0).value, flags=0)

                #else stop
                match_stop = re.search("Source", current_worksheet.cell(x,0).value)
                if match_stop:
                   break
                if match:
                    record.append(current_worksheet.cell(x, 1).value)
                    for y in range(2, total_cols):
                        temp = current_worksheet.cell(x, y).value
                        if temp == "":
                            record.append(0)
                        else:
                            #round because some values of the xls are floats
                            record.append(round(temp))

                    # if match is ok ------> INSERT
                    sql = "INSERT INTO "+ current_db_table + " VALUES(?, ?, ?, ?, ?, ?)"
                    val = (str(record[0]), record[1] ,record[2] ,record[3] ,record[4] ,record[5])
                    try:
                        # Executing the SQL command
                        c.execute(sql, val)
                        # Commit your changes in the database
                        conn.commit()

                    except:
                        # Rolling back in case of error
                        print("failed")
                    record = []
        year +=1
    conn.close()       



db_create_tables()
db_insert()


