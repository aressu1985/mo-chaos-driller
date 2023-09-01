from scripts.Logger import Logger
import datetime
import time
import subprocess
import os

def run_case_tool(result, report):
    command = "./run.sh -n /root/matrixone/test/distributed/cases -m run -g"   
    times = 3

    for i in range(1, times+1):      
        subprocess.Popen("cd ../mo-tester", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)      
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) 
        subprocess.Popen("cd ../chaos_injection_tool/", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdout, stderr =  process.communicate()
        
        with open("../mo-tester/report/report.txt", "r") as file:
            report_content = file.read().strip()
           
        report_content = "The result of this case tests: \n{}".format(report_content)

        result.logger.info(report_content)
        report.logger.info(report_content)
    
          

if __name__ == "__main__":
    result = Logger("experiment")
    result.get_log("log")   
    report = Logger("report")
    report.logger.addHandler(report.file_handler("report"))
    run_case_tool(result, report)



   
