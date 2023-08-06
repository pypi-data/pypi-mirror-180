import os
import re
from tempfile import mktemp

from IPython.display import display
from pylatex import Command, Document, Section, Subsection
from pylatex.utils import NoEscape, italic
from wand.image import Image as WImage

from pyfeyn2.render.render import Render


class LatexRender(Document, Render):
    def __init__(
        self,
        fd,
        documentclass="standalone",
        document_options=["preview", "crop"],
        *args,
        **kwargs,
    ):
        super().__init__(
            *args,
            documentclass=documentclass,
            document_options=document_options,
            **kwargs,
        )
        Render.__init__(self, fd)

    def get_src(self):
        return self.dumps()

    def get_src_diag(self):
        return self.src_diag

    def set_src_diag(self, src_diag):
        self.src_diag = src_diag
        self.append(NoEscape(src_diag))

    def render(
        self,
        file=None,
        show=True,
        resolution=100,
        width=None,
        height=None,
        clean_up=True,
    ):
        delete = False
        if file is None:
            delete = True
            file = "tmp"
        file = re.sub("\.pdf$", "", file.strip())
        self.generate_pdf(file, clean_tex=clean_up)
        wi = WImage(
            filename=file + ".pdf", resolution=resolution, width=width, height=height
        )
        if delete:
            os.remove(file + ".pdf")
        if show:
            display(wi)
        return wi
