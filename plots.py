import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
import operator
import os

current_directory = os.path.dirname(os.path.realpath(__file__))
months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
years = ["2011", "2012", "2013", "2014", "2015"]


def plot_1():


    year = 2011
    total_tourists = []
    # opening every csv for ever year
    while year != 2016:
        temp_sum = 0
        for i in range(len(months)):
            csv_name = os.path.join(current_directory, "CSV", months[i] + "_" + str(year) + ".csv")
            df = pd.read_csv(csv_name)

            data = pd.DataFrame(df)
            
            # sums the whole total column of the csv and adds it to the previous one 
            temp_sum += data['total'].sum()
        total_tourists.append(temp_sum)
        year +=1
    

    #dividing plot by 5
    xpos = np.arange(len(years)) 

    #writes years on x-axis
    plt.xticks(xpos, years)

    #plot title and labels
    # plt.title("Συνολικές αφίξεις στην Ελλάδα για την πενταετία 2011-2015 ")
    # plt.xlabel("Χρονιά")
    # plt.ylabel("Αφίξεις")
    plt.title("Number of arrivals in Greece from 2011 to 2015")
    plt.xlabel("Year")
    plt.ylabel("Arrivals")

    #plots
    plot = plt.bar(xpos, total_tourists)

    #setting bars colors and writing text on them 
    for bar in plot:
        bar.set_color('c')
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')
    
    #maximizes plot
    # manager = plt.get_current_fig_manager()
    # manager.resize(*manager.window.maxsize())
    plt.show()

def plot_2(grafhma_no):
    year = 2011

    # dictionary holding sum of tourists per country
    dict_all_years = {}
    dict_each_year = [{}, {}, {}, {}, {}]

    #open all csv
    while year != 2016:
        for i in range(len(months)):
            csv_name = os.path.join(current_directory, "CSV", months[i] + "_" + str(year) + ".csv")
            df = pd.read_csv(csv_name)
            data = pd.DataFrame(df)

            rows = len(df.axes[0])
            
            # for each country for each month add its total to the key on the dictionary
            for x in range (rows):
                country = df.iloc[x,0]
                country_total = df.iloc[x,5]
                current_year = year-2011
                #keep all countries separately to create 5 graphs(one for each year)
                if country in dict_each_year[current_year]:
                    dict_each_year[current_year][country] += country_total
                else:
                    dict_each_year[current_year][country] = country_total

                #keep count for all years to create one graph
                if country in dict_all_years:
                    dict_all_years[country] += country_total
                else:
                    dict_all_years[country] = country_total
                
        year +=1

    #sort the dictionary so we have small to biggest tourists number
    sorted_all_years = sorted(dict_all_years.items(), key=operator.itemgetter(1))

    #sort all dictionaries for each year
    sorted_for_each_year = []
    for i in range(len(years)):
        sorted_for_each_year.append(sorted(dict_each_year[i].items(), key=operator.itemgetter(1)))
        

    # taking the last 10 countries with biggest numbers for each year separately
    countries_names_each = [[], [], [], [], []]
    countries_total_each = [[], [], [], [], []]
    for i in range(len(sorted_for_each_year)):
        for j in range(len(sorted_for_each_year[i])-10, len(sorted_for_each_year[i])):
            countries_names_each[i].append(sorted_for_each_year[i][j][0])
            countries_total_each[i].append(sorted_for_each_year[i][j][1])


    countries_names_all = []
    countries_total_all = []
    # taking the last 10 countries with biggest arrivals for all years
    for c in range(len(sorted_all_years)-10, len(sorted_all_years)):
        countries_names_all.append(sorted_all_years[c][0])
        countries_total_all.append(sorted_all_years[c][1])
    
    #call function of ploting for all years
    if grafhma_no == -1:
        #plot for all years 
        grafhma_2_plots(countries_names_all, countries_total_all, "2011-2015")
    else:    
        title = str(grafhma_no)
        grafhma_2_plots(countries_names_each[grafhma_no-2011], countries_total_each[grafhma_no-2011], title)

def plot_3():
    year = 2011
    air_list = []
    railway_list = []
    sea_list = []
    road_list = []
    #open every csv
    while year != 2016:
        temp_air = 0
        temp_railway = 0
        temp_sea = 0
        temp_road = 0
        for i in range(len(months)):
            csv_name = os.path.join(current_directory, "CSV", months[i] + "_" + str(year) + ".csv")
            df = pd.read_csv(csv_name)

            data = pd.DataFrame(df)

            #add the whole column of the current csv and sum it to the previous one
            temp_air += data['air'].sum()
            temp_railway += data['railway'].sum()
            temp_sea += data['sea'].sum()
            temp_road += data['road'].sum()
        
        #append the final sum for each year in the lists below
        air_list.append(temp_air)
        railway_list.append(temp_railway)
        sea_list.append(temp_sea)
        road_list.append(temp_road)
        
        year +=1


    #dividing plot by 5
    xpos = np.arange(len(years)) 
   
    #plt.xticks(xpos)
    plt.xticks(xpos, years)

    #bars positions and labels
    plt.bar(xpos - 0.15, air_list, color = 'm', width = 0.1, label='AIRPLANE')
    plt.bar(xpos - 0.05, railway_list, color = 'y', width = 0.1, label='TRAIN')
    plt.bar(xpos + 0.05 , sea_list, color = 'r', width = 0.1, label='BOAT')
    plt.bar(xpos + 0.15, road_list, color = 'c', width = 0.1, label='CAR')


    #set title and labels
    # plt.title("Aφίξεις τουριστών στην Ελλάδα ανά μέσο μεταφοράς για την πενταετία 2011-2015 ")
    # plt.xlabel("Χρονιά")
    # plt.ylabel("Αφίξεις")
    plt.title("Arrivals of tourists in Greece by means of transport 2011-2015")
    plt.xlabel("Year")
    plt.ylabel("Arrivals")

    #set legend so that it does not overlap
    plt.legend(bbox_to_anchor=(0., 1.05, 1, .102), loc=3,
       ncol=2, mode="expand", borderaxespad=0.)


    # texting 0 over bars whose value is 0
    plt.text(xpos[1] - 0.05, 2500, 0, ha='center', va='bottom', color='y')
    plt.text(xpos[2] - 0.05, 2500, 0, ha='center', va='bottom', color='y')


    #maximizes plot
    #manager = plt.get_current_fig_manager()
    #manager.resize(*manager.window.maxsize())

    #log scale so all bars can be seen
    plt.yscale('log')
    plt.show()

def plot_4():

    year = 2011

    # all_years_quarters[0][0] = first quarter of 2011, all_years_quarters[0][1] = fist quarter of 2012  
    all_years_quarters = [[], [], [], []]
    # opening every csv for ever year
    while year != 2016:
        quarter_sum = 0
        current_quarter = 0
        for i in range(len(months)):
            csv_name = os.path.join(current_directory, "CSV", months[i] + "_" + str(year) + ".csv")
            df = pd.read_csv(csv_name)
            data = pd.DataFrame(df)
            
            # every 3 months we append the total sum and we increase the current_quarter by 1
            if i % 3 != 0 or i ==0:
                quarter_sum += data['total'].sum()
                if i == 11:
                    all_years_quarters[current_quarter].append(quarter_sum)
            else:
                all_years_quarters[current_quarter].append(quarter_sum)
                quarter_sum = data['total'].sum()
                current_quarter +=1
        year +=1
    #dividing plot by 5
    xpos = np.arange(len(years)) 
   
    #plt.xticks(xpos)
    plt.xticks(xpos, years)

    #bars positions and labels
    plt.bar(xpos - 0.15, all_years_quarters[0], color = 'r', width = 0.1, label='First quarter')
    plt.bar(xpos - 0.05, all_years_quarters[1], color = 'y', width = 0.1, label='Second quarter')
    plt.bar(xpos + 0.05 , all_years_quarters[2], color = 'm', width = 0.1, label='Third quarter')
    plt.bar(xpos + 0.15, all_years_quarters[3], color = 'c', width = 0.1, label='Fourth quarter')


    #set title and labels
    # plt.title("Αφίξεις τουριστών στην Ελλάδα ανά τρίμηνο για την πενταετία 2011-2015")
    # plt.xlabel("Χρονιά")
    # plt.ylabel("Αφίξεις")
    plt.title("Arrivals of tourists in Greece per quarter 2011-2015")
    plt.xlabel("Year")
    plt.ylabel("Arrivals")
    plt.legend()


    #maximizes plot
    # manager = plt.get_current_fig_manager()
    # manager.resize(*manager.window.maxsize())

    plt.show()

def grafhma_2_plots(countries_names, countries_total, title):
    xpos = np.arange(len(countries_names)) 

    # #writes years on x-axis
    plt.xticks(xpos, countries_names,  ha='center', fontsize=7)

    # #plot title and labels
    # plt.title("10 πρώτες Χώρες καταγωγής με το μεγαλύτερο μερίδιο στις αφίξεις "+title)
    # plt.xlabel("Χώρα")
    # plt.ylabel("Αφίξεις")
    plt.title("10 first countries with the biggest number of arrivals"+title)
    plt.xlabel("Country")
    plt.ylabel("Arrivals")

    #plots
    plot = plt.bar(xpos, countries_total)

    for bar in plot:    
        bar.set_color('m')
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')

#maximizes plot
    # manager = plt.get_current_fig_manager()
    # manager.resize(*manager.window.maxsize())
    plt.show()

if __name__ == "__main__":
    plot_1()
    plot_2(-1)
    plot_3()
    plot_4()
