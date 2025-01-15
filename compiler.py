import sys
import argparse
import os

def format_homepage(filename='index.html'):
    dirs = [d for d in os.listdir('.') if os.path.isdir(d) and not d.startswith('.')]
    dirs.sort()
    print(dirs)

    with open(filename, 'w') as html_file:
        html_file.write(f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Homepage</title>
            """ + r"""
            <style>
                body {
                    color: #FEFEFE;
                    background-color: #0A0B11;
                    margin: 0 auto;
                    padding: 1em 0 1em 0;
                }

                a {
                    color: #93ffd7;
                    text-decoration: none;
                }

                @font-face {
                    font-family: "unifont";
                    src: url("./unifont.woff") format('woff');
                }

                pre {
                    font-family: "unifont", "Lucida Console", monospace, Monaco;
                    font-size: 16px;
                    line-height: 1.0;
                    padding-left: 20px;
                }

                .header {
                    font-family: "unifont", "Lucida Console", monospace, Monaco;
                    font-size: 14px;
                    line-height: 1.0;
                    padding-left: 20px;
                }

                .txtdiv {
                    display: block;
                    text-align: left;
                }
        </style>
        """ + f"""
        </head>

        <body>
            <pre class="header">
░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓███████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░       ░▒▓█▓▒▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░  ░▒▓█▓▒▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        ░▒▓█▓▓█▓▒░ ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        ░▒▓█▓▓█▓▒░ ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓███████▓▒░░▒▓████████▓▒░  ░▒▓██▓▒░  ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 

            ░▒▓███████▓▒░ ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░ ░▒▓██████▓▒░ ░▒▓██████▓▒░  
            ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
            ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
            ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
            ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
            ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
            ░▒▓███████▓▒░ ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░ ░▒▓██████▓▒░ ░▒▓██████▓▒░  
</pre><pre>                                                                                    
                                                                                    
- Writeups\n
""")

        for d in dirs:
            html_file.write(f'  - <a href="{d}/">{d}</a>\n')

        html_file.write("""

- Resume
        </pre>
        </body>
        </html>
        """)

def text_format(input_file, output_file):
    with open(input_file, 'r') as txt_file:
        content = txt_file.read()

    wrapped_content = ''
    for line in content.split('\n'):
        while len(line) > 83:
            split_index = line[:83].rfind(' ')
            if split_index == -1:
                split_index = 83
            wrapped_content += line[:split_index] + '\n'
            line = line[split_index:].lstrip()
        wrapped_content += line + '\n'

    with open(output_file, 'w') as txt_file:
        txt_file.write(wrapped_content)

def txt_to_html(input_file, output_file, center=False):
    with open(input_file, 'r') as txt_file:
        content = txt_file.read()

    wrapped_content = ''
    for line in content.split('\n'):
        leading_spaces = len(line) - len(line.lstrip(' '))
        while len(line) > 83:
            split_index = line[:83].rfind(' ')
            if split_index == -1:
                split_index = 83
            wrapped_content += line[:split_index] + '\n' + ' ' * leading_spaces
            line = line[split_index:].lstrip()
        wrapped_content += line + '\n'

    if center:
        wrapped_content = f'<center><div style="display: inline-block; text-align: left;"><pre>{wrapped_content}</pre></div></center>'
    else:
        wrapped_content = f'<pre>{wrapped_content}</pre>'

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Formatted Text</title>
        <style>""" + r"""
            body {
                color: #FEFEFE;
                background-color: #0A0B11;
                margin: 0 auto;
                padding: 1em 0 1em 0;
            }
            a { 
                color: #93ffd7;
                text-decoration: none; 
            }
            @font-face { 
                font-family: "unifont"; 
                src: url("./unifont.woff") format('woff'); 
            }
            pre { 
                font-family: "unifont", "Lucida Console", monospace, Monaco; 
                font-size:16px; 
                line-height: 1.0;
                padding-left: 20px;
            }
            .txtdiv {
                display: block;
                text-align: left;
            }
        </style>
    """ + f"""
    </head>

    <body>
        {wrapped_content}
    </body>
    </html>
    """
    with open(output_file, 'w') as html_file:
        html_file.write(html_content)

def main():
    parser = argparse.ArgumentParser(description='Convert text file to HTML')
    parser.add_argument('filename')
    parser.add_argument('-o' ,'--output', help='Output file path')
    parser.add_argument('-c', '--center', action='store_true', help='Center the text')
    parser.add_argument('-t', '--text-format', action="store_true", help='Text format')
    parser.add_argument('-p', '--format-homepage', action="store_true", help='Format homepage')
    args = parser.parse_args()

    input_file = args.filename
    output_file = args.output if args.output else f'{input_file.split('.')[0]}.html'

    if args.format_homepage:
        format_homepage()
        exit(0)

    if args.text_format:
        text_format(input_file, input_file)
    else:
        txt_to_html(input_file, output_file, args.center)

if __name__ == "__main__":
    main()