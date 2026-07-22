import json
class Task_manager:
    def __init__(self) -> None:
        self.task=[]
    def load_task(self):
        try:
            with open("task.json","r") as file:
                self.task=json.load(file)
        except FileNotFoundError as error:
            self.task=[]
            print(f"error occured {error}\n")
        except json.JSONDecodeError as error:
            self.task=[]
            print(f"error occured {error}\n")
    def save_task(self):
        with open("task.json","w") as file:
            json.dump(self.task,file,indent=4)
    def add_task(self,a,b):
        self.task.append({"name":a,"status":b})
        self.save_task()
        print("task added successfully\n")
        self.list_of_task()
    def list_of_task(self):
        if not self.task:
            print("no task\n")
        else:
            for n,t in enumerate(self.task,1):
                print(f'{n}. {t["name"]},{t["status"]}\n')
    def update(self,x):
        if not self.task:
            print("no task\n")
        elif x<1 or x>len(self.task):print("out of range\n")
        else:
            status_update=input("enter status of task: ")
            self.task[x-1]["status"]=status_update
            self.save_task()
            print("task updated to done successfully\n")
            self.list_of_task()
    def delete_task(self,z):
        if not self.task:
            print("no task\n")
        elif z<1 or z>len(self.task):print("out of range\n")
        else:
            self.task.pop(z-1)
            self.save_task()
            print("task deleted succesfully\n")
            self.list_of_task()
    def main(self):
        self.load_task()
        while True:
            try:
                user=int(input("welcome to task manager!\n1.Add a task\n2.See all tasks\n3.Change status of task\n4.Delete a task\n5.Exit\n=====>>>"))
                if user==1:
                    name=input("enter name of task: ")
                    status=input("enter status of task: ")
                    self.add_task(name,status)
                elif user==2:
                    self.list_of_task()
                elif user==3:
                    try:
                        self.list_of_task()
                        number=int(input("enter the number of task you want to update: "))
                        self.update(number)
                    except ValueError:
                        print(f"please enter integer value!\n")
                elif user==4:
                    try:
                        self.list_of_task()
                        num=int(input("enter the number of task you want to delete: "))
                        self.delete_task(num)
                    except ValueError:
                        print(f"please enter integer value\n!")
                elif user==5:
                    print("thank you for visiting task manager!\n")
                    break
                elif 1>user>5:
                    print("please enter numbers of option between 1 to 5")
            except ValueError:
                print("please enter integer input!\n")
manager=Task_manager()
manager.main()