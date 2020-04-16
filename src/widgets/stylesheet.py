from pathlib import Path


# path
root_path = Path(__file__).parent
filename  = root_path / 'stylesheet.css'

# read
with filename.open() as f:
    stylesheet = f.read()
