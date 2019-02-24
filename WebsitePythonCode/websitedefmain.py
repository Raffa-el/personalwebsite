def main():
    template = open('kickstart/personalwebsite/personalwebsite/templates/base.html').read()

    index_content = open('docs/index.html').read()

    finished_index_page = template.replace ('{{content}}', index_content) 
    open('docs/index.html', 'w+').write(finished_index_page)

main()