# -*- coding:utf-8 -*-
# @Author: huang-jy
import inspect
import allure


def operation(operation_expression: str, precision=6, name="operation_result"):
    this_code_context = inspect.stack()[1].code_context[0].strip().split(",")[0]
    operation_index = this_code_context.find("operation(")
    if this_code_context[operation_index + 10] == "f":
        operation_index += 1
    join_var = this_code_context[operation_index+10:-1].replace('"', '').replace("'", "")
    join_var = join_var.replace('{', '').replace('}', '')
    get_result = format(eval(f'{operation_expression}'), f'.{precision}f')
    operation_result_context = f'{name}'
    operation_result_context += f'\n= {join_var}'
    operation_result_context += f'\n= {operation_expression}'
    operation_result_context += f'\n= {get_result}'
    print(operation_result_context)
    allure.attach(f'{operation_result_context}', f'{name}({get_result})')
    if '.' in get_result:
        return float(get_result)
    else:
        return int(get_result)


class OperationSetting:
    def __init__(self, name="operation_result", precision=6):
        self._name = name
        self._precision = precision
        self._operation_describe = ''
        self._operation_variable_context = ''
        self._operation_value_context = ''
        self._operation_total_context = f'{name}'

    def add_operation_describe(self, des: str):
        self._operation_describe += des

    def append_operation(self, operation_expression: str):
        this_code_context = inspect.stack()[1].code_context[0].strip()
        operation_index = this_code_context.find('operation(')
        if this_code_context[operation_index+10] == 'f':
            operation_index += 1
        join_var = this_code_context[operation_index+10:-1].replace('"', '').replace("'", "")
        join_var = join_var.replace('{', '').replace('}', '')
        if self._operation_variable_context == '':
            self._operation_variable_context += f'{join_var}'
        else:
            self._operation_variable_context += f'\n  {join_var}'
        self._operation_value_context += operation_expression

    def generate_results(self):
        try:
            get_result = format(eval(f'{self._operation_value_context}'), f'.{self._precision}f')
            if self._operation_describe != '':
                self._operation_total_context += f'\n= {self._operation_describe}'
            self._operation_total_context += f'\n= {self._operation_variable_context}'
            self._operation_total_context += f'\n= {self._operation_value_context}'
            self._operation_total_context += f'\n= {get_result}'
            print(self._operation_total_context)
            allure.attach(f'{self._operation_total_context}', f'{self._name}({get_result})')
            if '.' in get_result:
                return float(get_result)
            else:
                return int(get_result)
        except SyntaxError as e:
            error_info = f'SyntaxError:{e}\n_operation_value_context:{self._operation_value_context}'
            allure.attach(error_info, f'{self._name}|SyntaxError')
            raise AssertionError(error_info)


if __name__ == '__main__':
    # op_set = OperationSetting(name='bb', precision=2)
    # op_set.append_operation('1+2')
    # op_set.append_operation('+3')
    # print(op_set.generate_results())
    # print(operation('9+11+33', precision=3, name="hao"))
    pass
