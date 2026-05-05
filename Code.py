#Casestudy4_GauravKiroula_202501100700075_B
# Case Study 4: Debugged and Final Version
filename = "CS4.txt"

try:
    # --- Task 1: Basic File Reading ---
    # Using read() for full content
    with open(filename, 'r') as f:
        full_data = f.read()

    # Using readline() for specific lines
    with open(filename, 'r') as f:
        first_line = f.readline()
        second_line = f.readline()

    # Using readlines() for total count
    with open(filename, 'r') as f:
        all_lines = f.readlines()
    
    print(f"Total number of lines: {len(all_lines)}")
    print(f"First 2 lines:\n{first_line}{second_line}")
    print(f"Last 2 lines:\n{''.join(all_lines[-2:])}")

    # --- Task 2: Log Classification ---
    # Keywords: INFO, WARNING, ERROR
    log_counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    for line in all_lines:
        for key in log_counts.keys():
            if key in line:
                log_counts[key] += 1
    print(f"\nLog Summary: {log_counts}")

    # --- Task 3: Write Filtered Files ---
    # Filtering lists
    info_list = [l for l in all_lines if "INFO" in l]
    warn_list = [l for l in all_lines if "WARNING" in l]
    err_list = [l for l in all_lines if "ERROR" in l]

    # Use writelines() for lists and write() for joined strings
    with open("info_logs.txt", "w") as f:
        f.writelines(info_list)
    with open("warning_logs.txt", "w") as f:
        f.write("".join(warn_list))
    with open("error_logs.txt", "w") as f:
        f.writelines(err_list)
    print("\nFiltered files (info, warning, error) have been created.")

    # --- Task 4: Search Feature ---
    search_query = input("\nEnter keyword to search: ")
    # Case-insensitive matching for better user experience
    matches = [l for l in all_lines if search_query.upper() in l.upper()]
    
    print(f"Matches for '{search_query}':")
    for m in matches:
        print(m.strip())
        
    with open("search_result.txt", "w") as f:
        f.writelines(matches)

    # --- File Pointer (seek) Operations ---
    print("\n--- Performing Seek Operations ---")
    # Must use 'rb' for seeking from the end
    with open(filename, 'rb') as f:
        # Read first 50 characters
        print(f"First 50 chars: {f.read(50).decode().strip()}")
        
        # Beginning -> seek(0)
        f.seek(0)
        print(f"At Beginning (seek 0): {f.read(15).decode()}...")
        
        # Middle -> seek(len//2)
        f.seek(0, 2) # Go to end
        size = f.tell()
        f.seek(size // 2)
        print(f"At Middle: ...{f.read(20).decode()}...")
        
        # Last 100 chars -> seek(-100, 2)
        f.seek(-100, 2)
        print(f"Last 100 chars: {f.read().decode().strip()}")

except FileNotFoundError:
    print(f"Error: '{filename}' not found. Please ensure it is in the same folder.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
