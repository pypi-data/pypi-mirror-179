
def create_command(command: str, args: dict):
    command_populated = command.format(command, **args)
    array_command = command_populated.split(' ')
    array_filtered = [i for i in array_command if len(i) > 0 and i != '\n']
    return array_filtered
