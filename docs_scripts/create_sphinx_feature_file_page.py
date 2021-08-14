#!/usr/bin/env python3
import sys
import json
import pathlib
from os import path
from screenplay.behave_extensions.collecting_formatter import CollectedFeature, CollectedStep
from jinja2 import Template


status_to_style_dict = {
    'not run': 'notrun',
    # behave.model_core.Status
    'untested': 'notrun',
    'skipped': 'notrun',
    'passed': 'passed',
    'failed': 'failed',
    'undefined': 'notimplemented',
    'executing': 'notrun'
}


def status_to_style(status):
    return status_to_style_dict.get(status, 'failed')


def screenshots_from_step(step: CollectedStep):
    screenshots = []
    for line in step.text:
        line_text: str = line.strip()
        line_split = line_text.split("'")
        if len(line_split) == 3 and line_split[0] == 'Save screenshot ':
            screenshots.append(line_split[1])
    return screenshots


def read_template():
    template_path = path.join(pathlib.Path(__file__).parent.absolute(), 'feature.template')
    if not path.exists(template_path):
        print('Unable to find template\n')
        exit(2)

    with open(template_path) as file:
        return file.read()


def read_feature():
    feature_path = sys.argv[1]
    if not path.exists(feature_path):
        print('Unable to find feature file\n')
        exit(2)

    with open(feature_path, 'rt') as file:
        return CollectedFeature.from_json(json.load(file))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Invalid command format, format is:\n {a[0]} <json feature result>\n'.format(a=sys.argv))
        exit(1)

    template = read_template()
    feature = read_feature()

    context = {
        "feature": feature,
        "status_to_style": status_to_style,
        "screenshots_from_step": screenshots_from_step
    }

    (file_name, _) = path.splitext(sys.argv[1])
    file_name += '.rst'

    with open(file_name, 'wt') as file:
        file.write(Template(template).render(**context))
