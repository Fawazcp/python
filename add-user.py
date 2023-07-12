#!/usr/bin/python3

import os
userlist=["fawaz","aws","python"]

print("Adding users to the script")
print("############################")

# loop to add users from userlist
for user in userlist:
    exitcode=os.system(f"id {user}")
    if exitcode != 0:
        print(f"User {user} does not exist. Adding it")
        print("###########################################")
        print()
        os.system(f"useradd {user}")
    else:
        print("User already exist, skipping it")
        print("#################################")
        print()

