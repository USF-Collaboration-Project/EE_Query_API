from datetime import date, timedelta

def get_num_of_days(start, end):

    start = start.split("-")
    start = [int(x) for x in start]
    end = end.split("-")
    end = [int(x) for x in end]
    print(date(start[0], start[1], start[2]))
  
    start_date = date(start[0], start[1], start[2])
    end_date = date(end[0], end[1], end[2])

    delta = end_date - start_date       # as timedelta
    print(delta.days)
    # for i in range(delta.days):
    #     day = start + timedelta(days=i)
    #     print(day)


start = '2018-01-13'
end = '2018-01-11'
get_num_of_days(start, end)
