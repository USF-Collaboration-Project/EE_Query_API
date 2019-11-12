from datetime import date, timedelta


def clean_date(date_str):
    """
    Clean the date string and return as list
    Args:
        date_str(str): format is YEAR-MONTH-DAY
    Returns:
        date_str(list): make the string to list
    """
    date_str = date_str.split("-")
    return [int(x) for x in date_str]


def get_num_of_days(start, end):
    """
    Returns the number of days in range of start and end
    Args:
        start(string): [YEAR, MONTH, DAY]
        end(string): [YEAR, MONTH, DAY]
    Returns:
        number of days(int): days between [start, end)
    """

    start = clean_date(start)
    end = clean_date(end)
    # print(date(start[0], start[1], start[2]))

    start_date = date(start[0], start[1], start[2])
    end_date = date(end[0], end[1], end[2])

    delta = end_date - start_date       # as timedelta
    
    return delta.days


start = '2018-01-13'
end = '2018-01-11'
print(get_num_of_days(start, end))
