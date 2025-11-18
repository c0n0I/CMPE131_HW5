#Coverage Report
## Summary of Coverage Results
<img width="339" height="149" alt="image" src="https://github.com/user-attachments/assets/955ec118-5dc4-451a-b38b-f693b2bee717" />


This shows that pricing.py is 100% covered, while order_io.py is 90% covered with 2 lines that are uncovered (12,15). Together, 95% of the files are covered. 

## Uncovered Lines
- **Line 12** — `if not ln.strip(): continue`
- **Line 15** — error handling: `raise ValueError("Malformed line: " + ln.strip())`

## Analysis of Which Uncovered Parts are Acceptable
For line 12, this piece of code skips the blank lines from the input file. The integration test doesn't contain any blank lines, therefore this piece of code is not tested or run through.
For line 15, this branh handles *malformed* CSV lines. The integration test also didn't include any malformed lines, so this piece of code was also not tested or run through.

These uncovered parts are not too important in the main purpose of the application, which is to load an order and generate a reciept. These purpose of lines 12 and 15 is to protect the program from incorrect user input. However, we are assuming that the input is going to be valid, so handling errors are not our primary concern. Therefore, it is reasonable that we can leave it uncovered.
