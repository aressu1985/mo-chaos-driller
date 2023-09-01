import subprocess
import time
import multiprocessing
from case_controller import run_case_tool
from Logger import Logger


def run_chaosmesh(apply, describe, result, times=1):    
    interval = 5  
    process_apply = subprocess.Popen(apply, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) 
    data_apply, error_apply = process_apply.communicate()
    result.logger.info(data_apply.strip())
    if error_apply != '':
        result.logger.error(error_apply)

    for i in range(1, times+1):
        process_result = subprocess.Popen(describe, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) 
        des_data, des_error = process_result.communicate()

        extracted = get_extracted(des_data)
        extracted = "The status of chaosmesh: \n{}".format(extracted)
        result.logger.info(extracted)
        if des_error != '':
            result.logger.error(des_error)

        if i < times:
            time.sleep(interval)


def get_extracted(data):
    first_seg = get_segment(data, "Name:", "Labels:")
    second_seg = get_segment(data, "Status:", "Events:")
    extracted = "{}\n{}".format(first_seg, second_seg)
    return extracted


def get_segment(data, start, end):
    start_index = data.find(start)
    end_index = data.find(end)
    if start_index != -1 and end_index != -1:
        seg = data[start_index:end_index].strip()     
    return seg


def execute_both(apply, describe, case_command, conf, result, report):
    times = (conf["circle-times"] * conf["case-interval"] - conf["tool-interval"])//5

    process_case = multiprocessing.Process(target=run_case_tool, args=(conf, case_command, result, report))

    if times > 0:
        process_chaosmesh = multiprocessing.Process(target=run_chaosmesh, args=(apply, describe, result, times))
    else:
        process_chaosmesh = multiprocessing.Process(target=run_chaosmesh, args=(apply, describe, result))
   

    process_case.start()
    time.sleep(conf["tool-interval"])

    process_chaosmesh.start()

    process_case.join()
    process_chaosmesh.join()






def preparation(tool, addr):
    if tool == 'mo-tester':
        prepare_tester()
    elif tool == 'mo-tpch':
        prepare_tpch(addr)
    elif tool == 'mo-tpcc':
        prepare_tpcc()
    else:
        print('Error')
        exit(0)


def prepare_tester():
    
    """tp_cn_0_pod=$(kubectl -n mo-chaos get pod -l matrixorigin.io/component=CNSet -o wide| awk 'NR==2 {print $1}')
    kubectl exec -it $tp_cn_0_pod -n mo-chaos -- /bin/sh<<EOF
    apt-get update
    apt-get install git vim net-tools mysql-client openjdk-8-jdk -y
    git clone https://github.com/matrixorigin/matrixone.git

    
    tp_cn_1_pod=(kubectl -n mo-chaos get pod -l matrixorigin.io/component=CNSet -o wide| awk 'NR==3 {print $1}')
    kubectl exec -it $tp_cn_1_pod -n mo-reg -- /bin/sh<<EOF
    apt-get update
    apt-get install git vim net-tools mysql-client openjdk-8-jdk -y
    git clone https://github.com/matrixorigin/matrixone.git
    
    tp_cn_2_pod=(kubectl -n mo-chaos get pod -l matrixorigin.io/component=CNSet -o wide| awk 'NR==4 {print $1}')
    kubectl exec -it $tp_cn_2_pod -n mo-reg -- /bin/sh<<EOF
    apt-get update
    apt-get install git vim net-tools mysql-client openjdk-8-jdk -y
    git clone https://github.com/matrixorigin/matrixone.git"""


    prepare_commands = [
        
        
        
        
    ]
    for command in prepare_commands:
        subprocess.run(command, shell=True)


def prepare_tpch(addr):
    prepare_commands = [
        "git clone mo-tpch mo-load-data"
        "cd mo-load-data && ./load.sh -h {addr} -c cases/00_from_s3/tpch_10 -r -m -g"
    ]
    for command in prepare_commands:
        subprocess.run(command, shell=True)


def prepare_tpcc(addr):
    prepare_commands = [
        "git clone mo-tpcc mo-load-data"
        "cd mo-load-data && ./load.sh -h {addr} -c cases/00_from_s3/tpcc_10 -r -m -g"
        "cd mo-tpcc"
        "cp props.mo props_10.mo"
        "sed -i '/.*terminals=*/c\terminals=10' props_10.mo"
        "sed -i '/.*warehouses=*/c\warehouses=10' props_10.mo"
        "sed -i 's/tpcc/tpcc_10/g' props_10.mo"
        "sed -i 's/127.0.0.1/172.20.235.194/g' props_10.mo"
        "sed -i '/runMins=*/c\runMins=5' props_10.mo"
    ]
    for command in prepare_commands:
        subprocess.run(command, shell=True)
















