# CSS Analyzer

![CSS Analyzer](https://img.shields.io/badge/CSS-Analyzer-blue)  
**CSS Analyzer** is a Python tool designed to analyze and optimize CSS files by removing duplicate rules and properties, generating detailed reports, and maintaining readable formatting.

## Features
- **Duplicate Rule Removal**: Detects and removes duplicate CSS rules across multiple files, consolidating them into a `shared_rules.css` file.
- **Duplicate Property Removal**: Eliminates redundant properties within rules in the same file (e.g., multiple `color: blue;` declarations).
- **Readable Formatting**: Ensures modified CSS files retain clean formatting with 2-space indentation and proper line breaks.
- **Detailed Reporting**: Generates a `css_analysis_report.md` file with statistics on parsed files, rules, duplicates, and removed properties.
- **Tool Attribution**: Includes tool metadata (name, repository, script path) in output files.
- **Flexible Exclusions**: Supports excluding specific directories and files during analysis.

## Requirements
- Python 3.6 or higher
- `cssutils` library (`pip install cssutils`)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/MohammedBoure/CSS_Analyzer.git
   cd CSS_Analyzer
   ```
2. Install dependencies:
   ```bash
   pip install cssutils
   ```

## Usage
Run the tool on a directory containing CSS files:
```bash
python main.py <directory_path> [--exclude-dirs <dirs>] [--exclude-files <files>]
```
- `<directory_path>`: Path to the directory with CSS files.
- `--exclude-dirs`: Directories to exclude (e.g., `node_modules`).
- `--exclude-files`: CSS files to exclude.

### Example
Analyze CSS files in a directory, excluding specific folders:
```bash
python main.py ./css_project --exclude-dirs node_modules .git
```

### Outputs
- ** `shared_rules.css`**: Created in directories with duplicate rules, containing consolidated rules with source comments.
  - Example:
    ```css
    /* Shared CSS Rules generated by CSS Analyzer (Python tool)
       Tool path: /path/to/CSS_Analyzer/main.py
       Generated on: 2025-05-28 15:31:45 */

    /* Used in: style.css, theme.css */
    :root {
      --primary-color: #007bff;
      --secondary-color: #6c757d;
    }
    ```
- ** `css_analysis_report.md`**: Generated in the root directory, detailing analysis statistics and tool information.
  - Example:
    ```markdown
    # CSS Analysis Report

    Generated on: 2025-05-28 15:31:45
    Processed by: CSS Analyzer (Python tool)
    Tool path: /path/to/CSS_Analyzer/main.py

    ## Directory: css
    - **CSS Files Parsed**: 5
    - **Total Rules Found**: 200
    - **Duplicate Rules Found**: 20
    - **Duplicate Properties Removed**: 10
    - **Shared Rules File**: css/shared_rules.css
    - **Modified Files**:
      - css/style.css (Properties removed: 5)
      ...

    ## Processing Status
    Analysis completed successfully on 2025-05-28 15:31:45.

    ## Tool and Analysis Information
    - **Tool Name**: CSS Analyzer
    - **Repository**: https://github.com/MohammedBoure/CSS_Analyzer
    - **Tool Path**: /path/to/CSS_Analyzer/main.py
    ```

## Contributing
To contribute:
1. Fork the repository.
2. Create a branch (`git checkout -b feature/new-feature`).
3. Make and test changes.
4. Commit (`git commit -m "Describe changes"`).
5. Submit a pull request.

Open an issue for bugs or feature suggestions. Follow PEP 8 and include clear documentation.

## License
Licensed under the [MIT License](LICENSE). See `LICENSE` for details.

## Contact
- **Repository**: [https://github.com/MohammedBoure/CSS_Analyzer](https://github.com/MohammedBoure/CSS_Analyzer)
- **Developer**: Mohammed Boure
- **Issues**: Use GitHub Issues for support

---

# أداة تحليل CSS

![CSS Analyzer](https://img.shields.io/badge/CSS-Analyzer-blue)  
**أداة تحليل CSS** هي أداة Python لتحليل وتحسين ملفات CSS عن طريق إزالة القواعد والخصائص المكررة، إنشاء تقارير مفصلة، والحفاظ على تنسيق مقروء.

## الخصائص
- **إزالة القواعد المكررة**: اكتشاف وإزالة القواعد المكررة عبر ملفات CSS، مع تجميعها في ملف `shared_rules.css`.
- **إزالة الخصائص المكررة**: حذف الخصائص المكررة داخل القواعد في نفس الملف (مثل `color: blue;` المتكرر).
- **تنسيق مقروء**: الحفاظ على تنسيق CSS أنيق بمسافات بادئة (مسافتين) وفواصل أسطر.
- **تقارير مفصلة**: إنشاء ملف `css_analysis_report.md` بإحصائيات عن الملفات، القواعد، والخصائص المحذوفة.
- **معلومات الأداة**: تضمين بيانات الأداة (الاسم، المستودع، مسار السكربت) في المخرجات.
- **استثناءات مرنة**: دعم استثناء المجلدات والملفات أثناء التحليل.

## المتطلبات
- Python 3.6 أو أحدث
- مكتبة `cssutils` (`pip install cssutils`)

## التثبيت
1. استنسخ المستودع:
   ```bash
   git clone https://github.com/MohammedBoure/CSS_Analyzer.git
   cd CSS_Analyzer
   ```
2. ثبت المتطلبات:
   ```bash
   pip install cssutils
   ```

## الاستخدام
شغّل الأداة على مجلد يحتوي على ملفات CSS:
```bash
python main.py <مسار_المجلد> [--exclude-dirs <مجلدات>] [--exclude-files <ملفات>]
```
- `<مسار_المجلد>`: مسار المجلد الذي يحتوي على ملفات CSS.
- `--exclude-dirs`: المجلدات المستثناة (مثل `node_modules`).
- `--exclude-files`: ملفات CSS المستثناة.

### مثال
تحليل ملفات CSS في مجلد مع استثناء مجلدات:
```bash
python main.py ./css_project --exclude-dirs node_modules .git
```

### المخرجات
- **ملف `shared_rules.css`**: يُنشأ في المجلدات التي تحتوي على قواعد مكررة، مع تعليقات توضح المصادر.
  - مثال:
    ```css
    /* Shared CSS Rules generated by CSS Analyzer (Python tool)
       Tool path: /path/to/CSS_Analyzer/main.py
       Generated on: 2025-05-28 15:31:45 */

    /* Used in: style.css, theme.css */
    :root {
      --primary-color: #007bff;
      --secondary-color: #6c757d;
    }
    ```
- **تقرير `css_analysis_report.md`**: يُنشأ في المجلد الجذر، يحتوي على إحصائيات التحليل ومعلومات الأداة.
  - مثال:
    ```markdown
    # CSS Analysis Report

    Generated on: 2025-05-28 15:31:45
    Processed by: CSS Analyzer (Python tool)
    Tool path: /path/to/CSS_Analyzer/main.py

    ## Directory: css
    - **CSS Files Parsed**: 5
    - **Total Rules Found**: 200
    - **Duplicate Rules Found**: 20
    - **Duplicate Properties Removed**: 10
    - **Shared Rules File**: css/shared_rules.css
    - **Modified Files**:
      - css/style.css (Properties removed: 5)
      ...

    ## Processing Status
    Analysis completed successfully on 2025-05-28 15:31:45.

    ## Tool and Analysis Information
    - **Tool Name**: CSS Analyzer
    - **Repository**: https://github.com/MohammedBoure/CSS_Analyzer
    - **Tool Path**: /path/to/CSS_Analyzer/main.py
    ```

## المساهمة
للمساهمة:
1. قم بعمل Fork للمستودع.
2. أنشئ فرعًا (`git checkout -b feature/ميزة_جديدة`).
3. نفّذ واختبر التغييرات.
4. ارفع التغييرات (`git commit -m "وصف التغيير"`).
5. قدّم Pull Request.

افتح Issue للإبلاغ عن أخطاء أو اقتراح ميزات. التزم بـ PEP 8 وأضف توثيقًا واضحًا.

## الترخيص
مرخص بموجب [MIT License](LICENSE). راجع ملف `LICENSE` للتفاصيل.

## التواصل
- **المستودع**: [https://github.com/MohammedBoure/CSS_Analyzer](https://github.com/MohammedBoure/CSS_Analyzer)
- **المطور**: Mohammed Boure
- **الدعم**: استخدم GitHub Issues