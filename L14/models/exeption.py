class UserException(Exception):
    def __init__(self, message="Максимум 10 людей у групу"):
        self.message = message
        super().__init__(self.message)
