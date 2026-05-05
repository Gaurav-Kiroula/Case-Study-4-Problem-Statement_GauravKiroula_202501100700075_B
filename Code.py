#Casestudy4_GauravKiroula_202501100700075_B
# Task 1: Basic File Reading
filename = "CS4.txt"

print("--- Task 1: Basic File Reading ---")
try:
    # Reading entire content to demonstrate read()
    with open(filename, 'r') as f:
        full_content = f.read()
    
    # Reading lines to demonstrate readlines() and count totals
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    total_lines = len(lines)
    print(f"Total number of lines: {total_lines}")
    
    # Printing first and last 2 lines
    print(f"First 2 lines:\n{''.join(lines[:2])}")
    print(f"Last 2 lines:\n{''.join(lines[-2:])}")

    # Task 2: Log Classification
    print("\n--- Task 2: Log Classification ---")
    log_counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    for line in lines:
        for key in log_counts.keys():
            if key in line:
                log_counts[key] += 1
    print(f"Stored Results in Dictionary: {log_counts}")

    # Task 3: Write Filtered Files
    print("\n--- Task 3: Write Filtered Files ---")
    # Using list comprehensions to filter
    info_logs = [line for line in lines if "INFO" in line]
    warning_logs = [line for line in lines if "WARNING" in line]
    error_logs = [line for line in lines if "ERROR" in line]

    # Writing using writelines() and write() as requested
    with open("info_logs.txt", "w") as f:
        f.writelines(info_logs)
    
    with open("warning_logs.txt", "w") as f:
        f.write("".join(warning_logs))
        
    with open("error_logs.txt", "w") as f:
        f.writelines(error_logs)
    print("Files 'info_logs.txt', 'warning_logs.txt', and 'error_logs.txt' created.")

    # Task 4: Search Feature
    print("\n--- Task 4: Search Feature ---")
    search_key = input("Enter keyword to search (e.g., ERROR): ")
    matching_lines = [line for line in lines if search_key.upper() in line.upper()]
    
    print(f"Matches found for '{search_key}':")
    for match in matching_lines:
        print(match.strip())
        
    with open("search_result.txt", "w") as f:
        f.writelines(matching_lines)

    # File Pointer (seek) Operations
    print("\n--- File Pointer (seek) Operations ---")
    # Using 'rb' (read binary) mode for backward seeking
    with open(filename, 'rb') as f:
        # Read first 50 characters
        first_50 = f.read(50).decode()
        print(f"First 50 characters: {first_50}")
        
        # Move pointer to Beginning
        f.seek(0)
        print(f"Content at Beginning: {f.read(20).decode()}...")
        
        # Move pointer to Middle (Calculating size without 'os' module)
        f.seek(0, 2)            # Seek to end (position 2)
        file_size = f.tell()    # Get current position (size)
        f.seek(file_size // 2)  # Seek to middle
        print(f"Content at Middle: {f.read(20).decode()}...")
        
        # Move pointer to Last 100 chars
        f.seek(-100, 2)         # -100 from the end (position 2)
        print(f"Content at Last 100: ...{f.read().decode().strip()}")

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
