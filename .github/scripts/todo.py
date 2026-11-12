class Task:
    def __init__(self, title, status="ToDo"):
        self.title = title
        self.status = status
        self.completed = status == "Done"

    def mark_completed(self):
        self.completed = True
        self.status = "Done"

    def __repr__(self):
        return f"{self.title} - {self.status}"

    def __str__(self):
        return f"Task: {self.title}, Status: {self.status}"


class TaskPool:
    def __init__(self):
        self.tasks = []

    def populate(self):
        titles = [
            "Research user needs",
            "Create wireframes",
            "Review accessibility",
            "Build prototype",
            "Test navigation",
            "Review feedback",
        ]

        self.tasks = [Task(title) for title in titles]

        for task in self.tasks[:3]:
            task.mark_completed()

    def add_task(self, task):
        self.tasks.append(task)

    def get_open_tasks(self):
        return [task for task in self.tasks if task.status == "ToDo"]

    def get_done_tasks(self):
        return [task for task in self.tasks if task.status == "Done"]


def main():
    pool = TaskPool()
    pool.populate()

    print("ToDo Tasks:")
    for task in pool.get_open_tasks():
        print(task.title)

    print("Done Tasks:")
    for task in pool.get_done_tasks():
        print(task.title)


if __name__ == "__main__":
    main()