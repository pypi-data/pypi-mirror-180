# -*- coding:utf-8 -*-
# @Author: huang-jy
import json
import allure
import datetime
import requests


def select_dict_from_list(lt: list, dt: dict):
    new_lt = []
    for l_data in lt:
        result = 1
        for dtKey in dt.keys():
            if l_data[dtKey] != dt[dtKey]:
                result = 0
        if result:
            new_lt.append(l_data)
    return new_lt


def get_dictionary_form_list(d_list, **kwargs):
    new_list = []
    for d in d_list:
        is_exist = "yes"
        for k, v in kwargs.items():
            try:
                if d[k] != v:
                    is_exist = 'no'
                    break
            except KeyError:
                is_exist = 'no'
                break
        if is_exist == "yes":
            new_list.append(d)
    return new_list


def convert_to_json(dict_data):
    if dict_data is None:
        return ''
    if isinstance(dict_data, str):
        if dict_data.strip() == '':
            return dict_data
        try:
            # 如果可以会转为dict或list
            dict_data = json.loads(dict_data)
        except ValueError:
            pass
    if isinstance(dict_data, (dict, list)):
        dict_data = json.dumps(dict_data, sort_keys=True, indent=4, ensure_ascii=False, separators=(',', ':'))
    if isinstance(dict_data, int):  # 字符串数字会因为 json.loads 转为 int 导致request报错
        dict_data = str(dict_data)
    return dict_data


def json_output(data):
    print(convert_to_json(data))


def send_api_request(method_data, url_data, headers_data, body_data=None, timeout=7, is_print=False, **kwargs):
    json_body_data = convert_to_json(body_data)
    api_into = f'{method_data.upper()} {url_data}'
    api_into += f'\n{method_data.upper()} Data:'
    api_into += f'\n{json_body_data}\n\nRequest Headers:\n{headers_data}\n\n'
    api_into += f'RequestStart:{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")}\n'
    api_err = ""
    try:
        res_data = requests.request(
            method=method_data, url=url_data, data=json_body_data.encode('utf-8'),
            headers=headers_data, timeout=timeout, **kwargs)
    except Exception as e:
        api_into += f'ResponseOver:{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")}\n\n'
        api_err += f'Response Error:\n{e}'
        api_into += api_err
    else:
        api_into += f'ResponseOver:{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")}\n\n'
        try:
            res_message = convert_to_json(res_data.json())  # json | return dict | 多这一步处理快点
        except ValueError:
            res_message = convert_to_json(res_data.text)
        res_string_length = len(res_message)
        api_into += f'Response Status:{res_data.status_code}    Response Time{res_data.elapsed.total_seconds()}\n'
        api_into += f'Response Message Show String Length: {res_string_length}\n'
        show_length = 10000
        if res_string_length > show_length:
            api_into += f'Response Message:\n{res_message[0:5000]}\n' + ' ' * 17
            api_into += f'+++(show_length:{show_length})+++\n{res_message[-5000:-1]}\n'
        else:
            api_into += f'Response Message:\n{res_message}'
        return res_data
    finally:
        allure.attach(api_into, "details")
        if is_print:
            print(api_into)
        if api_err != "":
            raise AssertionError(api_err)


def collect_data_from_string(cur_string: str, start_part: str, end_part: str) -> str:
    idx_start_part = cur_string.find(start_part)
    new_string = cur_string[idx_start_part+len(start_part):]
    idx_end_part = new_string.find(end_part)
    return new_string[:idx_end_part]


if __name__ == '__main__':
    print(convert_to_json({"name": "123"}))
    pass
