# www.openmodelica.org

In order to test the webpage locally:

```bash
hugo serve
```

This prints the URL at which you can preview the webpage (minus some files that are only on the server and not in Git).
When files are modified, there is a JavaScript that will reload the browser window.

To create a new page:

```bash
hugo new content/news/openmodelica-1.21.0.md
```

And then edit the template in a text editor.

## config.toml

The config.toml file contains parameters that can be used inside of articles.
For example, it is possible to write code like:

```markdown
Report bugs in [GitHub]({{< param "bugreporting" >}})
```

There are also parameters for the release, stable and nightly versions that can be used to generate webpages.

## Download statistics

The [Download Statistics](https://openmodelica.org/download/statistics) page shows `/api/statistics.json`.
That file is not in Git: the Jenkins job runs `scripts/statistics.py` before `hugo`, which reads the monthly
numbers from the AWStats of build.openmodelica.org and writes `static/api/statistics.json`.

- The numbers are the sum rows of the AWStats extra sections in `scripts/awstats/extra-sections.conf`,
  which must be part of `/etc/awstats/awstats.conf.local` on the web server.
- The AWStats login is the Jenkins username/password credential with the ID `awstats`.
- Pull requests and builds without the login reuse the published numbers.

To see the page locally with the published numbers:

```bash
python3 scripts/statistics.py
hugo serve
```

## Formatting

The Hugo templates (`layouts/`, `themes/openmodelica/layouts/`) and the theme stylesheets are formatted with
[Prettier](https://prettier.io/) and the Go template plugin, with the settings in `.prettierrc.json`.
Page content is not formatted. A GitHub workflow checks the formatting of every pull request.

```bash
npm install
npm run format        # format all files
npm run check-format  # only check
```

Prettier breaks `{{ if }}…{{ else }}…{{ end }}` blocks inside attribute values onto several lines,
which puts line breaks into the value. Use a single action instead, for example
`href="{{ .Params.external_url | default .RelPermalink }}"`.
