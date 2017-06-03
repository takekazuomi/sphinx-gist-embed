#-*- coding:utf-8 -*-

from docutils import nodes

from docutils.parsers import rst

class gist(nodes.General, nodes.Element):
    pass



def visit(self, node):

    if len(node.file) > 0:
        tag = u'''<script src="{0}.js?file={1}">&nbsp;</script>'''.format(node.url, node.file)
    else:
        tag = u'''<script src="{0}.js">&nbsp;</script>'''.format(node.url)

    self.body.append(tag)

def depart(self, node):
    pass

class GistDirective(rst.Directive):

    name = 'gist'
    node_class = gist

    has_content = False
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {'file': rst.directives.unchanged }


    def run(self):

        node = self.node_class()

        node.url = self.arguments[0]

        if 'file' in self.options:
            node.file = self.options['file']
        else:
            node.file = ''

        return [node]
