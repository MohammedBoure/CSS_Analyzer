import cssutils
import os
from collections import defaultdict
import argparse
import logging

# Configure cssutils to suppress warnings and disable strict validation
cssutils.log.setLevel(logging.ERROR)  # Only show critical errors
cssutils.ser.prefs.useMinified()  # Optional: Cleaner output for shared_rules.css

def parse_css_files(directory):
    """Parse all CSS files in the given directory and return a dictionary of rules."""
    rules_dict = {}
    try:
        # Parse with validation disabled to support modern CSS
        sheet = cssutils.parseFile(directory, validate=False)
        for rule in sheet:
            if isinstance(rule, cssutils.css.CSSStyleRule):
                selector = rule.selectorText
                if not selector or not rule.style:  # Skip invalid or empty selectors/rules
                    continue
                properties = []
                for prop in rule.style:
                    # Include all properties, even modern ones or custom properties
                    properties.append(f"{prop.name}: {prop.value};")
                if properties:  # Only add rules with properties
                    rules_dict[selector] = tuple(sorted(properties))  # Sort for consistent comparison
        return rules_dict
    except Exception as e:
        print(f"Error parsing {directory}: {e}")
        return {}

def find_duplicate_rules(css_files_data):
    """Find rules that are duplicated across different CSS files."""
    selector_rules_count = defaultdict(list)
    for filename, rules in css_files_data.items():
        for selector, properties in rules.items():
            selector_rules_count[(selector, properties)].append(filename)
    
    # Filter for rules that appear in more than one file
    duplicate_rules = {
        (selector, properties): files for (selector, properties), files in selector_rules_count.items()
        if len(files) > 1
    }
    return duplicate_rules

def create_shared_rules_file(duplicate_rules, output_dir, output_file="shared_rules.css"):
    """Create a new CSS file with the shared rules in the specified directory."""
    if not duplicate_rules:
        print(f"No duplicate rules to write in {output_dir}")
        return
    output_path = os.path.join(output_dir, output_file)
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("/* Shared CSS Rules */\n\n")
            for (selector, properties), files in duplicate_rules.items():
                # Use relative paths for clarity in comments
                relative_files = [os.path.relpath(f, output_dir) for f in files]
                f.write(f"/* Used in: {', '.join(relative_files)} */\n")
                f.write(f"{selector} {{\n")
                for prop in properties:
                    f.write(f"    {prop}\n")
                f.write("}\n\n")
        print(f"Shared rules have been written to {output_path}")
    except Exception as e:
        print(f"Error writing to {output_path}: {e}")

def process_directory(root_dir):
    """Process all CSS files in the directory and its subdirectories recursively."""
    for dirpath, _, filenames in os.walk(root_dir):
        # Filter CSS files in the current directory
        css_files = [f for f in filenames if f.endswith('.css')]
        if len(css_files) < 2:
            print(f"Skipping {dirpath}: Fewer than 2 CSS files found ({len(css_files)})")
            continue

        # Parse CSS files in the current directory
        css_files_data = {}
        for filename in css_files:
            file_path = os.path.join(dirpath, filename)
            rules = parse_css_files(file_path)
            if rules:
                css_files_data[file_path] = rules
                print(f"Parsed {file_path}: {len(rules)} rules found")

        if not css_files_data:
            print(f"No valid CSS files found in {dirpath}")
            continue

        # Debugging: Print parsed files and rule counts
        print(f"\nProcessing directory: {dirpath}")
        print(f"Total CSS files parsed: {len(css_files_data)}")
        for filename, rules in css_files_data.items():
            print(f"{os.path.relpath(filename, dirpath)}: {len(rules)} rules")

        # Find duplicate rules
        duplicate_rules = find_duplicate_rules(css_files_data)
        if not duplicate_rules:
            print(f"No duplicate rules found in {dirpath}")
            continue

        # Debugging: Print duplicate rules
        print(f"Found {len(duplicate_rules)} duplicate rules in {dirpath}:")
        for (selector, _), files in duplicate_rules.items():
            relative_files = [os.path.relpath(f, dirpath) for f in files]
            print(f"Selector '{selector}' found in: {', '.join(relative_files)}")

        # Create shared rules file in the current directory
        create_shared_rules_file(duplicate_rules, dirpath)

def main():
    parser = argparse.ArgumentParser(description="Analyze CSS files recursively and extract shared rules.")
    parser.add_argument("directory", help="Root directory containing CSS files")
    args = parser.parse_args()

    # Ensure the directory exists
    if not os.path.isdir(args.directory):
        print(f"Error: {args.directory} is not a valid directory")
        return

    # Process the directory and its subdirectories
    process_directory(args.directory)

if __name__ == "__main__":
    main()