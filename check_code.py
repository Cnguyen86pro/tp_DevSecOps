import subprocess

def check_code():
    print(f'Bandit:\n {subprocess.run(['bandit', '*.py'])}')
    print(f'Pip-audit:\n {subprocess.run(['pip-audit'])}')