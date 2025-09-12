#The datetime module in Python provides classes for working with dates and times..

from datetime import datetime, timedelta

now = datetime.now()
print("Now:", now)

# Formatting date
print("Formatted:", now.strftime("%Y-%m-%d "))

# Expiry after 7 days
expiry = now + timedelta(days=7)
print("Expiry:", expiry)

# String → datetime
dt = datetime.strptime("2025-09-12", "%Y-%m-%d")
print("Parsed Date:", dt)
