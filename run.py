from scripts.parse import *
from scripts.controller import run_chaosmesh, execute_both
from scripts.Logger import Logger

if __name__ == "__main__":
    args = get_args()
    apply, describe = get_chaosmesh_command(args.chaos)
    result = Logger("experiment")
    result.get_log("log")   

    
    if args.case == None:        
        run_chaosmesh(apply, describe, result)        
    else:
        report = Logger("report")
        report.logger.addHandler(report.file_handler("report"))
        conf, case_command = get_case_command(args)
        execute_both(apply, describe, case_command, conf, result, report)



