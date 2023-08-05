#!/usr/bin/env python3

"""
This module contains all functions for the documentation.
"""

import yaml
import json
import os
import glob
import re

from pytablewriter import MarkdownTableWriter


def md_file(outpath):
    """
    This function creates the markdown file.

    :param outpath: The path to save the Markdown document to
    """
    if not os.path.exists(f'{outpath}'):
        open(outpath, 'w+').close()
    else:
        open(outpath, 'w').close()


def write_table(data):
    """
    This function creates the markdown table.

    :param data: The data to be written to the table
    :return: The Markdown table writer
    """

    writer = MarkdownTableWriter(
        headers=['setting', 'value'],
        value_matrix=data,
    )

    return writer


def assignment_table(data):
    """
    This function creates the Markdown assignments table.

    :param data: The data to be written to the table
    :return: The Markdown table writer
    """

    def write_assignment_table(data, headers):
        writer = MarkdownTableWriter(
            headers=headers,
            value_matrix=data
        )

        return writer

    table = ""
    if "assignments" in data:
        assignments = data['assignments']
        assignment_list = []
        target = ""
        intent = ""
        for assignment in assignments:
            if assignment['target']['@odata.type'] == "#microsoft.graph.allDevicesAssignmentTarget":
                target = "All Devices"
            if assignment['target']['@odata.type'] == "#microsoft.graph.allLicensedUsersAssignmentTarget":
                target = "All Users"
            if 'groupName' in assignment['target']:
                target = assignment['target']['groupName']
            if "intent" in assignment:
                intent = assignment['intent']
                headers = ['intent', 'target', 'filter type', 'filter name']
            else:
                headers = ['target', 'filter type', 'filter name']
            if intent:
                assignment_list.append([intent,
                                        target,
                                        assignment['target']['deviceAndAppManagementAssignmentFilterType'],
                                        assignment['target']['deviceAndAppManagementAssignmentFilterId']])
            else:
                assignment_list.append([target,
                                        assignment['target']['deviceAndAppManagementAssignmentFilterType'],
                                        assignment['target']['deviceAndAppManagementAssignmentFilterId']])

            table = write_assignment_table(assignment_list, headers)

    return table


def remove_characters(string):
    """
    This function removes characters from the string.
    :param string: The string to be cleaned
    :return: The cleaned string
    """

    remove_chars = '#@}{]["'
    for char in remove_chars:
        string = string.replace(char, "")

    return string


def clean_list(data):
    """
    This function cleans the list.
    :param data: The list to be cleaned
    :return: The cleaned list
    """

    def list_string(data):
        string = ""
        liststr = ","
        table_string = ""
        string_list = []
        for i in data:
            if isinstance(i, str):
                string_list.append(i)
            if isinstance(i, list):
                string = i + liststr
                string = remove_characters(string)
            if isinstance(i, dict):
                for k, v in i.items():
                    if isinstance(v, str) and len(v) > 200:
                        i[k] = f'<details><summary>Click to expand...</summary>{v}</details>'

                string = json.dumps(i)
                string = remove_characters(string)

            table_string += string + liststr + "<br /> <br />"

        if string_list:
            table_string = liststr.join(string_list)

        return table_string

    def dict_string(data):

        # if value is a list, separate with a line break and indent
        for k, v in data.items():
            if isinstance(v, list):
                l = []
                if v:
                    first = '<br />&nbsp;&nbsp;&nbsp;&nbsp; - &nbsp;' + v[0]
                    for i in v[1:]:
                        i = "&nbsp;&nbsp;&nbsp;&nbsp; - &nbsp;" + i
                        l.append(i)
                    l.insert(0, first)
                    data[k] = l
            if isinstance(v, dict):
                # if value is a dict, separate with a line break and indent
                for k2, v2 in v.items():
                    if isinstance(v2, list):
                        l = []
                        if v2:
                            first = '<br />&nbsp;&nbsp;&nbsp;&nbsp; - &nbsp;' + v2[0]
                            for i in v2[1:]:
                                i = "&nbsp;&nbsp;&nbsp;&nbsp; - &nbsp;" + i
                                l.append(i)
                            l.insert(0, first)
                            v[k2] = l

        string = json.dumps(data)
        string = remove_characters(string)

        return string

    def string(data):
        if len(data) > 200:
            string = f'<details><summary>Click to expand...</summary>{item}</details>'
        else:
            string = item

        return string

    values = []

    for item in data:
        if isinstance(item, list):
            values.append(list_string(item))
        elif isinstance(item, dict):
            values.append(dict_string(item))
        elif isinstance(item, str):
            values.append(string(item))
        elif isinstance(item, int):
            values.append(item)
        elif isinstance(item, bool):
            values.append(item)
        else:
            values.append(item)

    return values


def document_configs(configpath, outpath, header, max_length, split, cleanup):
    """
    This function documents the configuration.

    :param configpath: The path to where the backup files are saved
    :param outpath: The path to save the Markdown document to
    :param header: Header of the configuration being documented
    :param max_length: The maximum length of the configuration to write to the Markdown document
    :param split: Split documentation into multiple files
    """

    # If configurations path exists, continue
    if os.path.exists(configpath):
        if split:
            outpath = configpath + "/" + header + ".md"
            md_file(outpath)
        with open(outpath, 'a') as md:
            md.write('# ' + header + '\n')

        pattern = configpath + "*/*"
        for filename in sorted(glob.glob(pattern, recursive=True), key=str.casefold):
            if filename.endswith(".md") or os.path.isdir(filename) or filename == ".DS_Store":
                continue

            # Check which format the file is saved as then open file, load data and set query parameter
            with open(filename) as f:
                if filename.endswith(".yaml"):
                    data = json.dumps(yaml.safe_load(f))
                    repo_data = json.loads(data)
                elif filename.endswith(".json"):
                    f = open(filename)
                    repo_data = json.load(f)

                # Create assignments table
                assignments_table = ""
                assignments_table = assignment_table(repo_data)
                repo_data.pop('assignments', None)

                description = ""
                if 'description' in repo_data:
                    if repo_data['description'] is not None:
                        description = repo_data['description']
                        repo_data.pop('description')

                # Write configuration Markdown table
                config_table_list = []
                for key, value in zip(repo_data.keys(), clean_list(repo_data.values())):
                    if cleanup:
                        if not value and type(value) is not bool:
                            continue

                    if key == "@odata.type":
                        key = "Odata type"

                    else:
                        key = key[0].upper() + key[1:]
                        key = re.findall('[A-Z][^A-Z]*', key)
                        key = ' '.join(key)

                    if max_length:
                        if value and isinstance(value, str) and len(value) > max_length:
                            value = "Value too long to display"

                    if value and isinstance(value, str):
                        comma = re.findall('[:][^:]*', value)
                        if len(value.split(",")) > 1:
                            vals = []
                            for v in value.split(','):
                                v = v.replace(' ', '')
                                if comma:
                                    for char in v:
                                        if char == ":":
                                            v = f'**{v.replace(":", ":** ")}'
                                vals.append(v)
                            value = ",".join(vals)
                            value = value.replace(',', '<br />')

                    config_table_list.append([key, value])

                config_table = write_table(config_table_list)

                # Write data to file
                with open(outpath, 'a') as md:
                    if "displayName" in repo_data:
                        md.write('## ' + repo_data['displayName'] + '\n')
                    if "name" in repo_data:
                        md.write('## ' + repo_data['name'] + '\n')
                    if description:
                        md.write(f'Description: {description} \n')
                    if assignments_table:
                        md.write('### Assignments \n')
                        md.write(str(assignments_table) + '\n')
                    md.write(str(config_table) + '\n')


def document_management_intents(configpath, outpath, header, split):
    """
    This function documents the management intents.

    :param configpath: The path to where the backup files are saved
    :param outpath: The path to save the Markdown document to
    :param header: Header of the configuration being documented
    :param split: Split documentation into multiple files
    """

    # If configurations path exists, continue
    if os.path.exists(configpath):
        if split:
            outpath = configpath + "/" + header + ".md"
            md_file(outpath)
        with open(outpath, 'a') as md:
            md.write('# ' + header + '\n')

        pattern = configpath + "*/*"
        for filename in sorted(glob.glob(pattern, recursive=True), key=str.casefold):
            # If path is Directory, skip
            if os.path.isdir(filename):
                continue
            # If file is .DS_Store, skip
            if filename == ".DS_Store":
                continue

            # Check which format the file is saved as then open file, load data and set query parameter
            with open(filename) as f:
                if filename.endswith(".yaml"):
                    data = json.dumps(yaml.safe_load(f))
                    repo_data = json.loads(data)
                elif filename.endswith(".json"):
                    f = open(filename)
                    repo_data = json.load(f)

                # Create assignments table
                assignments_table = ""
                assignments_table = assignment_table(repo_data)
                repo_data.pop('assignments', None)

                intent_settings_list = []
                for setting in repo_data['settingsDelta']:
                    setting_definition = setting['definitionId'].split("_")[1]
                    setting_definition = setting_definition[0].upper() + setting_definition[1:]
                    setting_definition = re.findall('[A-Z][^A-Z]*', setting_definition)
                    setting_definition = ' '.join(setting_definition)

                    vals = []
                    value = str(remove_characters(setting['valueJson']))
                    comma = re.findall('[:][^:]*', value)
                    for v in value.split(','):
                        v = v.replace(' ', '')
                        if comma:
                            v = f'**{v.replace(":", ":** ")}'
                        vals.append(v)
                    value = ",".join(vals)
                    value = value.replace(',', '<br />')


                    intent_settings_list.append([setting_definition,
                                                 value])

                repo_data.pop('settingsDelta')

                description = ""
                if 'description' in repo_data:
                    if repo_data['description'] is not None:
                        description = repo_data['description']
                        repo_data.pop('description')

                intent_table_list = []

                for key, value in zip(repo_data.keys(), clean_list(repo_data.values())):
                    key = key[0].upper() + key[1:]
                    key = re.findall('[A-Z][^A-Z]*', key)
                    key = ' '.join(key)

                    if value and isinstance(value, str):
                        if len(value.split(",")) > 1:
                            vals = []
                            for v in value.split(','):
                                v = v.replace(' ', '')
                                v = f'**{v.replace(":", ":** ")}'
                                vals.append(v)
                            value = ",".join(vals)
                            value = value.replace(',', '<br />')

                    intent_table_list.append([key, value])

                table = intent_table_list + intent_settings_list

                config_table = write_table(table)
                # Write data to file
                with open(outpath, 'a') as md:
                    if "displayName" in repo_data:
                        md.write('## ' + repo_data['displayName'] + '\n')
                    if "name" in repo_data:
                        md.write('## ' + repo_data['name'] + '\n')
                    if description:
                        md.write(f'Description: {description} \n')
                    if assignments_table:
                        md.write('### Assignments \n')
                        md.write(str(assignments_table) + '\n')
                    md.write(str(config_table) + '\n')


def get_md_files():
    """
    This function gets the Markdown files in the current directory.
    :return: List of Markdown files
    """

    md_files = []
    patterns = ["*/*.md", "*/*/*.md", "*/*/*/*.md"]
    for pattern in patterns:
        for filename in glob.glob(pattern, recursive=True):
            md_files.append(f'./{filename}')
    return md_files