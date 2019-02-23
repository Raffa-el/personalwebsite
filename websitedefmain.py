def main ():
    top_html = open('templates/websitetop.html').read()

    content_html = open('content/websitecontent.html').read()

    bottom_html = open('templates/websitebottom.html').read()


    combined_html = top_html + content_html + bottom_html

    open('output_file.html', 'w+').write(combined_html)

if __name__ == '__main__'
    main ()