import inspect
import time
import allure
import prettytable as pt


class RerunVerifyFail:
    def __init__(self):
        self.final_result = "pass"

    def retry_on_failure(self, method, retry_count=4, retry_interval=1):
        for i in range(retry_count + 1):
            try:
                eval(f'{method}')
                return "pass"
            except AttributeError:
                time.sleep(retry_interval)
                pass
        self.final_result = "fail"
        return 'fail'


class VerifyTable:
    def __init__(self, varify_name="verify_details"):
        self._varify_name = varify_name
        self._varify_table = pt.PrettyTable()
        self._varify_table.field_names = ["Describe", "Verify Expression", "Result"]
        self._verify_result = "pass"

    def _insert_default_row(self):
        self._varify_table.add_row(['-' * 18, "-" * 80, "-" * 6])

    def append_should_be_true(self, verify_expression: str, precision=3, allow_error=0.002):
        verify_join_ver_total = inspect.stack()[1].code_context[0].strip().split(',')[0]
        true_index = verify_join_ver_total.find('true')
        verify_join_var = verify_join_ver_total[true_index + 6:-1].replace("self.", "").replace("'", "")
        verify_join_var = verify_join_var.replace('{', '').replace('}', '')
        self._varify_table.add_row(["Variable", verify_join_var, ""])
        try:
            if eval(verify_expression):
                self._varify_table.add_row(["Actual Value", verify_expression, "pass"])
            else:
                if '==' in verify_expression and precision != 0:
                    left_data, right_data = verify_expression.split('==')
                    if isinstance(eval(left_data), (int, float)) and isinstance(eval(right_data), (int, float)):
                        left_data_result = format(eval(f'{left_data}'), f'.{precision}f')
                        right_data_result = format(eval(f'{right_data}'), f'.{precision}f')
                        balance = format(eval(f'{left_data_result}-{right_data_result}'), f'.{precision}f')
                        abs_balance = abs(eval(balance))
                        if abs_balance > allow_error:
                            self._verify_result = 'fail'
                            self._varify_table.add_row(["Actual Value", verify_expression, 'fail'])
                        else:
                            self._varify_table.add_row(["Actual Value", verify_expression, 'pass'])
                        self._varify_table.add_row(["LeftData == RightData", f'{left_data_result} == {right_data_result}', ''])
                        self._varify_table.add_row(["LeftData - RightData", f'{balance} | {abs_balance}>{allow_error}(allow_error)', ''])
                    else:
                        self._verify_result = 'fail'
                        self._varify_table.add_row(["Actual Value", verify_expression, 'fail'])
                else:
                    self._verify_result = 'fail'
                    self._varify_table.add_row(["Actual Value", verify_expression, 'fail'])
        except (SyntaxError, NameError):
            self._verify_result = 'fail'
            self._varify_table.add_row(["Actual Value", "SyntaxError", 'error'])
        self._insert_default_row()

    def generate_result(self):
        print(self._varify_table)
        allure.attach(f'{self._varify_table}', f'{self._varify_name} | {self._verify_result}')
        if self._verify_result == 'fail':
            raise AttributeError(f"fail: {self._varify_name}")


def operation(operation_expression: str, precision=6, name="operation_result"):
    this_code_context = inspect.stack()[1].code_context[0].strip().split(',')[0]
    operation_index = this_code_context.find('operation(')
    if this_code_context[operation_index + 10] == 'f':
        operation_index += 1
    join_var = this_code_context[operation_index + 10:-1].replace('"', '').replace("'", "")
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
        if this_code_context[operation_index + 10] == 'f':
            operation_index += 1
        join_var = this_code_context[operation_index + 10:-1].replace('"', '').replace("'", "")
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
            error_info = f'SyntaxError：{e}\n_operation_value_context:{self._operation_value_context}'
            allure.attach(error_info, f'{self._name} | SyntaxError')
            raise AttributeError(error_info)


if __name__ == '__main__':
    op_set = OperationSetting(name='bb', precision=2)
    op_set.append_operation('1+2')
    op_set.append_operation('+3')
    print(op_set.generate_results())
    print(operation('9+11+33', precision=3, name="hao"))
    pass
