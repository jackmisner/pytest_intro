class Reminder():
    def __init__(self, name):
        self.name = name
        self.tasks_list = []
    
    def remind_me_to(self, task):
        self.task = task
        self.tasks_list.append(task)

    def remind(self):
        if len(self.tasks_list) == 0:
            raise Exception("No reminders set!")
        for i in range(len(self.tasks_list)):
            return f'{self.tasks_list[i]}, {self.name}'
    
    def list_tasks(self):
        return self.tasks_list
