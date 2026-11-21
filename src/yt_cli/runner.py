import subprocess

from dataclasses import dataclass
from typing import List, Callable

@dataclass
class RunnerResult:
    stdout: str
    stderr: str
    returncode: int

class Runner:
    def __init__(self, executable: str = 'yt-dlp'):
        self.executable = executable

    def run(self, commands: List[str]) -> RunnerResult:
        result = subprocess.run(
            [self.executable, *commands],
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
    
    def run_stream(self, commands: List[str], on_line: Callable[[str], None] | None = None) -> RunnerResult:
        process = subprocess.Popen(
            [self.executable, *commands],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding='utf-8',
            errors='replace',
            bufsize=1,
        )

        output_lines: List[str] = []
        if process.stdout:
            for line in process.stdout:
                clean_line = line.strip()
                output_lines.append(clean_line)
                if on_line:
                    on_line(clean_line)

        process.wait()
        full_output = "\n".join(output_lines)

        return RunnerResult(
            stdout=full_output if process.returncode == 0 else '',
            stderr='' if process.returncode == 0 else full_output,
            returncode=process.returncode,
        )