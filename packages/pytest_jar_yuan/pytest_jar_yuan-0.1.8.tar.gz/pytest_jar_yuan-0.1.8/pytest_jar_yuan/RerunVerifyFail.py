# -*- coding:utf-8 -*-
# @Author: huang-jy
import time


class RerunVerifyFail:
    def retry_on_failure(self, method, retry_count=4, retry_interval=1):
        for i in range(retry_count+1):
            try:
                eval(f'{method}')
                return "pass"
            except AssertionError:
                time.sleep(retry_interval)
                pass
        return "fail"


if __name__ == '__main__':
    pass
