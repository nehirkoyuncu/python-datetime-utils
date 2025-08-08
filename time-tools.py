from datetime import datetime, timedelta
def format_date(timestamp,datetime_format):
    date = datetime.datetime.utcfromtimestamp(timestamp)
    return date.strftime(datetime_format)


def calculate_landing_time(rocket_launch_dt, travel_duration):
    landing_time = rocket_launch_dt + timedelta(days=travel_duration)
    return landing_time.strftime("%d-%m-%Y")


def days_until_delivery(expected_delivery_dt, current_dt):
    time_remaining = expected_delivery_dt - current_dt
    return time_remaining.days
