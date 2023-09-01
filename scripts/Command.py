import argparse


class Command():
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='A tool to run chaosmesh and mo-test')

    
    def chaosmesh_arguments(self):     
        """Arguments for chaosmesh"""

        self.parser.add_argument('--chaos', type=str, required=True, help='the name of the yaml file for chaosmesh')
        

    
    def mo_test_arguments(self):    
        """Arguments for mo-test"""

        self.parser.add_argument('--case', type=str, help='the name of the yaml file for mo-test')
        self.parser.add_argument('--ip', type=str, help='the ip of the server')
        self.parser.add_argument('--port', type=str, help='the port of the server')
        self.parser.add_argument('--user', type=str, help='the name of the user')
        self.parser.add_argument('--pwd', type=str, help='the password')       


    def get_arguments(self):
        self.chaosmesh_arguments()
        self.mo_test_arguments()
        args = self.parser.parse_args()
        return args
        
        

    
    
