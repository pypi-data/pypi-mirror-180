# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     parser
   Description :
   Author :       qiangyanwen
   date：          2021/4/6
-------------------------------------------------
"""

from lxml import etree
from jmx2yaml.const import JMXPath, JMXAttr
from jmx2yaml.util import get_name_from_url
import re

try:
    import simplejson as json
except (ImportError, SyntaxError):
    import json

assertion_map = {
    '16': 'in',
    '2': 'in',
    '6': 'not in',
    '20': 'not in'
}

re_str = "\$\{([A-Za-z0-9_]{1,100}?)\}"


def format_template(s) -> str:
    if s:
        results = re.findall(re_str, s)
        for ret in results:
            s = s.replace("${" + ret + "}", '{{' + ret + '}}')
    return s


def get_template_value(s) -> str:
    if s:
        results = re.findall(re_str, s)
        for ret in results:
            s = s.replace("${" + ret + "}", ret)
    return s


def _wrapper_header(step) -> {}:
    header_managers = step.xpath(JMXPath.HEADER_MANAGER)
    header = {}
    for header_manager in header_managers:
        headers = header_manager.findall(JMXPath.HEADER_COLLECTION)
        for h in headers:
            k = h.find(JMXPath.HEADER_NAME).text
            if k:
                k = format_template(k)
                header[k] = format_template(h.find(JMXPath.HEADER_VALUE).text)
    return header


def _wrapper_assertion(step) -> []:
    assertion_managers = step.xpath(JMXPath.ASSERTION_MANAGER)
    assertion_list = []
    for assertion_manager in assertion_managers:
        ast_type = assertion_manager.find(JMXPath.ASSERTION_TYPE).text
        if not ast_type:
            continue
        if ast_type not in assertion_map:
            print('unknown assertion type', ast_type)
            continue
        assertions = assertion_manager.findall(JMXPath.ASSERTION_COLLECTION)
        for ast in assertions:
            assertion_list.append(
                {'path': '.', 'expect': format_template(ast.text), 'operator': assertion_map[ast_type]})
    json_assertion_managers = step.xpath(JMXPath.JSON_ASSERTION_MANAGER)
    for json_assertion in json_assertion_managers:
        path = json_assertion.find(JMXPath.JSON_ASSERTION_PATH)
        value = json_assertion.find(JMXPath.JSON_ASSERTION_VALUE)
        if path is not None:
            assertion_list.append(
                {'path': format_template(path.text), 'expect': format_template(value.text), 'operator': "="})
    return assertion_list


def _wrapper_extractor(step) -> []:
    extractor_managers = step.xpath(JMXPath.EXTRACTOR_MANAGER)
    extractor_list = []
    for extractor_manager in extractor_managers:
        path = name = default = ''
        index = 0
        if extractor_manager.find(JMXPath.EXTRACTOR_PATH) is not None:
            path = format_template(extractor_manager.find(JMXPath.EXTRACTOR_PATH).text)
        if extractor_manager.find(JMXPath.EXTRACTOR_NAME) is not None:
            name = format_template(extractor_manager.find(JMXPath.EXTRACTOR_NAME).text)
        if extractor_manager.find(JMXPath.EXTRACTOR_INDEX) is not None:
            if extractor_manager.find(JMXPath.EXTRACTOR_INDEX).text:
                index = int(extractor_manager.find(JMXPath.EXTRACTOR_INDEX).text)
        if extractor_manager.find(JMXPath.EXTRACTOR_DEFAULT) is not None:
            default = format_template(extractor_manager.find(JMXPath.EXTRACTOR_DEFAULT).text)
        extractor_list.append({'path': path, 'name': name, 'index': index, 'default': default})
    return extractor_list


def _get_arg(step) -> {}:
    data = {}
    args = step.xpath(JMXPath.ARG_COLLECTION)
    for arg in args:
        k = arg.find(JMXPath.ARG_NAME)
        if k is not None:
            k = format_template(k.text)
            data[k] = format_template(arg.find(JMXPath.ARG_VALUE).text)
    return data


def _get_file(step) -> {}:
    data = {}
    args = step.xpath(JMXPath.ARG_FILE_COLLECTION)
    for arg in args:
        k = arg.find(JMXPath.ARG_FILE_NAME)
        if k is not None:
            k = format_template(k.text)
            data[k] = format_template(arg.find(JMXPath.ARG_FILE_PATH))
    return data


def _get_json(step) -> {}:
    data = {}
    args = step.xpath(JMXPath.ARG_COLLECTION)
    if not args:
        return data
    try:
        v = args[0].find(JMXPath.ARG_VALUE)
        if v is not None:
            s = format_template(v.text)
            data = json.loads(s)
    except ValueError as e:
        print('parser json error', e)
    return data


def _wrapper_request(step, method: str) -> {}:
    data = {}
    arg_type = step.find(JMXPath.ARG_TYPE)
    if arg_type is not None:
        arg_type = arg_type.text
        if arg_type == "true":
            jj = _get_json(step)
            if jj:
                data['json'] = jj
    file = _get_file(step)
    if file:
        data['file'] = file
    arg = _get_arg(step)
    if arg:
        if method.upper() == 'GET':
            data['query'] = arg
        else:
            data['data'] = arg
    return data


def _wrapper_step_arg(step, data: dict) -> None:
    bean_args = step.xpath(JMXPath.BEAN_SHELL_COLLECTION)
    for arg in bean_args:
        param = arg.find(JMXPath.BEAN_SHELL_KEY)
        if param is not None:
            data[param.text] = ""
    args = step.xpath(JMXPath.USER_PARAMETERS_COLLECTION)
    for arg in args:
        params = arg.findall(JMXPath.USER_PARAMETERS_KEY_COLLECTION)
        if params is not None:
            for i, param in enumerate(params):
                v = arg.find(JMXPath.USER_PARAMETERS_VALUE_COLLECTION + '[{}]'.format(i + 1))
                if v is not None:
                    data[param.text] = v.text


def get_parameters(tree) -> dict:
    data = {}
    parameter_node = tree.find(JMXPath.PARAMETER_COLLECTION)
    if parameter_node is not None:
        parameters = parameter_node.findall(JMXPath.PARAMETERS)
        for parameter in parameters:
            k = get_template_value(parameter.text)
            if k:
                data[k] = ""
    return data


def parse_jmx_file(fn):
    tree = etree.parse(fn)
    params = get_parameters(tree)
    steps = tree.xpath(JMXPath.TESTCASE)
    suite_name = get_name_from_url(fn)
    steps_list = []
    for step in steps:
        name = step.get(JMXAttr.TEST_NAME)
        protocol = "http" if not step.find(JMXPath.PROTOCOL).text else step.find(JMXPath.PROTOCOL).text
        host = step.find(JMXPath.DOMAIN).text
        port = "" if not step.find(JMXPath.PORT).text else ":" + step.find(JMXPath.PORT).text
        path = step.find(JMXPath.PATH).text
        url = "{}://{}{}{}".format(protocol, host, port, path)
        method = step.find(JMXPath.METHOD).text
        header = _wrapper_header(step)
        assertion_list = _wrapper_assertion(step)
        extractor_list = _wrapper_extractor(step)
        _wrapper_step_arg(step, params)
        req = {'url': format_template(url), 'method': method, 'header': header, }
        req.update(_wrapper_request(step, method))
        steps_list.append({'name': name, 'request': req, 'assertion': {'body': assertion_list},
                           'extractor': {'body': extractor_list}})
    return {'name': suite_name, 'config': {'constant': params}, 'groups': [{'name': suite_name, 'steps': steps_list}]}


if __name__ == "__main__":
    fp = "/Users/qiangyanwen/Downloads/automation/移动端校验.jmx"
    dd = parse_jmx_file(fp)
    print(json.dumps(dd, ensure_ascii=False))
