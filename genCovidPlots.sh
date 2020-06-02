rm covid_confirmed_usafacts.csv
wget --no-check-certificate "https://usafactsstatic.blob.core.windows.net/public/data/covid-19/covid_confirmed_usafacts.csv"

echo “hello printf”
source /Users/mikey/python-env/python3.8/bin/activate
python GeneratePlots.py

open *.png
