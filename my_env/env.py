from .models import Observation, Action
from .tasks import TASKS
from .grader import grade

class MyEnv:
    def __init__(self):
        self.task = "easy"
        self.done = False

    def reset(self):
        self.done = False
        return Observation(text=TASKS[self.task])

    def step(self, action: Action):
        reward = grade(self.task, action.text)
        self.done = reward == 1.0
        return Observation(text="done"), reward, self.done, {}

    def state(self):
        return {"task": self.task}
