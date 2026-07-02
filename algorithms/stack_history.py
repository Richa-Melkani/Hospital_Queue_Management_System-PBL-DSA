class TreatmentHistory:

    def __init__(self):
        self.stack = []

    def add_record(self, patient):
        self.stack.append(patient)

    def get_last_patient(self):

        if self.stack:
            return self.stack[-1]

        return None

    def get_all_history(self):
        return list(reversed(self.stack))

    def clear(self):
        self.stack.clear()

    def is_empty(self):
        return len(self.stack) == 0