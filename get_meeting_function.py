# AUXILIARY SCRIPT TO GET SCHEDULED MEETINGS IN A LIST

import requests
import json

from values import token

# Header for API calls
headers = {
  'Authorization': f'Bearer {token}'
}

# Request for list of scheduled meetings:
web_current_meetings = "https://webexapis.com/v1/meetings?meetingType=scheduledMeeting"
current_meetings_list = (requests.request("GET", url=web_current_meetings, headers=headers)).json()

#print(current_meetings_list)


# Creates a list with the IDs for all current scheduled meetings
list_of_meeting_ids = []
for n in range(len(current_meetings_list["items"])):
    list_of_meeting_ids.append(current_meetings_list["items"][n]["id"])
print(F'THIS IS THE LIST OF SCHEDULED MEETINGS (meeting Id): {list_of_meeting_ids}')






