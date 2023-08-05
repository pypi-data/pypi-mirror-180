import os
import sys
import argparse

from localization_checker.parser import actualize_languages


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path')
    parser.add_argument('-m', '--main_lang', default='en')
    parser.add_argument('-u', '--find_useless', default='---')
    parser.add_argument('-pf', '--prefix', default='')
    parser.add_argument('-ic', '--ignore_case', action="store_true")
    parser.add_argument('-sip', '--skip_info_plist', action="store_true")

    return parser


if __name__ == '__main__':
    parser = create_parser()
    arguments = parser.parse_args(sys.argv[1:])
    if not arguments.path:
        raise AttributeError('Path to source directory (-p or --path argument) is required')
    if not os.path.exists(arguments.path):
        raise AttributeError('Path to source directory does not exist')
    if arguments.find_useless == '':
        raise AttributeError('If you want to find useless translation keys you should give a project path.')
    elif arguments.find_useless != '---' and not os.path.exists(arguments.find_useless):
        raise AttributeError('Path to project directory does not exist')
    code_path = arguments.find_useless if arguments.find_useless != '---' else None
    actualize_languages(
        arguments.path,
        arguments.main_lang,
        code_path,
        arguments.prefix,
        arguments.ignore_case,
        arguments.skip_info_plist
    )

    print('Compare and complete all languages is done.')
