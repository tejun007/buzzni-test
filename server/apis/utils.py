def get_start_limit_dates(start_datetime, limit_datetime):
    start_date = int(start_datetime.strftime('%Y%m%d'))
    limit_date = int(limit_datetime.strftime('%Y%m%d'))
    return start_date, limit_date


def get_start_limit_times(start_datetime, end_datetime):
    start_time = int('{:d}{:02d}'.format(start_datetime.hour, start_datetime.minute))
    limit_time = int('{:d}{:02d}'.format(end_datetime.hour, end_datetime.minute))
    return start_time, limit_time
