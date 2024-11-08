import os
import re
import sys
import argparse
from typing import Dict, List, Tuple, Optional
from collections import defaultdict

p1 = re.compile(r'(\(property "Reference" )"([a-zA-Z]+[0-9]+)"')
p2 = re.compile(r'(\(reference )"([a-zA-Z]+[0-9]+)"')
p3 = re.compile(r'(fp_text reference )"([a-zA-Z]+[0-9]+)"')

def print_help(*args) -> str:
    """
    Show help text.
    """
    print(
        "\n"
        "kicad_designators.py\n"
        "====================\n"
        "This python script lists or modifies the designators in your KiCAD schematic and PCB\n"
        "files.\n"
        "\n"
        "Usage: python kicad_designators.py [options]\n"
        "\n"
        "Options:\n"
        "--------\n"
        "  -h, --help                                   Show this help message and exit.\n"
        "\n"
        "  -D DIRECTORY,                                Directory containing KiCAD schematic\n"
        "  --directory=DIRECTORY                        files to process. If not provided,\n"
        "                                               the current directory is used.\n"
        "\n"
        "  -i INCREMENT_DESIGNATOR,                     Designator to increment, eg. 'C3'.\n"
        "  --increment-designator=INCREMENT_DESIGNATOR\n"
        "\n"
        "  -d DECREMENT_DESIGNATOR,                     Designator to decrement, eg. 'C3'\n"
        "  --decrement-designator=DECREMENT_DESIGNATOR\n"
        "\n"
        "  -s, --show-designators                       Show designators and quit\n"
        "\n"
        "Examples:\n"
        "---------\n"
        "  Show the designators found in the schematic and PCB files in the current\n"
        "  directory:\n"
        "      > python kicad_designators.py -s\n"
        "\n"
        "  Increment the designator 'C3' (and all subsequent ones) in the schematic and PCB\n"
        "  files in the current directory:\n"
        "      > python kicad_designators.py -i C3\n"
        "\n"
        "  Decrement the designator 'R7' (and all subsequent ones) in the schematic and PCB\n"
        "  files in the current directory:\n"
        "      > python kicad_designators.py -d R7\n"
        "\n"
    )

def alphanumeric_sort_key(s: str) -> Tuple[str, int]:
    """
    Generate a sort key for alphanumeric strings by separating and identifying the alphabetical
    prefix and numerical suffix for proper sorting.
    
    Args:
        s (str): The alphanumeric string to be sorted.
        
    Returns:
        Tuple[str, int]: A tuple containing the alphabetical prefix and numerical suffix.
    """
    match = re.match(r"([a-zA-Z]+)([0-9]+)", s)
    return (match.group(1), int(match.group(2))) if match else (s, 0)

def extract_designator_prefix_and_number(designator: str) -> Tuple[str, int]:
    """
    Extract the prefix and numerical part of a designator.
    
    Args:
        designator (str): The designator to extract the prefix and numerical part from.
        
    Returns:
        Tuple[str, int]: A tuple containing the prefix and numerical part of the designator.
    """
    prefix, number = re.match(r"([a-zA-Z]+)([0-9]+)", designator).groups()
    return prefix, int(number)

def increment_and_filter_designators_in_dict(target_designator: str,
                                             orig_designator_dict: Dict[str, List[int]],
                                             increment: bool = True,
                                             ) -> Dict[str, List[int]]:
    """
    Increment or decrement in the given dictionary the numerical part of a specified designator and
    all subsequent designators with the same prefix.
    
    Args:
        target_designator (str):                The designator to increment.
        orig_designator_dict (Dict[str, int]):  A dictionary of designators with their positions
                                                in the file. For example:
                                                orig_designator_dict = {
                                                    'C39':  [2564, ]
                                                    'C40':  [2398, ]
                                                    'C41':  [1835, 2343, ]
                                                    'LED5': [2474, ]
                                                    'R25':  [2242, ]
                                                }
        
    Returns:
        Dict[str, int]: The updated dictionary with incremented designators.
    """
    # Extract the prefix and numerical part of the target designator
    t_prefix, t_num = extract_designator_prefix_and_number(target_designator)

    # Create a dictionary in the image of the original, but with incremented designators. Also,
    # filter out the designators that are irrelevant. If the target designator would be 'C40', then
    # only the designators 'C40', 'C41', ... would be incremented, the rest gets filtered out.
    updated_designator_dict: Dict[str, List[int]] = {}
    for d in sorted(orig_designator_dict.keys(), key=alphanumeric_sort_key):
        d_prefix, d_num = extract_designator_prefix_and_number(d)
        if d_prefix == t_prefix and d_num >= t_num:
            if increment:
                updated_designator_dict[f"{d_prefix}{d_num + 1}"] = orig_designator_dict[d]
            else:
                updated_designator_dict[f"{d_prefix}{d_num - 1}"] = orig_designator_dict[d]
        else:
            pass
            # updated_designator_dict[d] = orig_designator_dict[d]
        continue

    # Return the updated dictionary
    return updated_designator_dict

def process_file(filepath: str,
                 target_designator: Optional[str],
                 increment: bool,
                 ) -> None:
    """
    Process a KiCAD schematic or PCB file to increment specified designators. If a target designator
    is provided, increment it and update the file. Otherwise, it simply lists all designators found.
    
    Args:
        filepath (str): The file path of the KiCAD schematic file to process.
        target_designator (str): The designator to increment.
        increment (bool): If True, increment the designator. If False, decrement the designator.
    """
    print(f"\nProcessing {filepath}...")

    # Read the file and store its lines in the list `original_lines`
    with open(filepath, 'r') as file:
        original_lines = file.readlines()
    
    # Create a dictionary of designators and their positions in the file. The keys are the desig-
    # nators and the values are the line numbers where they are found. For example:
    # orig_designator_dict = {
    #   'C39':  [2564, ]
    #   'C40':  [2398, 1343, ]
    #   'C41':  [1835, ]
    #   'LED5': [2474, ]
    #   'R25':  [2242, ]
    # }
    orig_designator_dict: Dict[str, List[int]] = {}
    for i, line in enumerate(original_lines):
        for p in (p1, p2, p3):
            m = p.search(line)
            if m:
                if m.group(2) in orig_designator_dict:
                    orig_designator_dict[m.group(2)].append(i)
                else:
                    orig_designator_dict[m.group(2)] = [i]
                break
            continue
        continue

    # Modify the designator dictionary
    updated_designator_dict: Dict[str, List[int]] = increment_and_filter_designators_in_dict(
        target_designator    = target_designator,
        orig_designator_dict = orig_designator_dict,
        increment            = increment,
    )

    # Modify the file with the updated designators. To do that, loop over the lines in the file.
    # If line number i corresponds to line number j in the updated designator dictionary, then
    # substitute the designator in the line with the new designator and write the line back to
    # the file. Otherwise, just write the line back to the file as is.
    with open(filepath, 'w') as file:
        for i, line in enumerate(original_lines):
            for d_inc, j_list in updated_designator_dict.items():
                if i not in j_list:
                    continue
                for p in (p1, p2, p3):
                    m = p.search(line)
                    if m:
                        print(f"    line {i}: {line.strip()}", end=' => ')
                        line = p.sub(rf'\1"{d_inc}"', line)
                        print(f"{line.strip()}")
                        break
                    continue
                else:
                    assert False, f"  Designator not found in line {i}"
                continue
            file.write(line)
            continue
    return

def process_all_files(directory: str,
                      target_designator: Optional[str],
                      increment: bool,
                      ) -> None:
    """
    Process KiCAD schematic or PCB files in a directory to increment/decrement specified
    designators. If a target designator is provided, increment/decrement it and update the files.
    Otherwise, simply list all designators found.
    
    Args:
        directory (str): The directory containing KiCAD schematic files to process.
        target_designator (Optional[str]): The designator to increment, if provided.
        increment (bool): If True, increment the designator. If False, decrement the designator.
    """
    files = [f for f in os.listdir(directory) if f.endswith(('.kicad_sch', '.kicad_pcb'))]
    for filename in files:
        filepath = os.path.join(directory, filename)
        process_file(filepath, target_designator, increment)
        continue
    return

all_designators_cache: List[str] = []
def list_all_designators(directory: str) -> List[str]:
    """
    List all designators in the KiCAD schematic and PCB files in a directory.
    
    Args:
        directory (str): The directory containing KiCAD schematic files to process.
        
    Returns:
        List[str]: A list of all designators found in the files.
    """
    global all_designators_cache
    if all_designators_cache:
        return all_designators_cache
    files = [f for f in os.listdir(directory) if f.endswith(('.kicad_sch', '.kicad_pcb'))]
    all_designators: List[str] = []
    for filename in files:
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r') as file:
            lines = file.readlines()
        for line in lines:
            for p in (p1, p2, p3):
                m = p.search(line)
                if m:
                    all_designators.append(m.group(2))
                    break
                continue
            continue
        continue
    all_designators = list(set(all_designators))
    all_designators.sort(key=alphanumeric_sort_key)
    all_designators_cache = all_designators
    return all_designators

def check_operation_permitted(directory: str,
                              target_designator: str,
                              increment: bool,
                              ) -> bool:
    """
    Check if the operation is permitted. Decrementing the target designator is not permitted if this
    would result in a negative number or a duplicate.

    
    Args:
        directory (str): The directory containing KiCAD schematic files to process.
        target_designator (str): The designator to modify.
        increment (bool): If True, increment the designator. If False, decrement the designator.
        
    Returns:
        bool: True if the operation is permitted, False otherwise.
    """
    try:
        t_prefix, t_num = extract_designator_prefix_and_number(target_designator)
    except:
        print(
            f"The designator '{target_designator}' is not valid."
        )
        return False
    
    if increment:
        return True
    
    if t_num <= 1:
        print(
            f"The designator '{target_designator}' cannot be decremented. It would result in "
            f"zero or a negative number."
        )
        return False
    
    if f"{t_prefix}{t_num - 1}" in list_all_designators(directory):
        print(
            f"The designator '{target_designator}' cannot be decremented. "
            f"It would result in a duplicate."
        )
        return False
    
    return True

def check_designators_for_gaps(designator_list: List[str]) -> bool:
    """
    Check if the designators in the list have gaps. For example, if the list contains the
    designators 'C1', 'C2', 'C3', 'C5', 'C6', then a gap is found between 'C3' and 'C5'.

    Args:
        designator_list (List[str]): A list of designators to check for gaps.

    Returns:
        bool: True if gaps are found, False otherwise.
    """
    # Group designators by prefix
    grouped_designators = defaultdict(list)
    for designator in designator_list:
        prefix, number = extract_designator_prefix_and_number(designator)
        grouped_designators[prefix].append(number)

    # Check each group for gaps
    has_gaps = False
    for prefix, numbers in grouped_designators.items():
        numbers.sort()
        for i in range(1, len(numbers)):
            if numbers[i] - numbers[i-1] != 1:
                print(
                    f"Warning: Gap found in {prefix} series between "
                    f"'{prefix}{numbers[i-1]}' and '{prefix}{numbers[i]}'"
                )
                has_gaps = True

        # Check if the series starts from 1
        if numbers[0] != 1:
            print(
                f"Warning: {prefix} series starts from '{prefix}{numbers[0]}', number '1' is "
                f"missing."
            )
            has_gaps = True

    return has_gaps

if __name__ == '__main__':
    current_directory = os.getcwd()
    parser = argparse.ArgumentParser(description='Increment KiCAD designators.')

    # Add arguments to the parser
    parser.add_argument(
        '-D',
        '--directory',
        help='Directory containing KiCAD schematic files to process',
        default=current_directory
    )
    parser.add_argument(
        '-i',
        '--increment-designator',
        action='store',
        help='Designator to increment',
        default=None,
    )
    parser.add_argument(
        '-d',
        '--decrement-designator',
        action='store',
        help='Designator to decrement',
        default=None,
    )
    parser.add_argument(
        '-s',
        '--show-designators',
        action='store_true',
        help='Show designators and quit',
        default=None,
    )
    # Override the default help message with a custom one
    parser.print_help = print_help

    # Check if no arguments were provided. Show the help message in that case.
    if len(sys.argv) == 1:
        # Display the help message and exit
        parser.print_help(sys.stderr)
        sys.exit(1)

    # Parse the arguments
    args = parser.parse_args()
    
    # Check if the directory exists.
    if not os.path.isdir(args.directory):
        print(f"The directory '{args.directory}' does not exist.")
        exit(1)

    # If the --directory argument is provided, but none of the other arguments are provided, then
    # show the help message and quit.
    if not (args.increment_designator or args.decrement_designator or args.show_designators):
        parser.print_help(sys.stderr)
        exit(1)

    # If --show-designators is provided, just list all designators in the files. This also assumes
    # that --increment-designator and --decrement-designator are not provided. If they are provided
    # then show an error message and quit.
    if args.show_designators:
        if args.increment_designator or args.decrement_designator:
            print(
                "The options --increment-designator and --decrement-designator cannot be used with "
                "--show-designators."
            )
            exit(1)
        # process_all_files(args.directory)
        all_designators = list_all_designators(args.directory)
        print(all_designators)
        print("\n")
        print(f"Total designators found: {len(all_designators)}")
        print("\n")
        if not check_designators_for_gaps(all_designators):
            print("No gaps found in designators.")
        exit(0)

    # If --increment-designator or --decrement-designator is provided, then increment/decrement the
    # designator and update the files. if both are provided, then show an error message and quit.
    if args.increment_designator and args.decrement_designator:
        print(
            "The options --increment-designator and --decrement-designator cannot be used together."
        )
        exit(1)
    if args.increment_designator or args.decrement_designator:
        target = args.increment_designator if args.increment_designator else args.decrement_designator
        if not check_operation_permitted(args.directory, target, True if args.increment_designator else False):
            exit(1)
        print(
            f"\nYou are about to modify the designator '{target}' and all "
            f"subsequent ones in the '.kicad_sch' and '.kicad_pcb' files in the directory "
            f"'{args.directory}'. This action is irreversible and your KiCAD project becomes "
            f"unusable if anything goes wrong.\n\n"
        )
        response = input("Type 'yes' to confirm you made a backup of your KiCAD project: ")
        if response.lower() != 'yes':
            print("Exiting...")
            exit(0)
        response = input("Type 'yes' again to confirm you want to proceed with the modification: ")
        if response.lower() != 'yes':
            print("Exiting...")
            exit(0)
        if args.increment_designator:
            print(f"\nIncrementing designator '{target}'...")
            process_all_files(args.directory, target, True)
        if args.decrement_designator:
            print(f"\nDecrementing designator '{target}'...")
            process_all_files(args.directory, target, False)
        exit(0)
    exit(0)
