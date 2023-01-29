## Description ⚡
Statistics of tourist arrivals in Greece 2011-2015 :car: :airplane: :ship: :train: :bar_chart:  

## Steps to run :runner:

Clone repository and cd to the folder
~~~
git clone https://github.com/IoannisSina/Greek-Arrivals-Statistics
cd Greek-Arrivals-Statistics
~~~

Create virtual enviroment and activate it:
~~~
python3 -m venv env
source env/bin/activate  # Activate on Linux/MacOS
env\Scripts\activate  # Activate on Windows
~~~

Install requirements:
~~~
pip install -r requirements.txt
~~~

Execute files in specific order
~~~
python3 download_XLS.py
python3 csv_code.py
python3 plots.py
~~~

or run with GUI :eyes:
~~~
brew install python-tk
python3 GUI.py
~~~
 
 
## Screenshots 📸

GUI:

![](/Screenshots/gui_en.png)

Total Arrivals 2011-2015:

![](/Screenshots/Total_arrivals.png)

Arrivals by means of transport 2011-2015:

![](/Screenshots/by_means.png)

Arrivals by quarter 2011-2015:

![](/Screenshots/quarter.png)
