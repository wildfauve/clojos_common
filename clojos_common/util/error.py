class TeamsException(Exception):
    def __init__(self, message="", name="", ctx={}, code=500, klass="", traceback: str = None):
        self.code = 500 if code is None else code
        self.message = message
        self.name = name
        self.ctx = ctx
        self.klass = klass
        self.traceback = traceback
        super().__init__(self.message)

    def error(self):
        return {'error': self.message, 'code': self.code, 'step': self.name, 'ctx': self.ctx}


class TeamServiceCallException(TeamsException):
    pass