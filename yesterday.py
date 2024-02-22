from datetime import datetime, timedelta
for days in range
    yesterday = datetime.today() - timedelta(days=1)
    print(yesterday.strftime('%Y%m%d'))
    today = datetime.today().strftime('%Y%m%d')
    print(type(today))