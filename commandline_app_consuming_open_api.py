#########This application uses python's requests HTTP Library#############
#########The Library can be installed by running pip install requests#####
import requests
print("======================================================================================")
print("Welcome! With this application, you will pull events about an Organisation's repo in Github")
print("====================================================================================== \n")
org = input("Please Enter Github Organisation e.g. andela : >> ")
if org !=  "":
    print("verifying organisation on Git hub.......")
    resp = requests.get("https://api.github.com/orgs/" + org + "/events")
    if resp.status_code != 200:
        print("Error: " +org + " is unknown to github")
        exit()
    else:
        print("Organisation OK!... \n Processing your events...\n")
        num_recent_events = input("Please Enter the required number of recent Events: \n")
        all_events = resp.json()
        if num_recent_events.isdigit():
            num = 0
            required_events = []
            while num < int(num_recent_events):
                required_events.append(all_events[num])
                num += 1
        else:
            print("The number of recent events must be an integer. \n")
            exit()
        print("==================================================================")
        print("========= " + org.upper() + " " + num_recent_events + " Most Recent Events =====================")
        print("==================================================================")
        for out_dict in required_events:
            for key,value in out_dict.items():
                if isinstance(value,dict):
                    print("=============================================")
                    print(key.upper() + " Details")
                    print("=============================================")
                    for ke,va in value.items():
                        print(str(ke) + " : " + str(va))
                else:
                    print(str(key) + " : "+ str(value))
else:
    print(" Please input a valid organisation ")