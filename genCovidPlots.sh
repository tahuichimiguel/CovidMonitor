rm covid_confirmed_usafacts.csv
wget --no-check-certificate "https://usafactsstatic.blob.core.windows.net/public/data/covid-19/covid_confirmed_usafacts.csv"

echo “hello printf”
source /Users/z003jqq/python-virtual-environments/env/bin/activate
python GeneratePlots.py

open *.png
