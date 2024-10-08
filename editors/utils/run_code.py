import subprocess


def run_javascript_code(code):
    with open("/tmp/script.js", "w") as file:
        file.write(code)

    result = subprocess.run(
        [
            "docker",
            "container",
            "run",
            "--rm",
            "-v",
            "/tmp:/code",
            "editor",
            "node",
            "/code/script.js",
        ],
        capture_output=True,
        text=True,
        timeout=10,  # to prevent infinite loop
    )

    return result.stdout if result.returncode == 0 else result.stderr


def run_python_code(code):
    with open("/tmp/script.py", "w") as file:
        file.write(code)

    result = subprocess.run(
        [
            "docker",
            "container",
            "run",
            "--rm",
            "-v",
            "/tmp:/code",
            "editor",
            "python",
            "/code/script.py",
        ],
        capture_output=True,
        text=True,
        timeout=10,
    )

    return result.stdout if result.returncode == 0 else result.stderr
