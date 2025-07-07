'''
StopThePress - Version1, Snapshot1

These functions can be used to comment-out or remove
lines of code ending in a specified substring,
e.g. '# temp check' marking temporary print statements
for checking intermediate value in algorithms.  
Caveat: Splits any internally-coded string linebreaks, 
so best not to use on code includng these.

TODO Make a version for GUI input & output.
'''

def remove_lines_with_suffix(text: str, suffix: str):
    lines = text.splitlines()
    for line in lines:
        if not line.endswith(suffix):
            print(line)


def comment_out_lines_with_suffix(text: str, suffix: str):
    lines = text.splitlines()
    for i in range(len(lines)):
        if lines[i].endswith(suffix):
            lines[i] = '# ' + lines[i]
        print(lines[i])


# Replace contents of this placeholder/example  
# string with text to be processed
test = '''
line1
line2 # temp check
line3# temp check
line4
'''

remove_lines_with_suffix(test, '# temp check')
comment_out_lines_with_suffix(test, '# temp check')