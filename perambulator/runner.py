#Reece Payne 2016
#The main runner object.

"""
This module contains the main runner class.
"""

#Import JSON loader
import json
from perambulator import apiConfigLoader

class runner():
    """
    This class is the main orchestration object for running all the other tests.

    Members:

    apiConfiguration -- An instance of apiConfigLoader with the loaded api
    Config.

    name -- The name of this object.
    """
    #Holds the apiConfiguration.
    apiConfiguration = ""
    name = ""

    def __init__(self):

    def loadConfig(apiConfigObject, self):
        """
        Takes a given configuration object (pre parsed from JSON, or built in
        python directly) and loads it in to an apiConfigObject.

        Keyword arguments:

        apiConfigObject -- A python dict with the API config.
        """
        self.apiConfiguration = apiConfigLoader(apiConfigObject)

    def loadConfigFromJSON(apiConfigObjectJson, self):
        """
        A variation of the loadConfig method that can directly take a JSON file
        and load it in to an instance of the apiConfigLoader class.
        Keyword arguments:

        apiConfigObjectJSON -- JSON containing the API config.
        """

        json.loads(apiConfigObjectJSON)
