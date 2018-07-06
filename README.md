# Counting Money with THE REAL MCKOY
## AN APP FOR CONVERTING WORLDWIDE CURRENCIES

## Features
### Access to up-to-date currency rates via currencylayer.com with a custom-made formula for handling currency conversions at lightning speed.
### Graphical User Interface for ease of use, compatible with all systems.

## How to Run
### You will need to retrieve an access key from currencylayer.com (a free account will still allow you access to almost all of the features of this app...please see Considerations When Using the App). Once you have an access key, you can create a file called `config.py` and type the following:
```python
config = 'TYPE YOUR ACCESS KEY HERE'
```
### Save the file and add it to the root directory. Althought this program makes use of the brilliant and very old Tkinter module, this code is bound to Python 3, and will need this interpreter in order to run. You can install all of the requirements needed to run this application via the following bash command:
```bash
pip install -r requirements.txt
```
### Please note, you may need to use `pip3` depending on your installation of Python 3. In order to start the program, you can run: 
```bash
python3 cc_gui.py
```
### and a new window will appear sporting the graphical user interface of the Currency Converter Application.

## How to Use
### You will see a entry box for a source country, a currency name for the country you would like to convert to or from, and the amount you would like to convert.  The source country must be typed as an abbreviation (refer to view sources in the menu), but for now only USD is available (please see Considerations When Using the App section). The currency name can be typed as an abbreviation or in it's long form (e.g. `AUD` or `Australian Dollar`). The amount can be written as an whole integer (positive or negative) or as a decimal (e.g. 34.22)--you can add as many digits as you like after the decimal point but the conversion will always be rounded to the nearest hundredth.  Click the `CONVERT IT!` button to display your conversion in a text box, which you can edit by typing into the box and copy using the command `CTRL-V` for PC's and `COMMAND-V` for Mac's.

## Considerations When Using the App
### Due to the limitations of the API, the app is only able to use USD as its source currency.  Functionality for different source countries will come later or you can upgrade your access key via currencylayer.com, and then you will be able to use the app to its full functionality.

### If your country does not match a country or country abbreviation, the program will display errors in the console but will not break and will allow you to make the appropriate changes.

### When changing to `DARK THEME`, if you would like to revert back to the normal theme, you will need to close the program and re-open it.

