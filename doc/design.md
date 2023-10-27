# 架构设计目标
1.故障注入启动，暂停，恢复环境操作（chaosmesh已具备该功能，如果同时运行case，工具需要设计case的启动/停止） 

2.yaml定义故障类型，故障注入方式，多种类型故障混合，定时任务，指定节点等故障场景（使用chaosmesh工具） 

3.故障注入同时指定执行case，也可以只注入故障不执行case（只注入故障，是否能正常拉起pod），case可以指定使用目前已有的case工具，自定义case yaml文件，该yaml文件可以指定运行的sql，执行次数，迭代周期

4.日志记录包含故障注入的开始时间，结束时间，故障类型，故障状态，故障类型相关的参数等；case中每条sql执行开始时间，结束时间，sql语句，sql执行成功还是失败状态

5.检测mo各节点状态，定时检测？restart？--chaosboard是否满足？

6.统计case执行成功/失败结果，case执行时间report --性能监控，记录数据入库（后期再考虑）

7.mo环境准备，检测是否启动，否则自动启动环境

# 架构图
![image](https://github.com/aressu1985/mo-chaos-driller/assets/113406637/1cd81117-baa9-419e-b16a-795a087b92bc)


# 各模块内部功能
![image](https://github.com/aressu1985/mo-chaos-driller/assets/113406637/e4db6bf1-b2d8-4ec9-a175-5d7aa6163cb7)

