import re
from io import StringIO
import csv

from markdown.blockprocessors import BlockProcessor
from markdown.extensions import Extension
import xml.etree.ElementTree as etree

from prettytable import from_csv
from markdown.util import AtomicString

FALLBACK_DELIMITER = ','

class CsvTablesProcessor(BlockProcessor):
    RE_CSV_START = r'^,{3}\s*\n' # start line, e.g., `,,,\n`
    RE_CSV_END = r'\n,{3}\s*$'  # last non-blank line, e.g, ',,,\n  \n\n'

    def test(self, parent, block):
        return re.match(self.RE_CSV_START, block)

    def run(self, parent, blocks):
        original_block = blocks[0]
        blocks[0] = re.sub(self.RE_CSV_START, '', blocks[0])

        # Find block with ending csv
        for block_num, block in enumerate(blocks):
            if re.search(self.RE_CSV_END, block):
                # remove csv
                blocks[block_num] = re.sub(self.RE_CSV_END, '', block)
                # render table area inside a new div
                e = etree.SubElement(parent, 'div')
                csv_block = blocks[0:block_num + 1]
                try:
                    table = from_csv(StringIO(csv_block[0]))
                except csv.Error:
                    table = from_csv(StringIO(csv_block[0]), delimiter=FALLBACK_DELIMITER)
                for row in table.rows:
                    for i, value in enumerate(row):
                        row[i] = AtomicString(value)
                e_table = etree.fromstring(table.get_html_string())
                e.append(e_table)
                # remove used blocks
                for i in range(0, block_num + 1):
                    blocks.pop(0)
                return True  # or could have had no return statement
        # No closing marker!  Restore and do nothing
        blocks[0] = original_block
        return False  # equivalent to our test() routine returning False

class CsvTablesExtension(Extension):
    def extendMarkdown(self, md):
        md.parser.blockprocessors.register(CsvTablesProcessor(md.parser), 'csv_tables', 175)