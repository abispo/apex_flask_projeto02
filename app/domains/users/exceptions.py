
from werkzeug.exceptions import HTTPException


class UserProfileNotFoundError(HTTPException):
    def __init__(self, msg='Profile Not Found.'):
        super().__init__(description=msg)
        self.code = 404
