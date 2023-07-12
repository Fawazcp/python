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
