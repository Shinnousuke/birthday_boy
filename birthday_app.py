import pandas as pd
import pywhatkit as kit
from datetime import datetime

# Path to your birthday file
FILE_PATH = "C:\\Users\\Admin\\Desktop\\internship_projects\\Birthday_bot\\birthday.txt"

# Scheduled time: 
HOUR = 00
MINUTE = 00
print("Birthday bot on DUTY...")

# Load data and force phone as string
data = pd.read_csv(FILE_PATH, dtype={"phone": str})

# Print loaded data
print("Contacts loaded:")
# print(data)

for _, row in data.iterrows():
    raw_phone = str(row['phone']).strip()

    # Clean up Excel formatting like "9876543210.0"
    if raw_phone.endswith(".0"):
        raw_phone = raw_phone[:-2]

    # Add +91 country code if missing
    if not raw_phone.startswith("+"):
        raw_phone = "+91" + raw_phone

    name = row['name']

    # Birthday message
    message = f"HAPPY BIRTHDAYY {name}! ENJOYY "

    # Show in terminal
    print(f"Message scheduled for: {name} | Phone:********** at {HOUR:02d}:{MINUTE:02d}")
    print(f"Message content: {message}")

    # Schedule the WhatsApp message 
    kit.sendwhatmsg(
        raw_phone,
        message,
        HOUR,
        MINUTE,
        wait_time=20,  # wait 20 seconds on WhatsApp Web before sending
        tab_close=True
    )

print("All birthday messages have been scheduled.")

