## i-file-utils

This project holds certain utilities which can help with file operations. Currently, the functionalities available are:

1) Find common integers between files

## Time Complexity

### Steps

- The script aims to process huge files with integers as contents which cannot fit into memory
- So the algorithm takes the following approach:

1) Break down the file into smaller chunks - You can configure the chunk size, else it defaults to **~512 MB/chunk**
2) File is read in chunks of size as configured above, and when written back to disk, the data is sorted
3) These sorted chunks are then merged back into a single file
4) This process is repeated for both the input files
5) Then we iterate through the files to find common elements. We take the smaller file as the reference point to
   optimistically save some CPU cycles hoping to we reach the EOF sooner.
6) During the comparison to find common elements, at any given point in time, only two values are kept in memory thus
   making this scalable for large files

**NOTE**

- All the intermediate files generated are stored in temp location which would be cleaned up automatically by the script
- This can be overridden by providing a working directory as input, but cleaning up intermediate files would be
  developer's responsibility in this case
- Hence, it is recommended to let the script do its magic and let it manage the intermediate files



### Big-O Notation 
1) Let <code>Size of File 1 = S</code>
2) Let <code>Size of File 2 = T</code>
3) Let <code>Chunk size or Block Size = B</code>

## Time Complexity
1) Splitting and sorting the file would take complexity of running sorting on (File Size / B) chunks. Hence, complexity
   for each file is as follows -
2) File 1: <code>O(S/B * B * log B) => O(S * log B)</code>
3) File 2: <code>O(T/B * B * log B) => O(T * log B)</code>
4) Merging the files back to a single sorted file. Again repeated for both files: 
5) <code>O(S * log S/B) + O(T * log T/B)</code>
6) Finding common elements between files: <code>O(S) + O(T)</code>
7) So overall complexity would be: 
8) **_<code>O(S * log B) + O(T * log B) + O(S * log S/B) + O(T * log T/B) + O(S) + O(T)</code>_**

**NOTE:**
- The overall **_wall clock time can be reduced_** by using parallel processing for sorting chunks
- Also, we can use parallel splitting of files as we know file size and chunk size. And the logic ignores duplicates
  during processing which eliminates the risk of overlapping elements. We need to be mindful that we don't miss any
  elements which can be achieved by reading a slightly bigger chunk than specified chunk size
- We could also tweak the chunk size to optimize the processing further

## Space Complexity
1) The maximum memory footprint of the logic is during the sorting phase, where we load Block size (B) amount of data.
2) So the space complexity would be O(B)


## Oh nice! How do I use it??

### Pre-requisites

1) Install python 3 and above version
2) Upgrade pip - https://pip.pypa.io/en/stable/installation/

## Install the package

1) https://pypi.org/project/iFileIntersection/
2) If lazy to open the link, run this command - pip install iFileIntersection

## I am all set! Help me run it

1) Running it is how you would run any other python program:
2) <code>python -m intersection.main --help</code>
3) Above command would show all the options you can pass in
4) <code>python -m intersection.main -l <fully_qualified_path_to_first_file> -r <
   fully_qualified_path_to_second_file> -o <fully_qualified_path_to_output_file> -c <chunk_size_in_mb></code>
5) If this package is a dependency to your package you can invoke the logic as follows:

   <code>from intersection.main import find_intersection</code>
   <code>find_intersection(file_path_1, file_path_2, output_file_path)</code>

## Contact

- Feel free to reach out to me at nikhilkm.dev@gmail.com if any questions