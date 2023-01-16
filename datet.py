class Datet:

    def __init__(self, stocks, start_date, end_date):
        self.stocks = stocks
        self.start_date = start_date
        self.end_date = end_date
        
    def select_stock(self, selected_stock):
        self.selected_stock = selected_stock
        
    def set_period(self, n_years):
        self.n_years = n_years
        self.period = n_years * 365

# A class containing the functions to make the predicted date more accurate
# Attributes:
    # stocks : number of stocks implemented to the prediction.
    # start_date : start date to see the 2015 date.
    # end_date : end date to make the date atleast 2 days before than today.

# Methods:
   # select_stock : makes the selected stock date from yahoo finance more acurate.
   # set_period : makes the slider to calculate the date more acurate.

