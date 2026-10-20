def convert_number_to_month(month_number):
    MONTH_LIST = ["Januari", "Februari", "Mars", "April","Maj", "Juni", "Juli",
                   "Augusti", "September", "Oktober", "November", "December"]
    return(MONTH_LIST[month_number-1])

def convert_number_to_month_english(month_number):
    MONTH_LIST = ["January", "February", "March", "April","May", "June", "July",
                   "August", "September", "October", "November", "December"]
    return(MONTH_LIST[month_number-1])