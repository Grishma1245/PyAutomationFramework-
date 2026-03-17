It is a Python-based automation framework for testing and utility scripts, including keyboard/mouse operations, screenshots, logging, and multiple test cases.
        Project Structure:
Base/                  # Base classes and setup scripts
Library/               # Utility scripts for keyboard, mouse, screenshots
TestCases/             # Test case scripts
configurationFiles/    # Configuration and environment files
myenv/                 # Python virtual environment
pytest/                # Pytest scripts

keyboard_op.py         # Keyboard automation utilities
mouse_op.py            # Mouse automation utilities
takeSS.py              # Screenshot capture utility
tc_SS.py               # Test case for screenshots
tc_logging.py          # Test case for logging
tc_multitab.py         # Test case for multi-tab operations
tesctcase.py           # Miscellaneous test cases
test1.py               # Sample test case
infolog.txt            # Log file for information

How to use:
1.Clone the repository
git clone https://github.com/Grishma1245/PyAutomationFramework-

2.Set up the virtual environment:
python -m venv myenv
source myenv/bin/activate   # Linux/Mac
myenv\Scripts\activate      # Windows

3.Install dependencies (if any):
pip install -r requirements.txt

4.Run the test cases:
pytest TestCases/
