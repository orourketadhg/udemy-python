class Tag(object):

    def __init__(self, name, contents):
        self.start_tag = "<{}>".format(name)
        self.end_tag = "</{}>".format(name)
        self.contents = contents

    def __str__(self):
        return "{0.start_tag}{0.contents}{0.end_tag}".format(self)

    def display(self, file=None):
        print(self, file=file)


class DocType(Tag):

    def __init__(self):
        super().__init__('!DOCTYPE HTML', '')
        self.end_tag = ''   # DOCTYPE doesnt have a end tag


class Head(Tag):

    def __init__(self):
        super().__init__('head', '')


# inheritance from Tag - not a subclass but a override of Tag methods
class Body(Tag):

    def __init__(self):
        super().__init__('body', '')    # body contents will be built up separately
        self._body_contents = []

    def add_tag(self, name, contents):
        # composition - creating a class object in class
        new_tag = Tag(name, contents)
        self._body_contents.append(new_tag)

    def display(self, file=None):
        for tag in self._body_contents:
            self.contents += str(tag)

        super().display(file=file)


class HtmlDoc(object):

    # a class is made up of other class objects and attributes (composition)
    def __init__(self):
        # create class object attributes
        self._doc_type = DocType()
        self._head = Head()
        self._body = Body()

    def add_tag(self, name, contents):
        self._body.add_tag(name, contents)

    def display(self, file=None):
        self._doc_type.display(file=file)
        print('<html>')
        self._head.display(file=file)
        self._body.display(file=file)
        print('</html>')


if __name__ == '__main__':
    my_page = HtmlDoc()
    my_page.add_tag('h1', 'main header')
    my_page.add_tag('h2', 'sub header')
    my_page.add_tag('p', 'test paragraph')
    my_page.display()
