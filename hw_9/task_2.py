from task_1 import Trainee

class HardworkingTrainee(Trainee):
    def do_homework(self) -> None:
        """Increases score by 2"""
        self.score += 2

class AuditTrainee(Trainee):
    def is_passing(self) -> bool:
        return True

class Cohort:
    def __init__(self, title: str, trainees: list[Trainee] = []):
        self.title = title
        self.trainees = trainees

    def add_trainee(self, trainee: Trainee) -> None:
        self.trainees.append(trainee)

    def conduct_lecture(self) -> None:
        for trainee in self.trainees:
            trainee.visit_lecture()
    def get_passing_students(self) -> list[Trainee]: 
        return [trainee for trainee in self.trainees if trainee.is_passing()]
