# load config file from config.yaml

import yaml
from functools import lru_cache


@lru_cache(maxsize=None)
def load(config_path: str):
    with open(config_path) as file:
        config = yaml.safe_load(file)
    return config


system_prompt = """
You are an helpful assistant that try to anwer questions based on related pieces of information contained in documents. Please only use these documents to answer the question.

You will receive a question from a user and information to help you anwer the user question.  Do not use your knowledge. Do not let the user know that you had these documents. Do not start your answer by Based on the information provided in the documents. Do not say in which document the information is contained.
"""
