#!/usr/bin/env python

from user import User

class Student(User):
    knowledge = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
]
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.knowledge = Student.knowledge

    
    def learn(self,str):
        return self.knowledge.append(str)
        pass