class commands:
    def __init__(self, __Wincommand: str) -> None:
        try:
            if __Wincommand is None:
                print("[__Wincommand]: Does Not Have A Current Command In Place.")
            self.command = __Wincommand
        except Exception or WindowsError as __error__:
            print(
                str(
                    __error__
                )
            )
    
    def run(self) -> None:
        try:
            __import__('os').system(self.command)
        except Exception or WindowsError as __error__:
            print(
                str(
                    __error__
                )
            )

    def get_output(self) -> None:
        try:
            __import__('subprocess').getoutput(self.command)
        except Exception or WindowsError as __error__:
            print(
                str(
                    __error__
                )
            )
    
