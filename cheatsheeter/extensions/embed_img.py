
import base64
import mimetypes
import os
from urllib.parse import unquote
import xml.etree.ElementTree as etree
from markdown.inlinepatterns import LinkInlineProcessor
from markdown.extensions import Extension

def remove_namespace(doc, namespace):
    """Remove namespace in the passed document in place."""
    ns = u'{%s}' % namespace
    nsl = len(ns)
    for elem in doc.getiterator():
        if elem.tag.startswith(ns):
            elem.tag = elem.tag[nsl:]

class EmbedImageInlineProcessor(LinkInlineProcessor):
    """ Return a embed img element from the given match. """

    def handleMatch(self, m, data):
        from cheatsheeter.__main__ import cheatsheeter

        text, index, handled = self.getText(data, m.end(0))
        if not handled:
            return None, None, None

        src, title, index, handled = self.getLink(data, index)
        if not handled:
            return None, None, None

        filename = os.path.join(cheatsheeter.source_path, unquote(src))

        if src.endswith('.svg'):
            el = etree.parse(filename).getroot()
            remove_namespace(el, "http://www.w3.org/2000/svg")
            el.attrib.pop('width', None)
            el.attrib.pop('height', None)
        else:
            mime = mimetypes.guess_type(filename)[0]
            with open(filename, 'br') as f:
                data = base64.b64encode(f.read()).decode('ascii')
            src_data = "data:{};base64,{}".format(mime, data)
            el = etree.Element("img")

            el.set("src", src_data)

            if title is not None:
                el.set("title", title)

            el.set('alt', self.unescape(text))
        return el, m.start(0), index


class EmbedImageExtension(Extension):
    def extendMarkdown(self, md):
        EMBED_IMAGE_LINK_RE = r'\!\!\['
        md.inlinePatterns.register(EmbedImageInlineProcessor(EMBED_IMAGE_LINK_RE, md), 'embed_img', 175)