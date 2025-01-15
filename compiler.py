import sys
import argparse

def txt_to_html(input_file, output_file, center=False):
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

    if center:
        wrapped_content = f'<center><div style="display: inline-block; text-align: left;">{wrapped_content}</div></center>'

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
                font-size:13px; 
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
        <pre>{wrapped_content}</pre>
    </body>
    </html>
    """
    with open(output_file, 'w') as html_file:
        html_file.write(html_content)

def main():
    # if len(sys.argv) != 2:
    #     print(f'Usage: python3 {sys.argv[0]} <input_file>')
    #     sys.exit(1)

    # input_file = sys.argv[1]

    parser = argparse.ArgumentParser(description='Convert text file to HTML')
    parser.add_argument('filename')
    parser.add_argument('-o' ,'--output', help='Output file path')
    parser.add_argument('-c', '--center', action='store_true', help='Center the text')
    args = parser.parse_args()

    input_file = args.filename
    output_file = args.output if args.output else f'{input_file.split('.')[0]}.html'
    txt_to_html(input_file, output_file, args.center)

if __name__ == "__main__":
    main()