#!/usr/bin/env python3
import os
import sys
import re

CLASSES_DIR = "{}/Documents/UWcourses".format(os.path.expanduser("~"))


def className():
    clsName = input("What class do you want to add? ")
    while not re.match(r"^\w{3,7}\d{3}$", clsName):
        print("please write the class in the form CodeNumber")
        clsName = input("What class do you want to add? ")
    return clsName


def classCode(cls):
    term = input("What term are you taking {}? ".format(cls))
    while not re.match(r"^\d{2}(au|wi|sp|su)$", term):
        print("please write the term in the form YYQQ, Y for year, Q for" \
                "quarter")
        term = input("What term are you taking {}? ".format(cls))
    return "{}-{}".format(cls, term)


def createClassDir(code):
    group_path = "{}/{}".format(CLASSES_DIR, re.split(r"\d", code)[0])
    if not os.path.isdir(group_path):
        os.makedirs(group_path)

    class_path = "{}/{}".format(group_path, code)
    if os.path.isdir(class_path):
        sys.exit("class directory already exists!")

    os.makedirs(class_path)
    os.makedirs("{}/Lectures".format(class_path))
    os.makedirs("{}/Sections".format(class_path))
    os.makedirs("{}/HW".format(class_path))

def main(argv):
    if not argv:
        argv = [className()]

    for cls in argv:
        createClassDir(classCode(cls))

    print("classes are added!")

if __name__ == "__main__":
    main(sys.argv[1:])
