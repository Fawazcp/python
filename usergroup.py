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
# Condition to check the group exist or not, add if the group does not exist

exitcode=os.system("grep devops /etc/group")
if exitcode !=0:
    print("Group devops does not exist. Adding it")
    print("##############################################")
    print()
    os.system("groupadd devops")
else:
    print("Group already exist, skipping it")
    print("####################################")
    print()

# add users the group
for user in userlist:
    print(f"Adding user {user} in the devops group")
    print("##########################################")
    print()
    os.system(f"usermod -G devops {user}")
