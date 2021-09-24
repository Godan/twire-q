

from free_answer.models.question import Question


class FreeAnswerApplication:
    def start_aggregate(self, question: Question) -> None:
        question.start_aggregate()

    def end_aggregate(self, question: Question) -> None:
        question.end_aggregate()