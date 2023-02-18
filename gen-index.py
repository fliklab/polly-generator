import os
import re

html_files = []

# search for HTML files in the current directory and its subdirectories
for dirpath, dirnames, filenames in os.walk('.'):
    for filename in filenames:
        if re.search('\.html$', filename):
            html_files.append(os.path.join(dirpath, filename))

# create the index file
with open('index.html', 'w') as index_file:
    # write the HTML header
    index_file.write('<html>\n<head>\n<title>Index of HTML files</title>\n</head>\n<body>\n')
    # write the list of HTML files
    index_file.write('<ul>\n')
    for html_file in html_files:
        index_file.write(f'<li><a href="{html_file}">{html_file}</a></li>\n')
    index_file.write('</ul>\n')
    # write the HTML footer
    index_file.write('</body>\n</html>\n')
