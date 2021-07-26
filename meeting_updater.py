# THIS IS THE MAIN SCRIPT

import requests
import json

# Make sure to update the toke before the demo
from values import token

# these headers apply for both scheduling and updating meetings
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {token}"
}

# URLs
schedule_meeting = "https://webexapis.com/v1/meetings"

meeting_id = ''
update_meeting = f"https://webexapis.com/v1/meetings/{meeting_id}"


# Schedule a meeting

payload_schedule = json.dumps({
    "title": "Scheduled via Python Script",
    "start": "2021-07-30T21:00:00Z",
    "end": "2021-07-30T21:20:00Z",
    "invitees": [
        {
            "email": ""
        },
        {
            "email": "",
        }
    ],
    "sendEmail": True,
    "hostEmail": ""
})

# Schedule a meeting
input("Press any button to schedule a meeting")

# Sends the POST request to Webex in order to create a new meeting
schedule_meeting = requests.request("POST", url=schedule_meeting, headers=headers, data=payload_schedule)
# print(schedule_meeting.text)

# Convert to JSON format in order to parse
scheduled_meeting_info = schedule_meeting.json()
print(f"Meeting with the ID: {scheduled_meeting_info['id']} has been scheduled")


# PAUSE THE SCRIPT in order to make changes in control hub - change phone number

input_key = input("PLEASE MAKE CHANGES IN WEBEX CONTROL HUB - Press q to quit or any other key to continue: ")
if input_key == "q":
    quit()
else:
    pass



# Parse the result from creating a new meeting, this information will be used to update the meeting
meeting_id = scheduled_meeting_info["id"]
title = scheduled_meeting_info["title"]
password = scheduled_meeting_info["password"]
start = scheduled_meeting_info["start"]
end = scheduled_meeting_info["end"]


# Minimum information required in order to update a meeting, parsed from previous step

payload_updater = json.dumps({
    "title": f"{title}+changing name",
    # "title": f"{title}",
    "password": f"{password}",
    "start": f"{start}",
    "end": f"{end}",
    "enabledAutoRecordMeeting": False,
    "sendEmail": True
})

# update meeting, using a function


def meeting_updater():
    update_meeting_internal = f"https://webexapis.com/v1/meetings/{meeting_id}"
    update_scheduled_meeting = requests.request("PUT", url=update_meeting_internal, headers=headers, data=payload_updater)
    # print(update_scheduled_meeting.text)
    updated_meeting = update_scheduled_meeting.json()
    print(f"The Meeting with ID: {updated_meeting['id']} has  been updated")

# Run the following function in order to update an existing meeting


meeting_updater()