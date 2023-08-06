# github-slugger

[![Build][build-badge]][build]

[build-badge]: https://github.com/martinheidegger/github_slugger/workflows/main/badge.svg
[build]: https://github.com/martinheidegger/github_slugger/actions

> This is a Python Fork of the [JavaScript `github-slugger`][js] package

[js]: https://github.com/Flet/github-slugger

Generate a slug just like GitHub does for markdown headings. It also ensures slugs are unique in the same way GitHub does it. The overall goal of this package is to emulate the way GitHub handles generating markdown heading anchors as close as possible.

This project is not a markdown or HTML parser: passing `alpha *bravo* charlie`
or `alpha <em>bravo</em> charlie` doesn’t work.
Instead pass the plain text value of the heading: `alpha bravo charlie`.

## Install

```
pip install github-slugger
```

## Usage

```python
from github_slugger import GithubSlugger

slugger = GithubSlugger()

slugger.slug('foo')
# returns 'foo'

slugger.slug('foo')
# returns 'foo-1'

slugger.slug('bar')
# returns 'bar'

slugger.slug('foo')
# returns 'foo-2'

slugger.slug('Привет non-latin 你好')
# returns 'привет-non-latin-你好'

slugger.slug('😄 emoji')
# returns '-emoji'

slugger.reset()

slugger.slug('foo')
# returns 'foo'
```

Check [`test/fixtures.json`](test/fixtures.json) for more examples.

If you need, you can also use the underlying implementation which does not keep
track of the previously slugged strings (not recommended):

```python
from github_slugger import slug

slug('foo bar baz')
# returns 'foo-bar-baz'

slug('foo bar baz')
# returns the same slug 'foo-bar-baz' because it does not keep track
```

## Contributing

Contributions welcome! Please read the [contributing guidelines](CONTRIBUTING.md) first.

## License

[ISC](LICENSE)
