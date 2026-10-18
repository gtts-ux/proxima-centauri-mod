"""Exercise the real -m download path in the published, checksum-pinned app."""
import hashlib
from pathlib import Path
import subprocess
import sys
import tempfile
import zipfile

APP_SHA256 = 'b410ac2c2d76c02c26e3df532229959a199f4a0ac431a400a4d43b834b72e910'
ROOT = Path(__file__).resolve().parents[1]


def run(app, *args):
    result = subprocess.run([sys.executable, str(app/'solar_sim.py'), *args],
                            text=True, capture_output=True, timeout=60)
    if result.returncode or 'Could not run command:' in result.stdout:
        raise RuntimeError(result.stdout+result.stderr)
    return result.stdout


def main():
    archive = Path(sys.argv[1])
    if hashlib.sha256(archive.read_bytes()).hexdigest() != APP_SHA256:
        raise RuntimeError('The downloaded Solar Sim v1.7.0 ZIP checksum does not match.')
    with tempfile.TemporaryDirectory(prefix='proxima install ') as folder:
        # Extract only the known, checksum-pinned official archive.
        with zipfile.ZipFile(archive) as package:
            package.extractall(folder)
        app = Path(folder)/'solar-sim'
        output = run(app, '-mproxima centauri')
        if 'Proxima Centauri mod repository' not in output or 'bundled package' in output:
            raise RuntimeError('Expected a real repository download, not the fallback:\n'+output)
        if (app/'mods/proxima-centauri.json').read_bytes() != (ROOT/'proxima-centauri.json').read_bytes():
            raise RuntimeError('Installed mod differs from the published package.')
        output = run(app, '--offline', '-c', '/proxima centari', '-c', '/orbit',
                     '-c', '/compare "proxima b" "proxima d"', '-c', '/proxima exit', '-c', '/planet')
        for expected in ('Proxima Centauri b', 'Proxima Centauri d', 'Center-to-center distance:', '/neptune'):
            if expected not in output:
                raise RuntimeError('Missing expected command output: '+expected)
    print('PASS: published Solar Sim installed the exact mod from its GitHub repository; activation, orbits, comparison and exit work.')


if __name__ == '__main__':
    main()
