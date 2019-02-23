pages = [
    {
    'filename': 'content/websitecontent.html',
    'output': 'docs/output_file.html',
    'title': 'Website'
    }

]

for page in pages:
    print(page)

page_filename = page['filename']
print(page_filename)

page_output = page['output']
print(page_output)

page_title = page['title']
print(page_title)