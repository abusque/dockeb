import subprocess
import sys

import qng.generator


def _run():
    docker_args = ['docker', *sys.argv[1:]]

    if (len(docker_args) > 1 and
            docker_args[1] == 'run' and
            '--name' not in docker_args):
        # Command is "run" and no name is explicitly
        # specified. Substitute default random name by a Queb name.
        name_generator = qng.generator.QuebNameGenerator()
        name = name_generator.generate(snake_case=True)

        # The argument has to be spliced after the command, since it
        # can't come after the image name or executable (if any) at
        # the end.
        docker_args = [*docker_args[:2], '--name', name, *docker_args[2:]]

    subprocess.call(docker_args)


def main():
    try:
        _run()
    except KeyboardInterrupt:
        sys.exit(1)
