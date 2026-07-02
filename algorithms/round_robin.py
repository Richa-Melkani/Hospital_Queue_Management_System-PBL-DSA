class RoundRobinScheduler:
    def __init__(self):
        self.doctors = [
            "Dr. Sharma",
            "Dr. Mehta",
            "Dr. Khan",
            "Dr. Singh"
        ]
        self.current_index = 0

    def assign_doctor(self):
        doctor = self.doctors[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.doctors)
        return doctor