import subprocess

from dataclasses import dataclass
from typing import List

@dataclass
class RunnerResult:
    stdout: str
    stderr: str
    returncode: int

class Runner:
    def run(self, commands: List[str]) -> RunnerResult:
        result = subprocess.run(
            ['yt-dlp'] + commands,
            capture_output=True,
            text=True,
            encoding='utf-8',
            shell=False
        )

        if result.returncode != 0:
            return RunnerResult(
                stdout='',
                stderr=str(result.stderr),
                returncode=result.returncode
            )
        
        return RunnerResult(
            stdout=result.stdout,
            stderr='',
            returncode=result.returncode
        )