import yaml

from . import utility


def load_yaml(filepath) -> dict:
    """
    Open a yaml file.

        Args:
            filepath : str
                Filepath of your yaml file.

        Returns:
            (dict) : Returns a dict object with the contents of your yaml file.
    """
    # confirm the correct filetypes are used
    filepath = utility._check_save_parameters(fullpath=filepath, filetype=['.yml', '.yaml']) 
    with open(filepath,'r') as file:
        config = yaml.safe_load(file)

    return config


    