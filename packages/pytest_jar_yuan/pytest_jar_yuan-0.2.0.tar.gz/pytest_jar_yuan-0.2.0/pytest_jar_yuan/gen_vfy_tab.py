# -*- coding:utf-8 -*-
# @Author: huang-jy
import inspect
import allure
import prettytable as pt


class GenerateResults:
    def __init__(self):
        self.kTotal = 0
        self.kPass = 0
        self.kFail = 0
        self.kError = 0
        self.kAttachName = ""
        self.kAttachContext = ""

    def check(self):
        if self.kTotal == 0:
            raise AssertionError("total == 0")
        if self.kFail > 0:
            raise AssertionError("fail > 0")
        if self.kError > 0:
            raise AssertionError("error > 0")


class VerifyTable:
    def __init__(self, varify_name="verify_details"):
        self._verify_name = varify_name
        self._verify_table = pt.PrettyTable()
        self._verify_table.field_names = ["Describe", "Verify Expression", "Result"]
        self.result = GenerateResults()
        self._has_result = False

    def _insert_default_row(self):
        self._verify_table.add_row(['-' * 18, "-" * 80, "-" * 6])

    def that_is_true(self, verify_expression: str, precision=3, allow_error=0.002):
        self.result.kTotal += 1
        verify_join_ver_total = inspect.stack()[1].code_context[0].strip().split(',')[0]
        true_index = verify_join_ver_total.find('true')
        verify_join_var = verify_join_ver_total[true_index + 6:-1].replace("self.", "").replace("'", "")
        verify_join_var = verify_join_var.replace('{', '').replace('}', '')
        self._verify_table.add_row(["Variable", verify_join_var, ""])
        try:
            if eval(verify_expression):
                self.result.kPass += 1
                self._verify_table.add_row(["Actual Value", verify_expression, "pass"])
            else:
                if '==' in verify_expression and precision != 0:
                    left_data, right_data = verify_expression.split('==')
                    if isinstance(eval(left_data), (int, float)) and isinstance(eval(right_data), (int, float)):
                        left_data_result = format(eval(f'{left_data}'), f'.{precision}f')
                        right_data_result = format(eval(f'{right_data}'), f'.{precision}f')
                        balance = format(eval(f'{left_data_result}-{right_data_result}'), f'.{precision}f')
                        abs_balance = abs(eval(balance))
                        if abs_balance > allow_error:
                            self.result.kFail += 1
                            self._verify_table.add_row(["Actual Value", verify_expression, 'fail'])
                        else:
                            self.result.kPass += 1
                            self._verify_table.add_row(["Actual Value", verify_expression, 'pass'])
                        self._verify_table.add_row(["LeftData == RightData", f'{left_data_result} == {right_data_result}', ''])
                        self._verify_table.add_row(["LeftData - RightData", f'{balance} | {abs_balance}=<{allow_error}(allow_error)', ''])
                    else:
                        self.result.kFail += 1
                        self._verify_table.add_row(["Actual Value", verify_expression, 'fail'])
                else:
                    self.result.kFail += 1
                    self._verify_table.add_row(["Actual Value", verify_expression, 'fail'])
        except (SyntaxError, NameError):
            self.result.kError += 1
            self._verify_table.add_row(["Actual Value", "SyntaxError", 'error'])
        self._insert_default_row()

    def generate_result(self):
        self.result.kAttachName += f'{self._verify_name}:\n'
        self.result.kAttachName += f'total: {self.result.kTotal} | error: {self.result.kError} | '
        self.result.kAttachName += f'pass: {self.result.kPass} | fail: {self.result.kTotal}'
        self.result.kAttachContext += f'{self._verify_table}'
        allure.attach(self.result.kAttachContext, self.result.kAttachName)
        self._has_result = True
        return self.result

    def check(self):
        if self._has_result:
            self.result.check()
        else:
            self.generate_result().check()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with allure.step(f'{self._verify_name}'):
            self.check()


def output_verify_result(name: str, *args: GenerateResults):
    all_result = GenerateResults()
    all_result.kContext = f'{name}\n\n'
    for arg in args:
        if arg is not None:
            all_result.kTotal += arg.kTotal
            all_result.kPass += arg.kPass
            all_result.kFail += arg.kFail
            all_result.kError += arg.kError
            all_result.kContext += f'{arg.kAttachName}\n\n'
    all_result.kAttachName = f'{name} | Total: {all_result.kTotal} | Error: {all_result.kError} | '
    all_result.kAttachName += f'{all_result.kPass} | Error: {all_result.kFail}'
    allure.attach(all_result.kContext, all_result.kAttachName)
    return all_result


if __name__ == '__main__':
    pass
