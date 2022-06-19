# TO CONVERT DAYS INTO YEARS, MONTHS & DAYS
months = {
    'January': 31,
    'February': 28,
    'March': 31,
    'April': 30,
    'May': 31,
    'June': 30,
    'July': 31,
    'August': 31,
    'September': 30,
    'October': 31,
    'November': 30,
    'December': 31
}


def days_to_date(total_days):
    is_leap = False
    count = 0
    r_days = total_days
    d = 0
    month = 0

    while True:
        year_days = 365
        count += 1
        if count % 4 == 0 and ((not count % 100 == 0) or count % 400 == 0):
            year_days = 366
            is_leap = True
        r_days -= year_days
        if r_days <= 0:
            if r_days == 0:
                print('Years ', count)
                quit()
            r_days += year_days
            break
        else:
            is_leap = False

    for k, v in months.items():
        if is_leap and k == 'feb':
            v = 29
        d = d + v
        month = k

        if d == r_days:
            r_days = 0
            break
        elif d > r_days:
            r_days = r_days - d + v
            break

    print(total_days, " = ", count - 1, ' years  ', month, "  ", r_days, ' days')


def days_bwn_dates(date1, date2):
    pass

def date_after_days(date,days):
    pass

if __name__ == '__main__':
    days_to_date(int(input("Enter the total days: ")))