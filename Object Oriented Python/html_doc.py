class Tag(object):

    def __init__(self, name, contents):
        self.start_tag = "<{}>".format(name)
        self.end_tag = "</{}>".format(name)
        self.contents = contents

    def __str__(self):
        return "{0.start_tag}{0.contents}{0.end_tag}".format(self)

    def display(self):
        print(self)


class DocType(Tag):

    def __init__(self):
        super().__init__('!DOCTYPE HTML', '')
        self.end_tag = ''   # DOCTYPE doesnt have a end tag


class Head(Tag):

    def __init__(self):
        super().__init__('head', '')


class Body(Tag):

    def __init__(self):
        super().__init__('body', '')    # body contents will be built up sperately
        self._body_contents = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._body_contents.append(new_tag)

    def display(self):
        for tag in self._body_contents:
            self.contents += str(tag)

        super().display()
