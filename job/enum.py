from enum import Enum
class Status(Enum):

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)