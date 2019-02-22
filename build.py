print('Holy hell this is so hard')

top_html = open('templates/websitetop.html').read()

content_html = open('content/websitecontent.html').read()

bottom_html = open('templates/websitebottom.html').read()

print('Its still hard')

combined_html = top_html + content_html + bottom_html

open('output_file.html', 'w+').write(combined_html)

print ('testing')

 