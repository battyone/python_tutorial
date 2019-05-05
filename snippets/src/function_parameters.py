# %%

# '*' and '**' to "explode" iterables and mappings
# into seperate arguments


def tag(name, *content, cls=None, **attrs):
    #'''Generate one or more HTML tags'''
    if cls is not None:
        attrs['class'] = cls

    if attrs:
        attr_str = ''.join(' %s="%s"' %
                           (attr, value) for attr, value
                           in sorted(attrs.items()))
    else:
        attr_str = ''

    if content:
        return '\n'.join('<%s%s>%s</%s>' %
                         (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)


# %%
# just name
print(tag('br'))

# name and one item in content
print(tag('p', 'Hello'))

# two <p> tags with content
print(tag('p', 'Hello', 'World'))

# two p tags with content and one attribute
print(tag('p', 'Hello', 'World', cls='sidebar'))

# %%
# two <p> tags with content
a = ['content1', 'content2']
print(tag(name='foo', content=a))

# %%
func_para = {
    'name': 'img',
    'title': 'Sunset Boulevard',
    'src': 'sunset.jpg',
    'cls': 'framed'
}

print(tag(**func_para))

# %%
func_para = {
    'title': 'Sunset Boulevard',
    'src': 'sunset.jpg',
    'cls': 'framed'
}

print(tag('img', *['content1', 'content2'], **func_para))

# %%


def test(name, *content, **attrs):
    print(type(content))
    print(len(content))
    print(content)
    print(type(attrs))
    print(len(attrs))
    print(attrs)

# https://docs.python.org/3.7/tutorial/controlflow.html#keyword-arguments


test('bla', *['a', 'b'])
test('bla', *('a', 'b'))

test('bla', *('a', 'b'), **{'foo': 'bar', 'bla': 'bla bla'})
