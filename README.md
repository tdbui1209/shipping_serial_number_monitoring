# Shipping Serial Number Monitoring

## Description:
This project is designed to query shipping serial number (SSN) data from MES Oracle database, perform calculations to determine total SSN, remaining SSN, and percentage of remaining SSN. Then send an email notification with the monitoring results.
![Untitled1](https://github.com/tdbui1209/shipping_serial_number_monitoring/assets/72682397/3a960ebd-8d4b-4156-bd13-4ff1fc524e1c)

## Features:
1. Data querying: The system retrives SSN data from MES Oracle database using SQL queries.
2. Data manipulation: It calculates the total SSN, remaining SSN anf the percentage of SSN used.
3. Email notification: After the calculations, the system sends and email to the product team with the monitoring results.

## Setup Introductions:
1. Prerequisites: Python 3.10.11 and required packages in requirements.txt
2. Configuration: Update the database connection details, email server details, sender and recipient email addresses, and any other relevent configurations in the **config.json** file.
3. Running the system: Execute the main.py script to initiate the SSN monitoring process.

## Usage:
1. Run the main.py script to start the monitoring process.
2. Monitor the email inbox specified in the configuration file for monitoring results.
