from Command import Command
from case_controller import command_for_case
import yaml


def get_args():
    cmd = Command()
    args = cmd.get_arguments()
    return args


def get_chaosmesh_command(chaos):
    with open(chaos, 'r') as file:
        data = yaml.safe_load(file)
    name = data['metadata']['name']
    apply = "kubectl apply -f {}".format(chaos)
    describe = "kubectl describe podchaos {} -n chaos-mesh".format(name)  
    return apply, describe

def get_case_command(args):
    conf, case_command = command_for_case(args.case, args.ip, args.port, args.user, args.pwd)
    return conf, case_command


