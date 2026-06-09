# Reading an Everlance-branded mileage Log to grab Personal and Work mileage and creating a new mileage CSV without their branding for later processing.

import csv
import pandas as pd
df = pd.read_csv("filename.csv") # Reading the original Everlance CSV
with open("filename.csv", "r") as f:
    data = csv.reader(f) # Reading each row
    for row in data
        if row = "Personal" # For the row that contains mileage driven for personal reasons
            personalMiles = usecols[1] # Assign the personal mileage to personalMiles
        if row = "Work" # For the row that contains mileage driven for any freelance-oriented purposes.
            workMiles = usecols[1] # Assign the business mileage to workMiles
        if row = "TOTAL" # Everlance has one cell called TOTAL that signals that what follows it is the log itself.
            mileageLog = userows[(row.index)+2] # Going down 2 rows to mark the start of the log.
            for row in mileageLog # Looping through to read through the data for the mileage log.
                data.to_csv('mileage.csv') # Creating a new CSV for the raw data.
