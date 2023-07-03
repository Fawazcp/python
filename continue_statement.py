# random is used to shuffle the order
import random
DevOps= ["Linux","AWS","Docker","Kubernetes","Ansible"]
random.shuffle(DevOps)
print(DevOps)
Training=random.choice(DevOps)
print(Training)
for learn in DevOps:
    print(f"{learn} is skill")
    if learn == Training:
        print("########################")
        print(f"{Training} is an essential skill")
        continue
    print(f" This also important to learn")
