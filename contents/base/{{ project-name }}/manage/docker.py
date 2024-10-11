import subprocess


def docker_build():
    print("Creating docker image")
    subprocess.run(["docker", "build", "-t", "{{ project-name }}", "."])


def docker_run():
    print("Running docker image")
    {% if "FastAPI" in transport or "gRPC" in transport -%}
    command = [
        "docker", "run",
        "-p", "8080:8080",  # Port mapping
        "-it", "{{ project-name }}"
    ]
    subprocess.run(command)
    {% else -%}
    subprocess.run(["docker", "run", "-it", "{{ project-name }}"])
    {% endif %}