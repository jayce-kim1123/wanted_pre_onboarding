"""Error
    Note:
        CustomError: 사용자 지정 에러, 아무 메세지도 입력 되지 않으면 NO_MESSAGE 와 400 status 출력
        NoneObjectError: DB에서 객체를 찾을 수 없을 때 발생하는 에러, CustomError를 상속함 
        NoneFieldError: DB에서 필드를 찾을 수 없을 때 발생하는 에러, CustomError를 상속함 
        KeyError: 엔드포인트에서 잘못된 Key값이 전달됐을 때 발생하는 에러, CustomError를 상속함 
    Todo:
        1. Notion 문서 작성 (고객포털-작업공간-Common)
"""

class CustomError(Exception):
    def __init__(self, message='NO_MESSAGE', status=400):
        self.message = message
        self.status = status
        super().__init__(self.message, self.status)

class NoneObjectsError(CustomError):
    def __init__(self, message='DOES_NOT_EXIST', status=404):
        super().__init__(message, status)

class NoneFieldError(CustomError):
    def __init__(self, message='FIELD_IS_NONE', status=404):
        super().__init__(message, status)

class KeyError(CustomError):
    def __init__(self, message='INVALID_KEY', status=400):
        super().__init__(message, status)