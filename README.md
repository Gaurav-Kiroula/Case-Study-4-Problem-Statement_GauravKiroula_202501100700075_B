# Case-Study-4-Problem-Statement_GauravKiroula_202501100700075_B
## Case Study 4: Log Analysis System

## Execution Guide
This script automates the processing of `CS4.txt`. It identifies log levels, partitions data into separate files, and performs a keyword search[cite: 1].

## Debugging Notes
*   **Pointer Reliability**: The script uses binary mode (`rb`) for seek operations to allow backward movement from the end of the file, preventing common Python I/O errors[cite: 1].
*   **Memory Efficiency**: Uses list comprehensions for fast filtering of INFO, WARNING, and ERROR logs[cite: 1].
*   **Search**: The search tool is case-insensitive to ensure "error" finds "ERROR" entries[cite: 1].

## Final Submission Checklist
1.  Run the script to generate `info_logs.txt`, `warning_logs.txt`, `error_logs.txt`, and `search_result.txt`[cite: 1].
2.  Take a screenshot of the terminal output showing the "Seek Operations" results[cite: 1].
3.  Zip the `.py` file, the four `.txt` files, and the screenshot[cite: 1].
4.  Submit via the Google Form by **5th May 2026**[cite: 1].
