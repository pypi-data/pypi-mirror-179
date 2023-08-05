class log:
    def __init__(self, log: any) -> None:
        try:
            print(
                "Please Use: `log(<log>).<any>`"
            )
            self.log = log
        except Exception as __error__:
            print(
                str(
                    __error__
                )
            )

    def error(self, fileName) -> None:
        try:
            with open(f'{fileName}', "w") as file_:
                file_.write(
                    f'{self.log}'
                )
                file_.close()
        except Exception as __error__:
            print(
                str(
                    __error__
                )
            )

    def _content(self, __fileName: str) -> None:
        try:
            with open(f'{__fileName}', 'w') as file_:
                file_.write(f'{self.log}')
                file_.close()
        except Exception as __error__:
            print(
                str(
                    __error__
                )
            )