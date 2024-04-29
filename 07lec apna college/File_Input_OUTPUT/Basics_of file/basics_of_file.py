

#python can be used to porform operation on a file(read & write data)

"""
types of all files:

1. text file: .txt, .docx, .log etc.
2. Binary files: .mp4, .mov, .png, .jpeg etc


we   have to open a file before reading or writing

f = open("file_name", "mode)


'r' :- open for reading(default)
'w' :- open for writing truncating the file first
'x' :- create a new file and open it for writing
'a' :- open for writing appending to the end of the file if it exists 
'b' :- binary mode
't' :- text mode(default)
'+' :- open a disk file for updating (reading and writing)


r+  :- read and overwrite (ptr start) - no truncate
w+  :- read and overwrite             - truncate
a+  :- read and append    (ptr end)   - no truncate
"""