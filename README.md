# 🎭 Playwright with Python - Complete Learning Guide

## 📚 Table of Contents
- [Project Setup](#project-setup)
- [Test Cases Overview](#test-cases-overview)
- [Learning Topics](#learning-topics)
- [How to Run Tests](#how-to-run-tests)
- [Quick Reference](#quick-reference)

---

## 🚀 Project Setup

### Prerequisites
- Python 3.13+
- Virtual Environment

### Installation Steps
```bash
# Navigate to project directory
cd /Users/harshal/PycharmProjects/PythonProject/Playwright_Pytest_Python

# Activate virtual environment
source activate.sh
# OR manually: source venv/bin/activate

# Install dependencies (already done)
pip install -r requirements.txt

# Install browsers (already done)
playwright install
```

---

## 📋 Test Cases Overview

### 🔰 **Test 01: Playwright Basics** (`test_01playwrightBasics.py`)
**What you'll learn:**
- Basic Playwright setup and browser launching
- Page navigation and simple interactions
- Different ways to create browser instances
- Cross-browser testing (Chrome vs Firefox)

**Key Concepts:**
- `playwright.chromium.launch()` - Launch Chrome browser
- `browser.new_context()` - Create isolated browser session
- `page.goto()` - Navigate to URL
- `page.get_by_label()` - Find elements by label text
- `expect().to_be_visible()` - Assertions

---

### 🛒 **Test 02: E-commerce Application** (`test_02Ecom_Application.py`)
**What you'll learn:**
- Real-world application testing
- Product selection and checkout flow
- Element filtering and counting

**Key Concepts:**
- `page.filter(has_text="...")` - Filter elements by text
- `expect().to_have_count()` - Count assertions
- E-commerce workflow automation

---

### 🪟 **Test 03: Window Handling** (`test_03WindowHandle.py`)
**What you'll learn:**
- Handle popup windows and new tabs
- Switch between multiple browser windows
- Extract data from child windows

**Key Concepts:**
- `page.expect_popup()` - Handle new window/tab
- `pageinfo.value` - Access popup window
- Window switching and data extraction

---

### 🚨 **Test 04: Alert Handling** (`test_04Alert.py`)
**What you'll learn:**
- Handle JavaScript alerts, confirms, and prompts
- Accept/dismiss dialogs
- Show/hide element interactions

**Key Concepts:**
- `page.on("dialog", lambda d: d.accept())` - Accept alerts
- `page.on("dialog", lambda d: d.dismiss())` - Dismiss alerts
- `page.on("dialog", lambda d: d.accept("text"))` - Handle prompts
- `expect().to_be_hidden()` - Visibility assertions

---

### 🖼️ **Test 05: Frame Handling** (`test_05Frames.py`)
**What you'll learn:**
- Work with iframes and nested frames
- Switch context between main page and frames

**Key Concepts:**
- `page.frame_locator("#iframe-id")` - Access iframe
- Frame context switching
- Interacting with elements inside frames

---

### 🖱️ **Test 06: Mouse Hover** (`test_06MouseHover.py`)
**What you'll learn:**
- Mouse hover actions
- Reveal hidden menus on hover
- Mouse interaction patterns

**Key Concepts:**
- `page.locator().hover()` - Mouse hover
- Hover-triggered element visibility
- Menu navigation with hover

---

### 🤖 **Test 07: Code Generation** (`test_07CodeGen.py`)
**What you'll learn:**
- Playwright's code generation feature
- Auto-generate test scripts from browser interactions

**Key Concepts:**
- `playwright codegen` - Generate code automatically
- Different target languages (Python, JavaScript)
- Recording user interactions

---

### 📊 **Test 08: Web Table Handling** (`test_08WebTable.py`)
**What you'll learn:**
- Extract data from HTML tables
- Iterate through table rows and columns
- Search for specific data in tables

**Key Concepts:**
- `page.locator("//table/tbody/tr").count()` - Count table rows
- `page.locator(f"//tr[{i}]/td[{j}]").inner_text()` - Extract cell data
- Table data iteration and searching

---

### 📸 **Test 09: Screenshots & Videos** (`test_09ScreeenShot&Video.py`)
**What you'll learn:**
- Capture screenshots (full page and element-level)
- Record test execution videos
- Visual testing capabilities

**Key Concepts:**
- `page.screenshot(path="image.png")` - Take screenshots
- `record_video_dir="videos/"` - Record videos
- `full_page=True` - Full page screenshots

---

### 🎯 **Test 10: Advanced Actions** (`test_10DD_Scroll_DbClick_Click.py`)
**What you'll learn:**
- Double-click actions
- Right-click (context menu)
- Drag and drop operations
- Page scrolling techniques

**Key Concepts:**
- `page.dblclick()` - Double click
- `page.click(button="right")` - Right click
- `page.drag_and_drop(source, target)` - Drag & drop
- `page.mouse.wheel()` - Scrolling
- `scroll_into_view_if_needed()` - Smart scrolling

---

### ⌨️ **Test 11: Keyboard Actions** (`test_11KeyBoardActions.py`)
**What you'll learn:**
- Keyboard input simulation
- Key combinations and shortcuts
- Text typing vs key pressing

**Key Concepts:**
- `page.locator().type("text")` - Type text
- `page.keyboard.press("Enter")` - Press keys
- `page.keyboard.down("Shift")` - Hold keys

---

### 🔗 **Test 12: Broken Links** (`test_12BrokenLinks.py`)
**What you'll learn:**
- Identify and test broken links
- HTTP status code validation
- Link accessibility testing

**Key Concepts:**
- Link validation techniques
- HTTP response checking
- Accessibility testing

---

### 📋 **Test 13: Dropdown Handling** (`test_13dropdown.py`)
**What you'll learn:**
- Handle different types of dropdowns
- Select by value, label, or index
- Multi-select dropdowns

**Key Concepts:**
- `select_option(value="...")` - Select by value
- `select_option(label="...")` - Select by visible text
- `select_option(index=...)` - Select by index
- `select_option(['option1', 'option2'])` - Multi-select

---

### 🧭 **Test 14: Browser Navigation** (`test_14BrowserNavigation.py`)
**What you'll learn:**
- Browser navigation controls
- Back, forward, and refresh operations
- Navigation history management

**Key Concepts:**
- `page.go_back()` - Navigate back
- `page.go_forward()` - Navigate forward
- `page.reload()` - Refresh page

---

### 🎯 **Test 15: XPath Locators** (`test_15Xpath.py`)
**What you'll learn:**
- Advanced XPath expressions
- Complex element location strategies
- XPath axes and functions

**Key Concepts:**
- `//input[@id='element']` - Basic XPath
- `//input[contains(@id,'partial')]` - Contains function
- `//parent::div/child::button` - XPath axes
- `//following-sibling::div` - Sibling navigation

---

### ☑️ **Test 16: Checkboxes** (`test_16Checkboxes.py`)
**What you'll learn:**
- Checkbox selection and validation
- Multiple checkbox handling
- Checkbox state verification

**Key Concepts:**
- `page.locator("input[type='checkbox']")` - Find checkboxes
- `checkbox.nth(i).click()` - Select specific checkbox
- `is_checked()` - Verify checkbox state
- Bulk checkbox operations

---

### ✅ **Test 17: Assertions** (`test_17AssertionPW.py`)
**What you'll learn:**
- Playwright's built-in assertions
- Element state verification
- Page-level assertions

**Key Concepts:**
- `expect(page).to_have_title()` - Page title assertion
- `expect(page).to_have_url()` - URL assertion
- `expect(element).to_have_text()` - Text assertion
- `expect(element).to_have_id()` - Attribute assertion
- `is_enabled()`, `is_checked()` - State checking

---

### 🎚️ **Test 18: Sliders & Resizable** (`test_18Sliders_Resizeable.py`)
**What you'll learn:**
- Handle slider controls
- Resizable element manipulation
- Mouse coordinate calculations

**Key Concepts:**
- `element.bounding_box()` - Get element dimensions
- `page.mouse.move()` - Mouse movement
- `page.mouse.down()` / `page.mouse.up()` - Mouse actions
- Coordinate-based interactions

---

### 🔐 **Test 19: Basic Authentication** (`test_19BasicAuthPopup.py`)
**What you'll learn:**
- Handle HTTP basic authentication
- Browser context with credentials
- Authentication popup handling

**Key Concepts:**
- `http_credentials={"username": "...", "password": "..."}` - Set auth
- Browser context authentication
- Secure login handling

---

### 📁 **Test 20: File Upload** (`test_20UploadFile.py`)
**What you'll learn:**
- Single and multiple file uploads
- File input handling
- File path management

**Key Concepts:**
- `set_input_files("path/to/file")` - Single file upload
- `set_input_files(["file1", "file2"])` - Multiple files
- File upload validation

---

### 📝 **Test 21: Logging** (`test_21GeneratingLog.py`)
**What you'll learn:**
- Generate test execution logs
- Different log levels (INFO, ERROR, DEBUG)
- Log file configuration

**Key Concepts:**
- `logging.basicConfig()` - Configure logging
- `logger.info()`, `logger.error()` - Log messages
- Log file management

---

### ⚙️ **Test 22: Configuration Files** (`test_22Configini.py`)
**What you'll learn:**
- External configuration management
- INI file reading
- Environment-specific settings

**Key Concepts:**
- `ConfigParser()` - Read config files
- `config.get(section, key)` - Get config values
- Externalized test data

---

### 📊 **Test 23: Excel Operations** (`test_23Reading_Writing_Excel.py`)
**What you'll learn:**
- Read data from Excel files
- Write data to Excel files
- Excel-based test data management

**Key Concepts:**
- `openpyxl.load_workbook()` - Load Excel file
- `sheet.cell(row=i, column=j).value` - Read cell data
- `sheet.max_row`, `sheet.max_column` - Get dimensions
- Excel data iteration

---

### 🔄 **Test 24: Parameterization** (`test_24Parameterization.py`)
**What you'll learn:**
- Data-driven testing with pytest
- Test parameterization
- Multiple test data sets

**Key Concepts:**
- `@pytest.mark.parametrize()` - Parameterize tests
- Multiple data sets execution
- Dynamic test generation

---

### 🌐 **Test 25: Multi-Browser Testing** (`test_25MultiBrowser.py`)
**What you'll learn:**
- Cross-browser testing
- Browser-specific fixtures
- Parallel browser execution

**Key Concepts:**
- Browser fixtures (Chrome, Firefox)
- Cross-browser compatibility testing
- Browser-specific behavior testing

---

### 📊 **Test 26: Allure Reports** (`test_26AllureReport.py`)
**What you'll learn:**
- Generate beautiful test reports
- Test categorization and severity
- Step-by-step reporting

**Key Concepts:**
- `@allure.feature()` - Feature categorization
- `@allure.severity()` - Test severity levels
- `with allure.step()` - Step reporting

---

### 📸 **Test 27: Allure with Screenshots** (`test_27AllureReportScreenshot.py`)
**What you'll learn:**
- Attach screenshots to reports
- Visual test evidence
- Enhanced reporting with images

**Key Concepts:**
- `allure.attach()` - Attach files to reports
- `AttachmentType.PNG` - Attachment types
- Visual test documentation

---

### 📈 **Test 28: Data-Driven Testing** (`test_28DataDrivenTesting.py`)
**What you'll learn:**
- Excel-based data-driven testing
- Dynamic test data loading
- Scalable test data management

**Key Concepts:**
- Excel data reading for tests
- Dynamic parameterization
- Large-scale data testing

---

## 🏃‍♂️ How to Run Tests

### Run Individual Tests
```bash
# Activate environment first
source activate.sh

# Navigate to playwright directory
cd playwright

# Run specific test
pytest test_01playwrightBasics.py -v

# Run specific test method
pytest test_01playwrightBasics.py::test_pw_shortcut -v

# Run with browser visible
pytest test_01playwrightBasics.py -v -s --headed
```

### Run Multiple Tests
```bash
# Run all tests
pytest -v

# Run tests with specific pattern
pytest test_0* -v

# Run tests in parallel
pytest -n auto

# Generate Allure report
pytest --alluredir=allure-results
allure serve allure-results
```

### Browser Options
```bash
# Run with Firefox
pytest --browser firefox

# Run with WebKit (Safari)
pytest --browser webkit

# Run headless (default)
pytest --browser chromium --headed=false
```

---

## 🔧 Quick Reference

### Essential Locators
```python
# By text content
page.get_by_text("Click me")

# By label
page.get_by_label("Username:")

# By role
page.get_by_role("button", name="Submit")

# By placeholder
page.get_by_placeholder("Enter email")

# CSS selectors
page.locator("#id")
page.locator(".class")
page.locator("input[type='text']")

# XPath
page.locator("//button[text()='Click']")
```

### Common Actions
```python
# Click
page.locator("button").click()

# Fill text
page.locator("input").fill("text")

# Select dropdown
page.locator("select").select_option("value")

# Check/uncheck
page.locator("checkbox").check()
page.locator("checkbox").uncheck()

# Hover
page.locator("element").hover()

# Wait for element
page.locator("element").wait_for()
```

### Assertions
```python
# Element assertions
expect(page.locator("element")).to_be_visible()
expect(page.locator("element")).to_have_text("expected")
expect(page.locator("element")).to_be_enabled()

# Page assertions
expect(page).to_have_title("Expected Title")
expect(page).to_have_url("expected-url")
```

---

## 🎯 Learning Path Recommendation

### Beginner (Tests 1-10)
1. **Start with Test 01** - Learn basic Playwright setup
2. **Test 03** - Understand window handling
3. **Test 04** - Master alert handling
4. **Test 06** - Practice mouse interactions
5. **Test 08** - Work with tables

### Intermediate (Tests 11-20)
6. **Test 11** - Keyboard actions
7. **Test 13** - Dropdown handling
8. **Test 16** - Checkbox operations
9. **Test 17** - Assertions mastery
10. **Test 20** - File operations

### Advanced (Tests 21-28)
11. **Test 22** - Configuration management
12. **Test 23** - Excel integration
13. **Test 24** - Parameterization
14. **Test 26-27** - Reporting
15. **Test 28** - Data-driven testing

---

## 📞 Support

If you encounter any issues:
1. Check the virtual environment is activated
2. Ensure all dependencies are installed
3. Verify browser installation: `playwright install`
4. Check Python interpreter in PyCharm settings

**Happy Testing! 🎭✨**