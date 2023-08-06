# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     const
   Description :
   Author :       qiangyanwen
   date：          2021/4/6
-------------------------------------------------
"""


class JMXPath:
    TESTCASE = './/HTTPSamplerProxy[@enabled="true"]'
    DOMAIN = 'stringProp[@name="HTTPSampler.domain"]'
    PORT = 'stringProp[@name="HTTPSampler.port"]'
    PROTOCOL = 'stringProp[@name="HTTPSampler.protocol"]'
    PATH = 'stringProp[@name="HTTPSampler.path"]'
    METHOD = 'stringProp[@name="HTTPSampler.method"]'
    ARG_FILE_COLLECTION = 'elementProp[@elementType="HTTPFileArg"]/collectionProp/elementProp'
    ARG_COLLECTION = 'elementProp[@elementType="Arguments"]/collectionProp/elementProp'
    ARG_TYPE = 'boolProp[@name="HTTPSampler.postBodyRaw"]'
    ARG_FILE_NAME = 'stringProp[@name="File.paramname"]'
    ARG_FILE_PATH = 'stringProp[@name="File.path"]'
    ARG_NAME = 'stringProp[@name="Argument.name"]'
    ARG_VALUE = 'stringProp[@name="Argument.value"]'
    HEADER_MANAGER = 'following::hashTree[1]/HeaderManager'
    HEADER_COLLECTION = 'collectionProp/elementProp'
    HEADER_NAME = 'stringProp[@name="Header.name"]'
    HEADER_VALUE = 'stringProp[@name="Header.value"]'
    ASSERTION_MANAGER = 'following::hashTree[1]/ResponseAssertion[@enabled="true"]'
    ASSERTION_COLLECTION = 'collectionProp/stringProp'
    ASSERTION_TYPE = 'intProp'
    JSON_ASSERTION_MANAGER = 'following::hashTree[1]/JSONPathAssertion[@enabled="true"]'
    JSON_ASSERTION_PATH = 'stringProp[@name="JSON_PATH"]'
    JSON_ASSERTION_VALUE = 'stringProp[@name="EXPECTED_VALUE"]'
    EXTRACTOR_MANAGER = 'following::hashTree[1]/JSONPostProcessor[@enabled="true"]'
    EXTRACTOR_NAME = 'stringProp[@name="JSONPostProcessor.referenceNames"]'
    EXTRACTOR_PATH = 'stringProp[@name="JSONPostProcessor.jsonPathExprs"]'
    EXTRACTOR_INDEX = 'stringProp[@name="JSONPostProcessor.match_numbers"]'
    EXTRACTOR_DEFAULT = 'stringProp[@name="JSONPostProcessor.defaultValues"]'
    PARAMETER_COLLECTION = './/collectionProp[@name="UserParameters.thread_values"]'
    PARAMETERS = 'collectionProp/stringProp'
    USER_PARAMETERS_COLLECTION = 'following::hashTree[1]/UserParameters[@enabled="true"]'
    USER_PARAMETERS_KEY_COLLECTION = './/collectionProp[@name="UserParameters.names"]/stringProp'
    USER_PARAMETERS_VALUE_COLLECTION = './/collectionProp[@name="UserParameters.thread_values"]/collectionProp/stringProp'
    BEAN_SHELL_COLLECTION = 'following::hashTree[1]/BeanShellPostProcessor[@enabled="true"]'
    BEAN_SHELL_KEY = 'stringProp[@name="parameters"]'


class JMXAttr:
    TEST_NAME = "testname"
