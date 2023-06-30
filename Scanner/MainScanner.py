from Common.Logger.Logger import logger_info_decorator
from Scanner.Abstracts.IScannerEverything import IScannerEverything
from Scanner.Abstracts.IScannerSpecific import IScannerSpecific


class MainScanner(IScannerEverything):

    def __init__(self,
                 specific_scanners: list[IScannerSpecific],
                 specific_everything_scanners: list[IScannerEverything]):
        self.name = 'main'
        self.specific_everything_scanners = specific_everything_scanners
        self.specific_scanners = specific_scanners

    @logger_info_decorator
    def scan(self, **kwargs) -> list[str]:
        scanner_result = []

        for scanner in self.specific_everything_scanners:
            arguments = kwargs[scanner.name]
            scanner_result += scanner.scan(**arguments)

        for scanner in self.specific_scanners:
            scanner_result = scanner.scan(scanner_result)

        return scanner_result
