# Contributing to `www.openmodelica.org`

The website is built with [Hugo](https://gohugo.io/) from the Markdown files in `content/`.
The theme in `themes/openmodelica/` sets the look of all pages.
See the [README](README.md) for how to preview the website and create a new page.

## Writing pages

### One sentence per line

Write each sentence on its own line, and leave an empty line between paragraphs.
Do not wrap long sentences.

```markdown
OpenModelica is an open-source Modelica-based modeling and simulation environment.
It is intended for industrial and academic usage.

The development is supported by the Open Source Modelica Consortium.
```

Markdown joins the lines of a paragraph, so the page looks the same.
A change to one sentence then changes one line in the diff.

### No HTML and no styles

Write pages in plain Markdown.
Do not use HTML elements or `style` attributes, and do not set fonts, font sizes, colours or spacing in a page.
The stylesheet `themes/openmodelica/static/css/openmodelica.css` sets the look of all pages.
If a page needs a new look, change the stylesheet.

- Use Markdown headings (`##`, `###`), lists, links, images and `---` for a rule.
- Give a heading an anchor with `{#name}`, for example `## Contact {#contact}`.
- Do not add empty lines or `&nbsp;` for spacing.

Many older pages were exported from Joomla and still contain HTML.
When you change such a page, please convert it to Markdown.

### Tables

Write simple tables in Markdown.

For now, complex tables are the only exception to the rule above.
A table that needs cells over several rows or columns (`rowspan`, `colspan`) can be an HTML table.
Give it the class `table`, and do not add `style`, `border`, `cellpadding` or other layout attributes:

```html
<table class="table">
    <thead>
        <tr><th rowspan="2">Member type</th><th colspan="2">Annual fee in €</th></tr>
        <tr><th>Limited</th><th>Unlimited</th></tr>
    </thead>
    <tbody>
        <tr><td>Individual member</td><td>2600</td><td>4000</td></tr>
    </tbody>
</table>
```

The stylesheet styles `table.table`.

### Generated pages

A Jenkins job generates the bibliography pages in `content/research/` (master theses, PhD theses, papers and the full bibliography).
Do not edit these pages, because the next update overwrites the changes.

## Templates and stylesheets

The Hugo templates and the theme stylesheets are formatted with Prettier.
See [Formatting](README.md#formatting) in the README.
