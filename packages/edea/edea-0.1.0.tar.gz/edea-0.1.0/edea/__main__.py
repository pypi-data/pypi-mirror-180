"""
edea command line tool

SPDX-License-Identifier: EUPL-1.2
"""
import argparse
import glob
import json
import os
import shutil
import sys
from logging import getLogger
from string import Template
from time import time
from typing import Dict

from edea.draw import draw_svg
from edea.edea import Schematic, Project, PCB
from edea.imgdiff import imgdiff
from edea.kicad_files import EMPTY_PROJECT
from edea.parser import from_str
from edea.types.parser import from_str as from_str_typed

parser = argparse.ArgumentParser(description='Tool to parse, render, and merge KiCad projects.')
pgroup = parser.add_mutually_exclusive_group()
pgroup.add_argument('--extract-meta', help='Extract metadata from KiCad project and output to stdout or to json file.',
                    action='store_true')
pgroup.add_argument('--merge', action='store_true', help='Merge the listed KiCad projects into a single project ('
                                                         'specify target directory with the output argument).')
parser.add_argument('--diff', action='store_true', help='Render visual differences of images stored in two different'
                                                        'directories, output the result to a third directory.'
                                                        'The image files must have the same file name.')
parser.add_argument('--render', action='store_true', help='Render kicad_sch or kicad_pcb to SVG.')
parser.add_argument('--output', type=str, nargs='?', default=False,
                    help="Specify output directory for merge, or output file for metadata extraction.")
parser.add_argument('projects', type=str, nargs='+',
                    help='Path(s) to the KiCad Project directory used as input.')
parser.add_argument('-adir', type=str, nargs='?', default=None, help='Visual diff input directory A')
parser.add_argument('-bdir', type=str, nargs='?', default=None, help='Visual diff input directory B')
parser.add_argument('-odir', type=str, nargs='?', default=None, help='Visual diff output directory')

args = parser.parse_args()

log = getLogger()

# what we need: schematic and pcb file, ideally find from kicad project file
# we don't need to parse project json to get top level file names; the project name is always (?) the filename
# of the top level schematic

if args.extract_meta:
    # parse the top-level schematic (and sub-schematics) plus the PCB file
    # and output metadata about it
    if len(args.projects) != 1:
        log.error("need exactly one KiCad Project, found %d", len(args.projects))
        sys.exit(7)  # argument list too long

    project_path = args.projects[0]
    if project_path.endswith('.kicad_pro'):
        path, _ = os.path.splitext(project_path)
        root_schematic = path + ".kicad_sch"
        root_pcb = path + ".kicad_pcb"
    elif os.path.isdir(project_path):
        path_lead, project_name = os.path.split(os.path.normpath(project_path))
        root_schematic = os.path.join(project_path, project_name + '.kicad_sch')
        root_pcb = os.path.join(project_path, project_name + '.kicad_pcb')
    else:
        log.error("No KiCad project directory or project file provided")
        sys.exit(22)  # invalid argument

    pro = Project(root_schematic, root_pcb)
    before = time()
    pro.parse()
    after = time()

    metadata = pro.metadata()
    metadata["parse_time"] = after - before

    print(json.dumps(metadata))

elif args.merge:
    if not args.output:
        log.error("output needs to be specified")
        sys.exit(22)  # invalid argument

    if os.path.isdir(args.output):
        _, output_name = os.path.split(os.path.normpath(args.output))
        output_path = args.output
    else:
        log.error('output path "%s" is not a directory', args.output)
        sys.exit(20)  # not a directory

    files = {}
    target_schematic = Schematic.empty()

    for path in args.projects:
        # detect whether it points to a project file or a project directory
        if path.endswith('.kicad_pro'):
            path_lead, _ = os.path.splitext(path)
            project_name = os.path.basename(path_lead)
            project_path = os.path.dirname(path)
        elif os.path.isdir(path):
            _, project_name = os.path.split(os.path.normpath(path))
            project_path = path
        else:
            log.error("%s doesn't point to a kicad project file or kicad project directory", path)
            sys.exit(2)  # no such file or directory

        if project_path not in files:
            files[project_path] = [{"project_name": project_name, "name": project_name}]
        else:
            # check if the first instance was already renamed
            if "renamed" not in files[project_path][0]:
                files[project_path][0]["name"] = f"{project_name} 1"
                files[project_path][0]["renamed"] = True

            # append another instance of the project
            files[project_path].append(
                {"project_name": project_name, "name": f"{project_name} {len(files[project_path]) + 1}"},
            )

    parsed_schematics: Dict[str, Schematic] = {}

    # now iterate all the (renamed) instances of the projects
    for project_path, obj in files.items():
        log.debug("merging schematic: %s %s", project_path, obj)

        # parse the schematic once, append as many times as needed
        root_schematic = os.path.join(project_path, obj[0]["project_name"] + '.kicad_sch')
        with open(root_schematic, encoding="utf-8") as f:
            expr = from_str(f.read())

            for instance in obj:
                name = instance["name"]
                project_name = instance['project_name']
                parsed_schematics[name] = Schematic(expr, name, f"{project_name}.kicad_sch")

    # TODO: get the sub-schematic uuid here and apply it to the right PCB first
    target_schematic.append(parsed_schematics)

    # TODO: merge PCB too
    for project_path, obj in files.items():
        log.debug("merging pcbs: %s %s", project_path, obj)

    # write the resulting schematic
    with open(f"{os.path.join(output_path, output_name)}.kicad_sch", "w", encoding="utf-8") as f:
        f.write(str(target_schematic.as_expr()))

    # copy over all the schematics from the modules
    for project_path, obj in files.items():
        instance = obj[0]
        files = glob.iglob(os.path.join(project_path, "*.kicad_sch"))
        for file in files:
            if os.path.isfile(file):
                shutil.copy2(file, output_path)

    # TODO: write merged PCB file to the output

    # generate project file
    with open(f"{os.path.join(output_path, output_name)}.kicad_pro", "w", encoding="utf-8") as f:
        s = Template(EMPTY_PROJECT)
        f.write(s.substitute(project_name=output_name))

elif args.diff:
    input_dir_a = args.projects[0]
    input_dir_b = args.projects[1]
    output_dir = args.output

    file_lists = {
        "a": [],
        "b": [],
        "o": [],
        "A": [],
        "B": [],
    }

    for dirlabel, dirpath in [('a', input_dir_a), ('b', input_dir_b)]:
        with os.scandir(dirpath) as dir_iterator:
            for entry in dir_iterator:
                if entry.is_file() and (entry.name.endswith('.png') or entry.name.endswith('.svg')):
                    file_lists[dirlabel].append(entry.name)

    common_files = set(file_lists['a']).intersection(file_lists['b'])

    stats = []

    for fn in common_files:
        for dirlabel, dirpath in [('A', input_dir_a), ('B', input_dir_b), ('o', output_dir)]:
            file_lists[dirlabel].append(os.path.join(dirpath, fn if dirlabel != 'o' else fn[:-4] + '.png'))
        stats.append({'fn': fn})

    for idx in range(len(common_files)):
        params = []
        for identifier in 'ABo':
            params.append(file_lists[identifier][idx])
        stats[idx]['difference_pct'] = imgdiff(*tuple(params))

    with open(os.path.join(output_dir, 'stats.json'), 'wt', encoding='utf-8') as of:
        of.write(json.dumps(stats))

elif args.render:
    input_file = args.projects[0]
    file_name, ext = os.path.splitext(os.path.basename(input_file))
    ext = ext.lower()

    if os.path.isdir(args.output):
        output_file = os.path.join(args.output, file_name, ".svg")
    else:
        output_file = args.output

    with open(input_file, encoding="utf-8") as f:
        if ext == ".kicad_sch":
            typed_sch = from_str_typed(f.read())
            svg = draw_svg(typed_sch)
        elif ext == ".kicad_pcb":
            pcb = PCB(from_str(f.read()), "", "")
            svg = pcb.draw()
        else:
            raise NotImplementedError("can only render kicad_sch or kicad_pcb")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(svg.as_str())

else:
    log.error("only merge and metadata extraction are implemented for now")
    sys.exit(1)
