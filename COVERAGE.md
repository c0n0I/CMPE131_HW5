#Coverage Report
## Summary of Coverage Results
Name              Stmts   Miss  Cover   Missing
-----------------------------------------------
src\__init__.py       0      0   100%
src\order_io.py      20      2    90%   12, 15
src\pricing.py       22      0   100%
-----------------------------------------------
TOTAL                42      2    95%

This shows that pricing.py is 100% covered, while order_io.py is 90% covered with 2 lines that are uncovered (12,15). 

## Uncovered Lines
- **Line 12** — `if not ln.strip(): continue`
- **Line 15** — error handling: `raise ValueError("Malformed line: " + ln.strip())`

## Analysis of Which Uncovered Parts are Acceptable
For line 12, this piece of code skips the blank lines from the input file. The integration test doesn't contain any blank lines, therefore this piece of code is not tested or run through.
For line 15, this branh handles *malformed* CSV lines. The integration test also didn't include any malformed lines, so this piece of code was also not tested or run through.

These uncovered parts are not too important in the main purpose of the application, which is to load an order and generate a reciept. We assume that the input is going to be valid, so handling errors are not our primary concern. Therefore, we can leave it uncovered.
