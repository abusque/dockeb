import subprocess
import sys

import qng.generator


def _get_docker_args():
    docker_args = ['docker', *sys.argv[1:]]

    if len(docker_args) <= 1:
        # No sub-command, ignore.
        return docker_args

    subcommand = docker_args[1]
    if subcommand not in ['create', 'run']:
        # Doesn't create a container, ignore.
        return docker_args

    if '--name' in docker_args:
        # Name already explicitly specified, ignore.
        # FIXME: '--name' could actually be part of the arguments to
        # the command to execute inside the container (given after the
        # image name), in which case we still want to generate a Keb
        # name.
        return docker_args

    # Substitute default random name by a Queb name.
    name_generator = qng.generator.QuebNameGenerator()
    name = name_generator.generate(snake_case=True)

    # The argument has to be spliced after the command, since it
    # can't come after the image name or executable (if any) at
    # the end.
    docker_args = [*docker_args[:2], '--name', name, *docker_args[2:]]

    return docker_args


def _run():
    docker_args = _get_docker_args()

    subprocess.call(docker_args)


def main():
    try:
        _run()
    except KeyboardInterrupt:
        sys.exit(1)
