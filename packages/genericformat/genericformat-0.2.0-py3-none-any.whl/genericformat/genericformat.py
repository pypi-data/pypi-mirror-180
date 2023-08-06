import subprocess
import tempfile
from pathlib import Path


def format(formatter: str, code: str):
    file = tempfile.NamedTemporaryFile(prefix="codeformat")
    file.write(code.encode())
    file.seek(0)

    # cmd = ([*formatter.split(), file.name],)

    proc = subprocess.Popen(
        [*formatter.split(), file.name],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    if proc.wait() == 0:
        return Path(file.name).read_text()
        # return file.file.read().decode()
