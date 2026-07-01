import json
task=[]
def load_task():
    global task
    try:
        with open("task.json","r") as file:
            task=json.load(file)
    except FileNotFoundError as error:
        task=[]
        print(f"error occured {error}\n")
    except json.JSONDecodeError as error:
        task=[]
        print(f"error occured {error}\n")
def save_task():
    with open("task.json","w") as file:
        json.dump(task,file,indent=4)
def add_task(a,b):
    task.append({"name":a,"status":b})
    save_task()
    print("task added successfully\n")
    list_of_task()
def list_of_task():
    if not task:
        print("no task\n")
    else:
        for n,t in enumerate(task,1):
            print(f"{n}. {t["name"]},{t["status"]}\n")
def update(x):
    if not task:
        print("no task\n")
    elif x<1 or x>len(task):print("out of range\n")
    else:
        status_update=input("enter status of task: ")
        task[x-1]["status"]=status_update
        save_task()
        print("task updated to done successfully\n")
        list_of_task()
def delete_task(z):
    if not task:
        print("no task\n")
    elif z<1 or z>len(task):print("out of range\n")
    else:
        task.pop(z-1)
        save_task()
        print("task deleted succesfully\n")
        list_of_task()
def main():
    load_task()
    while True:
        try:
            user=int(input("welcome to task manager!\n1.Add a task\n2.See all tasks\n3.Change status of task\n4.Delete a task\n5.Exit\n=====>>>"))
            if user==1:
                name=input("enter name of task: ")
                status=input("enter status of task: ")
                add_task(name,status)
            elif user==2:
                list_of_task()
            elif user==3:
                try:
                    list_of_task()
                    number=int(input("enter the number of task you want to update: "))
                    update(number)
                except ValueError:
                    print(f"please enter integer value!\n")
            elif user==4:
                try:
                    list_of_task()
                    num=int(input("enter the number of task you want to delete: "))
                    delete_task(num)
                except ValueError:
                    print(f"please enter integer value\n!")
            elif user==5:
                print("thank you for visiting task manager!\n")
                break
            else:
                print("some error occured\n")
        except ValueError:
            print("please enter integer input!\n")
main()
