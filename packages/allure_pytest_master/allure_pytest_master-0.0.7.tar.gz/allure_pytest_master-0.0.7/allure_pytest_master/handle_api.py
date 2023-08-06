import json
import allure
import datetime
import requests


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
    if isinstance(dict_data, str) and dict_data.strip() != '':
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


def send_api_request(method_data, url_data, headers_data, body_data=None, **kwargs):
    json_body_data = convert_to_json(body_data)
    api_into = f'{method_data.upper()} {url_data} \n{method_data.upper()}'
    api_into += f' Data:\n{json_body_data}\n\nRequest Headers:\n{headers_data}\n\n'
    api_into += f'Request Start:\n{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")}\n'
    try:
        res_data = requests.request(
            method=method_data, url=url_data, data=json_body_data.encode('utf-8'),
            headers=headers_data, timeout=3, **kwargs)
        api_into += f'Response End:\n{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")}\n\n'
        try:
            res_message = convert_to_json(res_data.json())
        except ValueError:
            res_message = convert_to_json(res_data.text)
            pass
        res_string_length = len(res_message)
        api_into += f'Response Status:{res_data.status_code}    Response Time{res_data.elapsed.total_seconds()}\n'
        api_into += f'Response Message Show String Length: {res_string_length}\n'
        show_length = 10000
        if res_string_length > show_length:
            api_into += f'Response Message:\n{res_message[0:5000]}\n' + ' ' * 17
            api_into += f'+++(show_length:{show_length})+++\n{res_message[-5000:-1]}\n'
        else:
            api_into += f'Response Message:\n{res_message}'
        print(api_into)
        allure.attach(api_into, "details")
        return res_data
    except Exception as e:
        api_into += f'Response Error:\n{e}'
        allure.attach(api_into, "details")
        raise AttributeError(e)


if __name__ == '__main__':
    pass
