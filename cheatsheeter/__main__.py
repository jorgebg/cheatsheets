import argparse
from dataclasses import dataclass
import os

import markdown
from jinja2 import Environment, PackageLoader, select_autoescape


DEFAULT_SECTION_SEPARATOR = '~~~'
DEFAULT_OUTPUT_FILE = '{source}.html'
DEFAULT_SOURCE_PATH = './cheatsheets'
DEFAULT_BUILD_PATH = './docs'

parser = argparse.ArgumentParser(description='Cheatsheet creator.', prog="cheatsheeter")
parser.add_argument('--source-path', default=DEFAULT_SOURCE_PATH, help='Source path')
parser.add_argument('--build-path', default=DEFAULT_BUILD_PATH, help='Build path')
parser.add_argument('--separator', default=DEFAULT_SECTION_SEPARATOR, help='Section separator')


args = parser.parse_args()

@dataclass
class Section:
    title: str
    content_html: str
    width: int = 0
    footer: str = ""

class Cheatsheeter:
    def __init__(self, source_path, build_path, separator):
        self.source_path = source_path
        self.build_path = build_path
        self.separator = separator
        self.md = markdown.Markdown(extensions=['extra', 'meta', 'cheatsheeter.extensions.csv_tables:CsvTablesExtension', 'cheatsheeter.extensions.embed_img:EmbedImageExtension'])
        self.template_env = Environment(
            loader=PackageLoader("cheatsheeter"),
            # autoescape=select_autoescape()
        )

    def build(self):
        os.makedirs(args.source_path, exist_ok=True)
        os.makedirs(args.build_path, exist_ok=True)

        title_list = []
        for filename in os.listdir(args.source_path):
            if filename.endswith('.md'):
                title_list.append(self._build_cheatsheet(filename))
        self._build_index(title_list)
        


    def _build_cheatsheet(self, source_filename) -> str:
        title = os.path.splitext(source_filename)[0]
        with open(os.path.join(args.source_path, source_filename)) as f:
            src = f.read()

        section_src_list = src.split(args.separator)
        section_list = []

        cheatsheet_template = self.template_env.get_template("cheatsheet.html")

        for section_src in section_src_list:
            content_html = self.md.convert(section_src.strip())
            meta = {k: v[0] for k,v in self.md.Meta.items()}
            meta.setdefault('title', source_filename.title())
            section_list.append(Section(content_html=content_html, **meta))
            self.md.Meta = {}  # Clean Meta attribute, otherwise it will be carried over to the next section

        output_html = cheatsheet_template.render(title=title, section_list=section_list)

        build_filename = title + '.html'
        with open(os.path.join(args.build_path, build_filename), 'w') as f:
            f.write(output_html)

        return title

    def _build_index(self, title_list):
        index_template = self.template_env.get_template("index.html")
        output_html = index_template.render(title_list=title_list)
        with open(os.path.join(args.build_path, 'index.html'), 'w') as f:
            f.write(output_html)



Cheatsheeter(**vars(args)).build()