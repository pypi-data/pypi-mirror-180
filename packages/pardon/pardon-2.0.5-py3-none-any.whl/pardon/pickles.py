import os

import dill

from . import utility


def save_pickle(object, output_fullpath:str):
    """
    Save the class to the specified output fullpath. 

        Args:
            object : any
                The object to be saved.
            output_fullpath : str
                The output fullpath to where you want your object to be saved. The output fullpath should end with a reference to the filename as a pkl file.
    """
    # ensure the save parameters are correct and if necessary, add the working directory
    utility._check_save_parameters(fullpath=output_fullpath, filetype='.pkl') 

    with open(output_fullpath, 'wb') as out:
        dill.dump(object, out, dill.HIGHEST_PROTOCOL)


def load_pickle(object_fullpath:str):
    """
    Function to load a pkl file.

        Args:
            object_fullpath : str
                The fullpath to your pkl file.

        Returns:
            (any) : Returns the loaded pkl object.
    """
    # ensure the model exists
    if not os.path.exists(object_fullpath):
        raise FileNotFoundError(f'The model file {object_fullpath} does not exist. Ensure the full path is correct and try again.')
    try:
        # load the model
        obj = dill.load(open(object_fullpath, 'rb'))
    except Exception as e:
        # an error means the class has not opened correctly, set model to None
        raise Exception(f'The object "{object_fullpath}" has failed to load. The following error was given: {e}')

    return obj

    