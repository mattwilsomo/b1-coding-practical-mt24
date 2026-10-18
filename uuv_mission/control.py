class PDController:
    def __init__(self, k_p, k_d):
        self.k_p = k_p
        self.k_d = k_d
        self.previous_error = 0

    def call(self, reference, observation):
        error = reference - observation
        action = self.kp * error + self.kd * (error - self.previous_error)
        self.previous_error = error
        return action