import os
import re
import argparse
from typing import Dict, List, Tuple, Optional

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

def increment_and_filter_designators_in_dict(target_designator: str,
                                             orig_designator_dict: Dict[str, List[int]],
                                             ) -> Dict[str, List[int]]:
    """
    Increment in the given dictionary the numerical part of a specified designator and all sub-
    sequent designators with the same prefix.
    
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
    t_prefix, t_num = re.match(r"([a-zA-Z]+)([0-9]+)", target_designator).groups()
    t_num = int(t_num)

    # Create a dictionary in the image of the original, but with incremented designators. Also,
    # filter out the designators that are irrelevant. If the target designator would be 'C40', then
    # only the designators 'C40', 'C41', ... would be incremented, the rest gets filtered out.
    updated_designator_dict: Dict[str, List[int]] = {}
    for d in sorted(orig_designator_dict.keys(), key=alphanumeric_sort_key):
        d_prefix, d_num = re.match(r"([a-zA-Z]+)([0-9]+)", d).groups()
        d_num = int(d_num)
        if d_prefix == t_prefix and d_num >= t_num:
            updated_designator_dict[f"{d_prefix}{d_num + 1}"] = orig_designator_dict[d]
        else:
            pass
            # updated_designator_dict[d] = orig_designator_dict[d]
        continue

    # Return the updated dictionary
    return updated_designator_dict

def process_file(filepath: str,
                 target_designator: Optional[str] = None,
                 ) -> None:
    """
    Process a KiCAD schematic or PCB file to increment specified designators. If a target designator
    is provided, increment it and update the file. Otherwise, it simply lists all designators found.
    
    Args:
        filepath (str): The file path of the KiCAD schematic file to process.
        target_designator (Optional[str]): The designator to increment, if provided.
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
    p1 = re.compile(r'(\(property "Reference" )"([a-zA-Z]+[0-9]+)"')
    p2 = re.compile(r'(\(reference )"([a-zA-Z]+[0-9]+)"')
    p3 = re.compile(r'(fp_text reference )"([a-zA-Z]+[0-9]+)"')

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

    if target_designator:
        # Modify the designator dictionary
        updated_designator_dict: Dict[str, List[int]] = increment_and_filter_designators_in_dict(
            target_designator    = target_designator,
            orig_designator_dict = orig_designator_dict,
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
    else:
        # Just list all designators without modifying anything
        designators = list(orig_designator_dict.keys())
        designators.sort(key=alphanumeric_sort_key)
        print(designators)
    return

def process_all_files(directory: str,
                      target_designator: Optional[str] = None,
                      ) -> None:
    """
    Processes KiCAD schematic files in a directory to increment specified designators.
    If a target designator is provided, increments it and updates the files.
    Otherwise, it simply lists all designators found.
    
    Args:
        directory (str): The directory containing KiCAD schematic files to process.
        target_designator (Optional[str]): The designator to increment, if provided.
    """
    files = [f for f in os.listdir(directory) if f.endswith(('.kicad_sch', '.kicad_pcb'))]
    for filename in files:
        filepath = os.path.join(directory, filename)
        process_file(filepath, target_designator)
        continue
    return

if __name__ == '__main__':
    current_directory = os.getcwd()
    parser = argparse.ArgumentParser(description='Increment KiCAD designators.')
    parser.add_argument(
        '-d',
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
    args = parser.parse_args()

    if args.increment_designator:
        print(
            f"\nYou are about to increment the designator '{args.increment_designator}' and all "
            f"subsequent ones in the '.kicad_sch' and '.kicad_pcb' files in the directory "
            f"'{args.directory}'. This action is irreversible and your KiCAD project becomes "
            f"unusable if anything goes wrong.\n\n"
        )
        response = input("Type 'yes' to confirm you made a backup of your KiCAD project: ")
        if response.lower() != 'yes':
            print("Exiting...")
            exit(0)
        response = input("Type 'yes' again to confirm you want to proceed with the increment: ")
        if response.lower() != 'yes':
            print("Exiting...")
            exit(0)
        print(f"\nIncrementing designator {args.increment_designator}...")
    
    process_all_files(args.directory, args.increment_designator)
