from datetime import datetime, timezone, timedelta

# Replace the timestamp value with your actual timestamp
timestamp = 1703830023

# Create a datetime object from the timestamp
utc_datetime = datetime.utcfromtimestamp(timestamp)

# Set the UTC timezone
utc_timezone = timezone.utc
utc_datetime = utc_datetime.replace(tzinfo=utc_timezone)

# Convert to IST timezone
ist_timezone = timezone(timedelta(hours=5, minutes=30))  # IST is UTC+5:30
ist_datetime = utc_datetime.astimezone(ist_timezone)

# Format the datetime as a string
formatted_datetime = ist_datetime.strftime('%Y-%m-%d %H:%M:%S')

print(f'Timestamp in IST: {formatted_datetime}')
