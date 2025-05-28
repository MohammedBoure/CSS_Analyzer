# Changelog

## [Unreleased]

## Initial Commit - CSS Duplicate Rules Analyzer

### Added
- `main.py`: Python script to recursively scan directories for CSS files, identify duplicate CSS rules across multiple files, and generate a consolidated `shared_rules.css` file in directories containing duplicates.
- Support for modern CSS properties (e.g., flexbox, grid, rem units, CSS variables `var()`) by disabling strict validation in `cssutils`.
- Detailed `README.md` file containing:
  - Installation instructions
  - Usage guidelines
  - Example output
  - Troubleshooting tips
  - Arabic summary section for better accessibility and localization
- Debug output showing:
  - Number of parsed CSS files
  - Rule counts per file
  - Detected duplicate CSS rules across files

### Changed
- Configured `cssutils` to suppress warnings and errors for a cleaner output.

---
