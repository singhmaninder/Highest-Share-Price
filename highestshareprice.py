###############################################################################
#
#Consider Share prices for a N number of companies given for each month since year     
#1990 in a CSV file.  Format of the file is as below with first line as header.
# 
#Year,Month,Company A, Company B,Company C, .............Company N
#1990, Jan, 10, 15, 20, , ..........,50
#1990, Feb, 10, 15, 20, , ..........,50
#.
#.
#.
#.
#2013, Sep, 50, 10, 15............500
#
# This program is used to List for each Company year and month in which the share price was highest.
#
# Module Name: highestshareprice.py
#
# Author: Maninder Singh
#
# Created: Nov 18, 2013
#
##############################################################################

import csv


class HighestSharePrice(object):
    """
    The methods in this class helps to find list for each Company
    year and month in which the share price was highest.
    """

    def __init__(self):
        self.companies_data = self.read_file()

    def read_file(self):
        """Loads a Memory loadable CSV File to the program, which
           contains stock data of multiple companies since 1990.
        """
        with open('D:\\python_program\\companies_data.csv') as csv_file:
            reader = csv.reader(csv_file)
            data = [row for row in reader]

        return data

    def get_total_rows(self):
        """ get total number of rows of CSV file.
        """

        return (sum(1 for row in self.companies_data)) -1

    def get_total_columns(self):
        """ get total number of columns of CSV file.
        """

        found_columns = False
        try_column = 1

        while found_columns == False:
            try_column += 1
            try:
                identify_column = self.companies_data[0][try_column]
            except:
                found_columns = True
        # decrement column counter to 1 before failed
        column_count = try_column - 1

        return column_count

    def get_highest_share_price(self):
        """ return list for each Company, Year and Month in which
            the share price was highest.
        """

        best_company = []
        company_index = 2
        row_count = self.get_total_rows()
        column_count = self.get_total_columns()

        while company_index <= (column_count):

            # reset the row_index and highest_share for new company.
            row_index = 1
            highest_share = row_index
        
            # Set loop to go through each row
            while row_index <= row_count:
                # Test if data point is above or equal to current max
                # Currently set to use the most recent high point
                if int(self.companies_data[highest_share][company_index]) <= int(self.companies_data[row_index][company_index]):
                    highest_share = row_index
        
                # Move on to next row
                row_index += 1
        
            # Best Company = Company Name + year + month + value
            best_company.append(str(self.companies_data[0][company_index])+": "+str(self.companies_data[highest_share][0]) +", "+str(self.companies_data[highest_share][1])+", "+str(self.companies_data[highest_share][company_index]))
        
            # Move on to next company
            company_index += 1

        return best_company

if __name__ == '__main__':
    share_price = HighestSharePrice()
    results = share_price.get_highest_share_price()
    for result in results:
        print result