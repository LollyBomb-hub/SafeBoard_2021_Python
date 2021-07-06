#! /bin/python3


import os
import subprocess
from selenium import webdriver


def start_program(path: str, name: str) -> subprocess.Popen:
	return subprocess.Popen(os.path.join(path, name), cwd=path, stdout=subprocess.PIPE,
				stderr=subprocess.PIPE, encoding="utf-8")


def get_driver(path):
	return webdriver.Chrome(executable_path=path)
