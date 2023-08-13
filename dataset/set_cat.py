import csv

# List of source CSV files
source_files = ['array', 'string', 'hash-table', 'dynamic-programming','math','sorting','greedy','depth-first-search','database','binary-search','breadth-first-search','tree', 'matrix', 'binary-tree', 'bit-manipulation', 'heap', 'stack' ,'prefix-sum', 'graph', 'simulation', 'design', 'backtracking', 'counting', 'sliding-window', 'union-find', 'linked-list', 'ordered-set','enumeration','monotonic-stack','trie','recursion','divide-and-conquer','bitmask','number-theory','queue','binary-search-tree','segment-tree','memoization','geometry','topological-sort','binary-indexed-tree','hash-function','game-theory','shortest-path','interactive','combinatorics','data-stream','string-matching','rolling-hash','brainteaser','randomized','monotonic-queue','merge-sort','iterator','concurrency','doubly-linked-list','probability-and-statistics','quickselect','bucket-sort','suffix-array','minimum-spanning-tree','counting-sort','shell','line-sweep','reservoir-sampling','eulerian-circuit','radix-sort','strongly-connected-component','rejection-sampling','biconnected-component']

concatenated_file = 'concatenated_data.csv'

# Create a new CSV file for writing
with open(concatenated_file, 'w', newline='', encoding='utf-8') as new_csvfile:
    csv_writer = csv.writer(new_csvfile)

    # Loop through each source CSV file
    for source_file in source_files:
        with open(f"leetcode_questions_{source_file}.csv", 'r', newline='', encoding='utf-8') as source_csv:
            csv_reader = csv.reader(source_csv)
            
            # Skip the header if it exists in source files
            next(csv_reader)
            
            # Write each row from the source CSV to the concatenated CSV
            for row in csv_reader:
                csv_writer.writerow(row)

print("Concatenation completed.")