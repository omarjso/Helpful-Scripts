#!/usr/bin/env python3
import os
import sys
import re

CLASS_ALIASES = "{}/.aliases/.classes".format(os.path.expanduser("~"))
UNIS = ["UW", "KAUST"]

def addBashAlias(class_code, class_path):
    code = class_code.split("-")[0]
    path = class_path.replace(os.path.expanduser("~"), "~")
    alias_command = 'alias {}="cd {}"\n'.format(code, path)
    with open(CLASS_ALIASES, "a") as f:
            f.write(alias_command)

def className():
    clsName = input("What class do you want to add? ")
    while not re.match(r"^\w{2,7}\d{3}$", clsName):
        print("please write the class in the form CodeNumber")
        clsName = input("What class do you want to add? ")

    uniName = input(f"What university is this class in? {UNIS} ")
    while not uniName in UNIS:
        print("Choose a university from the listed universities")
        uniName = input(f"What university is this class in? {UNIS} ")
    return clsName, uniName


def classCode(cls):
    term = input("What term are you taking {}? ".format(cls))
    while not re.match(r"^\d{2}(au|wi|sp|su)$", term):
        print("please write the term in the form YYQQ, Y for year, Q for" \
                "quarter")
        term = input("What term are you taking {}? ".format(cls))
    return "{}-{}".format(cls, term)


def createClassDir(code, uni):
    CLASSES_DIR = "{}/Documents/{}/Courses".format(os.path.expanduser("~"), uni)
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
    return class_path

def main(argv):
    if not argv:
        argv = [className()]

    for cls, uni in argv:
        class_code = classCode(cls)
        class_path = createClassDir(class_code, uni)
        addBashAlias(class_code, class_path)

    print("classes are added!")

if __name__ == "__main__":
    main(sys.argv[1:])
