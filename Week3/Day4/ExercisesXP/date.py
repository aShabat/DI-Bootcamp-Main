# 5
#
# Use the datetime module to create a function that displays the current date.
#
# Step 1: Import the datetime module
#
# Step 2: Get the current date
#
# Step 3: Display the date

import datetime
from unicodedata import bidirectional

current_date = datetime.date.today()
print(current_date)

# 6
#
# Use the datetime module to calculate and display the time left until January 1st.
# more info about this module HERE
#
# Step 1: Import the datetime module
#
# Step 2: Get the current date and time
#
# Step 3: Create a datetime object for January 1st of the next year
#
# Step 4: Calculate the time difference
#
# Step 5: Display the time difference

goal = datetime.date(current_date.year + 1, 1, 1)
print(f"{(goal - current_date).days} left until January 1st")

# 7
# Create a function that accepts a birthdate as an argument (in the format of your choice), then displays a message stating how many minutes the user lived in his life.


def birthdate_func(birthdate):
    current_time = datetime.datetime.today()
    birthdatetime = datetime.datetime.combine(birthdate, datetime.datetime.min.time())
    print(
        f"The user lived {int((current_time - birthdatetime ).total_seconds() / 60)} minutes"
    )


birthdate_func(datetime.date(1999, 9, 22))
