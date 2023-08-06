# -*- coding:utf-8 -*-
# @Author: huang-jy
import os
import time
import pytest
import platform
# import threadpool

"""
eg:
class RunUsed:
    kMainPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__).replace('\\', '/')))
    kReportsPath = kMainPath + '/reports'
    kCurEnv = "test"
    
usage:
from pytest_jar_yuan import Ctrl, RunControl
CtrlVar.set_main_path(RunUsed.kMainPath)
CtrlVar.set_reports_path(RunUsed.kReportsPath)
CtrlVar.set_current_environment(RunUsed.kCurEnv)
"""


class CtrlVar:
    kMainPath = ""
    kReportsPath = ""
    kProjectName = ""
    kCurrentEnvironment = ""
    kTimestamp = time.strftime('%Y_%m_%d_%H%M%S', time.localtime())
    kPycharmPort = "66342"

    @staticmethod
    def set_main_path(new_main_path):
        # CtrlVar.kMainPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__).replace('\\', '/')))
        # CtrlVar.kProjectName = CtrlVar.kMainPath.split('/')[-1]
        CtrlVar.kMainPath = new_main_path
        CtrlVar.kProjectName = new_main_path.split('/')[-1]

    @staticmethod
    def set_reports_path(new_reports_path):
        # CtrlVar.kReportsPath = CtrlVar.kMainPath + '/reports'
        CtrlVar.kReportsPath = new_reports_path

    @staticmethod
    def set_current_environment(cur_env):
        CtrlVar.kCurrentEnvironment = cur_env


class RunControl:
    def __init__(self):
        if CtrlVar.kMainPath == "":
            raise AssertionError("CtrlVar.kMainPath 不能为空")
        else:
            print(f"MainPath: {CtrlVar.kMainPath}")
        if CtrlVar.kReportsPath == "":
            raise AssertionError("CtrlVar.kReportsPath 不能为空")
        else:
            print(f"ReportsPath: {CtrlVar.kReportsPath}")
        self.print_env()
        self.run_list = []
        self.allure_dir_all = ''
        self.run_command_context = ''
        self.idx = 1

    @staticmethod
    def print_env():
        if CtrlVar.kCurrentEnvironment != "":
            print(CtrlVar.kCurrentEnvironment)

    def run_case(self, pytest_command: list):
        path_temps = f"{CtrlVar.kReportsPath}/log_{CtrlVar.kTimestamp}_temps{self.idx}"
        self.run_list.append(["-v", f"--alluredir={path_temps}"] + pytest_command)
        self.idx += 1
        self.allure_dir_all += f'{path_temps} '
        return self

    # def thread_pool_run(self):
    #     # 直接开【多线程/线程池】跑会冲突，建议多容器化运行加速
    #     pool = threadpool.ThreadPool(4)
    #     requests = threadpool.makeRequests(pytest.main, self.run_list)
    #     [pool.putRequest(req) for req in requests]
    #     pool.wait()
    #     return self

    @staticmethod
    def open_all_temps_result():
        all_temps = [str(d) for d in os.listdir(f'{CtrlVar.kReportsPath}') if ("temp" in d) and ("log" in d)]
        all_temps = [str(d) for d in all_temps if time.strftime('%Y_%m_%d', time.localtime()) in d]
        gen_command = "allure generate"
        for temps in all_temps:
            gen_command += f' {CtrlVar.kReportsPath}/{temps}'
        gen_command += f' -o {CtrlVar.kReportsPath}/log_{CtrlVar.kTimestamp}_total --clean'
        print(all_temps)
        print(gen_command)
        os.system(gen_command)
        os.system(f'start chrome http://localhost:{CtrlVar.kPycharmPort}/{CtrlVar.kProjectName}/reports/log_{CtrlVar.kTimestamp}_total/')

    def open_result(self):
        if "Window" in platform.platform():
            allure_to_command = f"allure generate {self.allure_dir_all}"
            allure_to_command += f"-o {CtrlVar.kReportsPath}/log_{CtrlVar.kTimestamp} --clean"
            self.run_command_context += allure_to_command + '\n'
            os.system(allure_to_command)
            open_report_command = f'start chrome http://localhost:{CtrlVar.kPycharmPort}/{CtrlVar.kProjectName}/reports/log_{CtrlVar.kTimestamp}/'
            self.run_command_context += open_report_command + '\n'
            os.system(open_report_command)
        print(self.run_command_context)
        self.print_env()

    def open_report(self):
        for com in self.run_list:
            pytest.main(com)
            self.run_command_context += 'pytest ' + ' '.join(com) + '\n'
        self.open_result()

    def run_main(self, pytest_command: list):
        self.run_case(pytest_command).open_report()


if __name__ == '__main__':
    pass
