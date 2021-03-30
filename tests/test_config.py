import pytest

class NotInRange(Exception):
    def __init__(self ,message="value out of range"):
        self.message = message
        super().__init__(self.message)

    pass


def test_generic():
    a=5
    with pytest.raises(NotInRange):
        if a not in range(10,20):
            raise NotInRange
