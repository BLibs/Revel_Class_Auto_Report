# Class Sales Report Automation

This project automates the process of pulling product mix data from the Revel API for multiple establishments, compiling it into a report that shows a breakdown of sales across various items and their corresponding classes. The automation simplifies what was once a time-consuming task by allowing the report to be generated across all establishments at once.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Improvements](#improvements)

## Introduction

The Class Sales Report Automation project addresses a key inefficiency for businesses managing multiple establishments. Previously, companies had to manually run the product mix report for each establishment separately, a process that became increasingly time-consuming as the number of locations grew. For example, with 19 establishments, the company had to run the report 19 times to collect the necessary data.
This project automates the process by pulling product mix data from the Revel API and compiling it into a single report across all establishments. The data is processed using a DataFrame, filtered to include only the necessary information, and exported to an .xlsx file. The .xlsx format was chosen for its accessibility and ease of use for non-technical users.
To ensure the report retains a clean and uniform design, the output file is linked to a main report file that uses pivot tables for formatting. This approach maintains formatting across each execution, as the output file is overwritten with new data on every run.
The project includes automation on the Windows OS level to open and save the Excel report file, ensuring that the pivot tables are updated. Once the report is generated, it is sent via email using the smtplib library, with a Google account authorized for less secure apps. The project is compiled into an .exe for easy scheduling through Windows Task Scheduler, allowing the report to be generated and distributed at regular intervals.

## Features

- Automatically pulls product mix data from the Revel API for multiple establishments.
- Filters the data based on business requirements and outputs it to an .xlsx file.
- Links the output file to a main report using pivot tables to retain formatting.
- Automates Excel updates and saves on the Windows operating system.
- Sends the final report via email using smtplib.
- Runs as an .exe file, allowing it to be scheduled with Windows Task Scheduler for automatic execution.


## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/BLibs/Revel_Class_Auto_Report.git
    ```
2. Navigate to the project directory:
    ```sh
    cd Revel_Class_Auto_Report
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

Update the `config.py` file in the project directory and define the following variables:

```python
API_KEY = “Add API key here”
EXCEL_PW = "Excel file password goes here"
PATH = r"C:\PATH TO FILE GOES HERE"

# Email based variables
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'Gmail account address would go here (sender)'
EMAIL_PASSWORD = 'Gmail account password goes here'
RECIPIENT_EMAIL = ['Recipient email address goes here (can be a list of multiple recipients)']
```

## Usage 

The script can either be ran directly as a Python file or compiled into an .exe with Pyinstaller
- Run the script to start the automation process:
    ```sh
    python main.py
    ```
- Compile the .exe which can then be ran in any environment.
    ```sh
    pyinstaller --onefile --clean main.py

## Improvements

1. Consider switching from Windows Task Scheduler to a cloud-based job scheduler for greater flexibility and scalability.
2. Implement error handling to ensure that the code is stable in all possible scenarios. 
