from config import *
from email_file import send_report_email
from file_handling import handle_file
from get_data import get_data, get_dates
import pandas as pd
import time


''' Project is using Revel API to pull data. We are targeting the product mix endpoint, which shows a
    breakdown of sales across various items, and their corresponding classes. The main issue that is being
    solved is that there is no way to run this report against multiple establishments at once, making this
    a time consuming process as the number of establishments grows. In this case, we are working with 19 
    establishments, which previously required the company to run this report 19 times to pull this data.
    
    Once the data is collected, we are populating a dataframe object and filtering it down to only what
    we need. That dataframe is then turned into an .xlsx file to begin shaping the report. 
    
    .xlsx files were chosen because they require no additional costs and are easy to work with for a
    non-technical audience. The output.xlsx file is then linked to the main report file, which is using 
    pivot tables to add some design to the data, making it easier to read. 
    
    This linkage was necessary because we are going to be overwriting the output file on each execution,
    which would strip the file of any formatting. By using a linkage and then populating a pivot table with
    the data, we retain all formatting and can automate this process while keeping uniformity.
    
    Handling of the file required automation on the OS level, in this case Windows. To get Excel to update
    the data in the report file, it needs to be opened and saved. 
    
    Once the file has been handled by the OS, smtplib is used to email the file to the recipients. This 
    is coupled with a Google email account authorized for use in 'less secure apps'. The entire process
    is compiled down to an .exe so it can then be scheduled with task scheduler to run at the required times.'''


# Main script function
def main():
    # Populate the dataframe
    dataframe = get_data()
    # Output data to console for testing
    print(dataframe)
    # Export to Excel file
    output_path = 'data_files/output.xlsx'
    with pd.ExcelWriter(output_path) as writer:
        dataframe.to_excel(writer, index=False)

    # Handle the file twice (does not seem to update the data the first time Excel is opened)
    handle_file(PATH)
    time.sleep(5)
    handle_file(PATH)
    time.sleep(10)
    # Send the file via email to the listed recipients
    send_report_email(PATH, f"{ABR_EST_NAME} Weekly Class File " + get_dates(1))


if __name__ == "__main__":
    main()
