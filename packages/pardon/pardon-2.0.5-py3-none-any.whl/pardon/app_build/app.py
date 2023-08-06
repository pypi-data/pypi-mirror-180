import os, sys


def __get_calling_script_name() -> str:
    """Returns the directory name of the original calling script"""

    from inspect import getsourcefile

    return os.path.dirname(getsourcefile(lambda:0))


def app():
    '''
    Launches a streamlit graphical user interface for interacting with pardon data transformation, machine learning, and data visualisation.
    '''
    # this launches the streamlit app
    from streamlit import cli as stcli

    dir = __get_calling_script_name()
    fullpath = os.path.join(dir, 'poc_app.py')

    sys.argv = ["streamlit", "run", fullpath]
    sys.exit(stcli.main())