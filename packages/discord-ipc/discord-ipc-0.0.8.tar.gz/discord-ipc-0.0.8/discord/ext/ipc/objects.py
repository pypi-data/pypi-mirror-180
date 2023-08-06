class ResponseObject:
    
    def __init__(self, data: dict):
        for name, value in data.items():
            setattr(self, name, value)