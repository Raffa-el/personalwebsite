print('Holy hell this is makes more sense')

top_html = open('templates2/topwebsite.html').read()

content_html = open('content2/contentwebsite.html').read()

bottom_html = open('templates2/bottomwebsite.html').read()

print('Its still hard, but better')

combined_html = top_html + content_html + bottom_html

open('output_file.html', 'w+').write(combined_html)

print ('testing')
