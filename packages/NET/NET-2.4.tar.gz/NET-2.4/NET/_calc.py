class calc:
    def __init__(self, val: int) -> None:
        try:
            self.number = val
        except Exception as __error__:
            print(
                str(
                    __error__
                )
            )
    def add_one(self) -> None:
        try:
            return self.number + 1
        except Exception as __error__:
            print(
                str(
                    __error__
                )
            )
    
    def sub_one(self) -> None:
        try:
            return self.number - 1
        except Exception as __error__:
            print(
                str(
                    __error__
                )
            )
    def div(self, val: int) -> None:
        try:
            return self.number / val
        except Exception as __error__:
            print(
                str(
                    __error__
                )
            )
    def multiply(self, val: int) -> None:
        try:
            return self.number * val
        except Exception as __error__:
            print(
                str(
                    __error__
                )
            )
    def is_equal(self, val: int) -> None:
        try:
            is_equal = None
            if self.number == val:
                is_equal = True
            else:
                is_equal = False
            return is_equal
        except Exception as __error__:
            print(
                str(
                    __error__
                )
            )