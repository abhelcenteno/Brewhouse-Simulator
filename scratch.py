from datetime import datetime, timedelta

start = datetime.now()
gap = timedelta(minutes=100)
end = start + gap

print(end > start)