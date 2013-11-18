import csv
import random
import sys
import unittest
from datetime import datetime
from dateutil.relativedelta import relativedelta

from highestshareprice import HighestSharePrice

class TestHighestSharePrice(unittest.TestCase):
    """
    Unittests for the HighestSharePrice Class
    """

    def setUp(self):
        self.no_companies = 5
        self.create_csv()

    def month_iterator(self, from_date = "01/01/1990", to_date = "01/11/2013"):
        """

        """
        current_month = datetime.strptime(from_date,"%d/%m/%Y")
        to_month = datetime.strptime(to_date,"%d/%m/%Y")   

        while current_month <= to_month:
            yield current_month
            current_month = current_month + relativedelta(months = +1 )

        return

    def create_csv(self):

        with open('companies_data.csv','wb') as csvfile:
            
            write_data = csv.writer(csvfile, delimiter =',', quotechar='"')
            header = list(["year","month"])
            for icompany in xrange(self.no_companies):
                header.append('Company_%s'%icompany) 
                
            write_data.writerow(header)

            for i in self.month_iterator('01/01/1990','01/11/2013'):
                row = [i.strftime("%Y"),i.strftime("%b")]
                for icomp in xrange(self.no_companies):
                    row.append(random.randint(10,50)*(icomp + 1))
                #print row
                write_data.writerow(row)   

    def test_success(self):
        """
        Test the Working of Module
        """      
        x = HighestSharePrice()    
        self.assertTrue(x.get_highest_share_price())


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestHighestSharePrice)
    unittest.TextTestRunner(verbosity=2).run(suite)            
    sys.exit()