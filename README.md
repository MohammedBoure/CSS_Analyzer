# CSS Duplicate Rules Analyzer

**بالعربية**: أداة لتحليل ملفات CSS واستخراج القواعد المكررة  
هذه الأداة تقوم بفحص ملفات CSS داخل مجلد وفروعه بشكل تكراري، وتحدد القواعد المشتركة بين ملفات CSS متعددة، ثم تنشئ ملف `shared_rules.css` في كل مجلد يحتوي على قواعد مكررة.

## Overview
The **CSS Duplicate Rules Analyzer** is a Python tool that recursively scans directories for CSS files, extracts their selectors and properties, identifies duplicate rules (identical selectors with identical properties) across multiple files, and generates a `shared_rules.css` file in each directory containing duplicate rules. This helps reduce code redundancy and improve CSS organization.

## Features
- Recursively scans directories and subdirectories for `.css` files.
- Supports modern CSS properties (e.g., `flex`, `grid`, `rem`, `var()`) using `cssutils` with validation disabled.
- Identifies duplicate rules across multiple CSS files.
- Creates a `shared_rules.css` file in each directory with duplicate rules, including comments indicating the source files.
- Provides detailed debugging output for parsed files and rules.

## Prerequisites
- **Python 3.6+**: Ensure Python is installed on your system.
- **cssutils**: A Python library for parsing CSS files.

## Installation
1. Clone or download this repository:
   ```bash
   git clone https://github.com/<your-username>/css-duplicate-analyzer.git
   cd css-duplicate-analyzer
   ```
2. Install the required Python package:
   ```bash
   pip install cssutils
   ```

## Usage
Run the script with the path to the directory containing CSS files:
```bash
python main.py /path/to/css/directory
```
Example:
```bash
python main.py ~/Desktop/EduConnect-FrontEnd/
```

### What It Does
1. The script recursively scans the specified directory and its subdirectories for `.css` files.
2. For each directory with at least two CSS files:
   - Parses the CSS files and extracts selectors and their properties.
   - Identifies rules that are identical across multiple files.
   - Creates a `shared_rules.css` file in that directory, listing the duplicate rules with comments indicating the source files.
3. Outputs debugging information, including the number of files parsed, rules extracted, and duplicates found.

### Example Directory Structure
```
/path/to/css/
├── styles.css
├── components/
│   ├── button.css
│   ├── header.css
├── pages/
│   ├── home.css
│   ├── profile.css
```

If `button.css` and `header.css` both contain:
```css
.button {
    color: blue;
    font-size: 1rem;
}
```
A `shared_rules.css` file will be created in the `components/` directory:
```css
/* Shared CSS Rules */

/* Used in: button.css, header.css */
.button {
    color: blue;
    font-size: 1rem;
}
```

## Example Output
```
Skipping /path/to/css/: Fewer than 2 CSS files found (1)
Parsed /path/to/css/components/button.css: 5 rules found
Parsed /path/to/css/components/header.css: 8 rules found

Processing directory: /path/to/css/components
Total CSS files parsed: 2
button.css: 5 rules
header.css: 8 rules
Found 1 duplicate rules in /path/to/css/components:
Selector '.button' found in: button.css, header.css
Shared rules have been written to /path/to/css/components/shared_rules.css
```

## Notes
- The script requires at least two CSS files in a directory to detect duplicates.
- Modern CSS properties (e.g., `flex`, `grid`, `var()`) are supported by disabling strict validation in `cssutils`.
- If no duplicates are found, the script will inform you for each directory processed.
- Ensure you have write permissions in the directories where `shared_rules.css` will be created.

## Troubleshooting
- **No duplicates found**: Verify that multiple CSS files exist in the same directory and contain identical selectors with identical properties. Use `find /path/to/css -type f -name "*.css"` to list all CSS files.
- **Parsing errors**: If errors occur, ensure `cssutils` is up-to-date (`pip install --upgrade cssutils`). Share the error output for assistance.
- **Complex CSS**: The script focuses on standard CSS rules (`CSSStyleRule`). For support with `@media`, `@keyframes`, etc., additional customization may be needed.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue to suggest improvements or report bugs.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact
For questions or support, contact the maintainer at [your-email@example.com] or open an issue on GitHub.