import os
import subprocess
import venv

# 1. Create the virtual environment
venv_dir = '.venv'
venv.create(venv_dir, with_pip=True, prompt='junkdrawer')

# 2. Identify the correct Python path (handles Windows vs Unix)
if os.name == 'nt':  # Windows
    venv_python = os.path.join(venv_dir, 'Scripts', 'python.exe')
else:                # macOS/Linux
    venv_python = os.path.join(venv_dir, 'bin', 'python')

# Upgrade pip
try:
    subprocess.run(
        [venv_python, "-m", "pip", "install", "--upgrade", "pip"],
        check=True
    )
    print("Successfully upgraded pip...")
except subprocess.CalledProcessError as e:
    print(f"Installation failed: {e}")


# 3. Install from requirements.txt
try:
    subprocess.run(
        [venv_python, "-m", "pip", "install", "-r", "requirements.txt"],
        check=True
    )
    print("Successfully installed requirements...")
except subprocess.CalledProcessError as e:
    print(f"Installation failed: {e}")

try:
    subprocess.run(
        [venv_python, "-m", "ipykernel", "install", "--user", "--name", "junkdrawer", "--display-name", "junkdrawer"],
        check=True
    )
    print("Successfully installed kernelspec...")
except subprocess.CalledProcessError as e:
    print(f"Installation failed: {e}")

