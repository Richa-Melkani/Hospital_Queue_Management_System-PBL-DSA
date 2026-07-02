import heapq
from datetime import datetime


class Patient:
    def __init__(self, patient_id, name, age, disease, severity):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.severity = severity
        self.arrival_time = datetime.now()

    def waiting_minutes(self):
        return int((datetime.now() - self.arrival_time).total_seconds() // 60)

    def effective_priority(self):
        """
        Lower value = Higher Priority
        Every 5 minutes waiting improves priority by 1 level.
        """
        priority = self.severity - (self.waiting_minutes() // 5)

        if priority < 1:
            priority = 1

        return priority

    def __lt__(self, other):
        if self.effective_priority() == other.effective_priority():
            return self.arrival_time < other.arrival_time

        return self.effective_priority() < other.effective_priority()


class PriorityQueue:

    def __init__(self):
        self.queue = []

    def add_patient(self, patient):
        heapq.heappush(self.queue, patient)

    def treat_patient(self):
        if self.queue:
            return heapq.heappop(self.queue)
        return None

    def get_all_patients(self):
        return sorted(self.queue)

    def is_empty(self):
        return len(self.queue) == 0

    def clear(self):
        self.queue.clear()