from rich import print
from datetime import datetime

def get_time() -> str:
    return datetime.now().strftime('%m-%d %H:%M:%S')

class Logger:
    def success(self, msg: str) -> None:
        print(f'[bright_black]{get_time()}[/bright_black] [bold bright_white on chartreuse4] SUCCESS [/bold bright_white on chartreuse4] {msg}')

    def warning(self, msg: str) -> None:
        print(f'[bright_black]{get_time()}[/bright_black] [bold bright_white on gold3] WARNING [/bold bright_white on gold3] {msg}')

    def error(self, msg: str) -> None:
        print(f'[bright_black]{get_time()}[/bright_black] [bold bright_white on dark_red]  ERROR  [/bold bright_white on dark_red] {msg}')

    def debug(self, msg: str) -> None:
        print(f'[bright_black]{get_time()}[/bright_black] [bold bright_white on purple4]  DEBUG  [/bold bright_white on purple4] {msg}')

    def log(self, msg: str) -> None:
        print(f'[bright_black]{get_time()}[/bright_black] [bold bright_white on gray23]   LOG   [/bold bright_white on gray23] {msg}')

logger = Logger()
