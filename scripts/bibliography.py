#!/usr/bin/env python3
"""Generate the bibliography pages of the Research menu as Markdown.

Downloads openmodelica.bib from the OpenModelica repository and writes into
content/research/:

  journal-papers.md, conference-papers.md, phd-and-licentiate-theses.md,
  master-theses.md    the entries of one BibTeX type each, grouped by year,
                      newest first
  openmodelica.md     all entries, sorted by author
  openmodelica_bib.md the BibTeX source of all entries

The pages are not in Git; the Jenkins job of this website runs this script
before hugo. The Jenkins job of OpenModelica starts the website job when
openmodelica.bib changed on master.

Every entry is a paragraph with its BibTeX key as id, so that links like
/research/openmodelica#<key> keep working. This needs the Goldmark option
markup.goldmark.parser.attribute.block in config.toml.

Only the Python standard library is needed.
"""

import argparse
import os
import re
import sys
import time
import urllib.request

URL = "https://raw.githubusercontent.com/OpenModelica/OpenModelica/master/doc/bibliography/openmodelica.bib"

# The pages and their front matter.
# The pages, their front matter and the BibTeX types of their entries.
PAGES = {
    "journal-papers": ('title: "Journal Articles"', {"article"}),
    "conference-papers": ('title: "Conference Papers"', {"inproceedings", "conference", "incollection"}),
    "phd-and-licentiate-theses": ('title: "Doctoral and Licentiate Theses"', {"phdthesis"}),
    "master-theses": ('title: "Master Theses"\naliases: ["/research/recentlycompletedtheses"]', {"mastersthesis"}),
}
ALL = 'title: "OpenModelica Bibliography"'
BIB = 'title: "openmodelica.bib"'

MONTHS = {m: i + 1 for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"])}

ACCENTS = {
    '"': {"a": "ä", "o": "ö", "u": "ü", "A": "Ä", "O": "Ö", "U": "Ü", "e": "ë", "i": "ï"},
    "'": {"a": "á", "e": "é", "i": "í", "o": "ó", "u": "ú", "E": "É"},
    "`": {"a": "à", "e": "è", "o": "ò", "u": "ù"},
    "^": {"a": "â", "e": "ê", "o": "ô", "u": "û"},
    "~": {"n": "ñ", "a": "ã", "o": "õ"},
    "c": {"c": "ç", "C": "Ç"},
}
SYMBOLS = {"AA": "Å", "aa": "å", "o": "ø", "O": "Ø", "ss": "ß", "ae": "æ", "AE": "Æ", "&": "&", "%": "%", "_": "_", "$": "$", "#": "#"}


class Entry:
    def __init__(self, kind, key, fields, source):
        self.kind = kind.lower()
        self.key = key
        self.fields = fields
        self.source = source

    def get(self, name, default=""):
        return self.fields.get(name, default)


def fail(msg):
    sys.exit("bib2md.py: " + msg)


def read_value(text, i):
    """Read a field value starting at text[i]; return (value, next index)."""
    parts = []
    while True:
        while text[i].isspace():
            i += 1
        if text[i] == "{":
            depth, j = 0, i
            while True:
                if text[j] == "\\":
                    j += 2
                    continue
                if text[j] == "{":
                    depth += 1
                elif text[j] == "}":
                    depth -= 1
                    if depth == 0:
                        break
                j += 1
            parts.append(text[i + 1:j])
            i = j + 1
        elif text[i] == '"':
            j = i + 1
            depth = 0
            while text[j] != '"' or depth > 0:
                if text[j] == "\\":
                    j += 1
                elif text[j] == "{":
                    depth += 1
                elif text[j] == "}":
                    depth -= 1
                j += 1
            parts.append(text[i + 1:j])
            i = j + 1
        else:
            m = re.compile(r"[^\s,}#]+").match(text, i)
            parts.append(m.group(0))
            i = m.end()
        while text[i].isspace():
            i += 1
        if text[i] != "#":
            return "".join(parts), i
        i += 1


def parse(text):
    entries = []
    for m in re.finditer(r"^[ \t]*@([a-zA-Z]+)[ \t]*\{[ \t]*([^,\s]+)[ \t]*,", text, re.M):
        start, i = m.start(), m.end()
        fields = {}
        while True:
            while text[i].isspace() or text[i] == ",":
                i += 1
            if text[i] == "}":
                break
            f = re.compile(r"([a-zA-Z0-9_-]+)\s*=\s*").match(text, i)
            if not f:
                fail("cannot parse a field of %s near: %s" % (m.group(2), text[i:i + 40]))
            value, i = read_value(text, f.end())
            fields[f.group(1).lower()] = " ".join(value.split())
        entries.append(Entry(m.group(1), m.group(2), fields, text[start:i + 1].strip()))
    return entries


def latex(s):
    """Convert the LaTeX used in openmodelica.bib to plain text."""
    s = s.replace("\\-", "")

    def accent(m):
        table = ACCENTS.get(m.group(1), {})
        return table.get(m.group(2), m.group(2))
    s = re.sub(r"\\([\"'`^~c])\s*\{?\s*([a-zA-Z])\s*\}?", accent, s)
    s = re.sub(r"\{?\\(AA|aa|ss|ae|AE|o|O)\}?(?![a-zA-Z])", lambda m: SYMBOLS[m.group(1)], s)
    s = re.sub(r"\\([&%_$#])", lambda m: SYMBOLS[m.group(1)], s)
    s = s.replace("---", "—").replace("--", "–").replace("~", "\u00a0")
    s = s.replace("{", "").replace("}", "")
    return " ".join(s.split())


def md(s):
    """Escape plain text for Markdown."""
    return re.sub(r"([\\`*_\[\]<>])", r"\\\1", s)


def resolve(entries):
    byKey = {e.key: e for e in entries}
    for e in entries:
        ref = e.fields.get("crossref")
        if ref:
            parent = byKey.get(ref)
            if parent is None:
                fail("%s: crossref %s not found" % (e.key, ref))
            # The title of the proceedings or the book that a paper is part
            # of is the booktitle of the paper.
            part = parent.kind in ("proceedings", "book") and e.kind != parent.kind
            for name, value in parent.fields.items():
                if name == "title" and part:
                    e.fields.setdefault("booktitle", value)
                elif name not in ("key", "crossref"):
                    e.fields.setdefault(name, value)
    return byKey


def names(field):
    result = []
    for name in re.split(r"\s+and\s+", latex(field)):
        if "," in name:
            last, first = [p.strip() for p in name.split(",", 1)]
            name = first + " " + last
        result.append(name.strip())
    if len(result) <= 2:
        return " and ".join(result)
    return ", ".join(result[:-1]) + ", and " + result[-1]


def year(e):
    y = re.search(r"[0-9]{4}", e.get("year"))
    return int(y.group(0)) if y else 0


def month(e):
    m = e.get("month").strip().lower()
    if m.isdigit():
        return int(m)
    return MONTHS.get(m[:3], 0)


def sentence(*parts):
    text = ", ".join(p for p in parts if p)
    if text and not text.endswith((".", "?", "!")):
        text += "."
    return text


def cite_links(note, base, byKey):
    """The note with each \\cite{key,...} as links to the cited entries."""
    out = []
    for i, part in enumerate(re.split(r"\\cite\{([^}]*)\}", note)):
        if i % 2:
            links = []
            for k in (k.strip() for k in part.split(",")):
                text = latex(byKey[k].get("title")) if k in byKey else k
                links.append("[%s](%sopenmodelica#%s)" % (md(text), base, k))
            out.append(", ".join(links))
        else:
            text = md(latex(part))
            out.append((" " if part[:1].isspace() else "") + text + (" " if part[-1:].isspace() and text else ""))
    return "".join(out)


def render(e, base, byKey):
    """The Markdown paragraph for one entry."""
    f = lambda name: latex(e.get(name))
    authors = names(e.get("author")) if e.get("author") else ""
    editors = names(e.get("editor")) if e.get("editor") else ""
    title = md(f("title"))
    pages = f("pages")
    lines = []
    if e.kind in ("book", "proceedings"):
        who = authors or (editors + (", editors" if " and " in editors else ", editor") if editors else "")
        lines.append(sentence(md(who)))
        lines.append(sentence("**%s**" % title, md(f("edition") and f("edition") + " edition"), md(f("publisher")), md(f("address")), str(year(e) or "")))
    else:
        lines.append(sentence(md(authors)))
        if e.kind == "article":
            volume = f("volume") + ("(%s)" % f("number") if f("number") else "")
            if pages:
                volume += (":" if volume else "pages ") + pages
            lines.append("**%s**" % sentence(title))
            lines.append(sentence("*%s*" % md(f("journal")) if f("journal") else "", md(volume), str(year(e) or "")))
        elif e.kind in ("inproceedings", "incollection", "conference"):
            lines.append("**%s**" % sentence(title))
            book = "In *%s*" % md(f("booktitle")) if f("booktitle") else ""
            lines.append(sentence(book, md("pages " + pages) if pages else "", md(f("publisher")), md(f("address")), str(year(e) or "")))
        elif e.kind in ("mastersthesis", "phdthesis"):
            kind = f("type") or ("Master's thesis" if e.kind == "mastersthesis" else "PhD thesis")
            lines.append("**%s**" % sentence(title))
            lines.append(sentence(md(kind), md(f("school")), md(f("address")), str(year(e) or "")))
        elif e.kind == "techreport":
            report = "Technical report" + (" " + f("number") if f("number") else "")
            lines.append("**%s**" % sentence(title))
            lines.append(sentence(md(report), md(f("institution")), str(year(e) or "")))
        else:
            lines.append("**%s**" % sentence(title))
            lines.append(sentence(md(f("howpublished")), md(f("publisher")), str(year(e) or "")))
    for name in ("supervisor", "examiner"):
        if e.get(name):
            lines.append(sentence(md(f(name))))
    if e.get("note"):
        lines.append(sentence(cite_links(e.get("note"), base, byKey)))
    links = ["[BibTeX](%sopenmodelica_bib#%s)" % (base, e.key)]
    if e.get("doi"):
        doi = re.sub(r"^https?://(dx\.)?doi\.org/", "", e.get("doi"))
        links.append("[DOI](https://doi.org/%s)" % doi)
    for name, label in (("pdf", "PDF"), ("slide", "Slides"), ("url", "Link"), ("http", "Link")):
        if e.get(name) and not (name == "http" and e.get("url")):
            links.append("[%s](%s)" % (label, e.get(name)))
    lines.append(" · ".join(links))
    lines = [l for l in lines if l]
    lines.append('{id="%s" class="bib-entry"}' % e.key)
    return "\n".join(lines)


def read(source):
    """The text of a local file or of a URL, tried three times."""
    if not re.match(r"https?://", source):
        with open(source, encoding="utf-8") as fin:
            return fin.read()
    for attempt in range(3):
        try:
            with urllib.request.urlopen(source, timeout=60) as fin:
                return fin.read().decode("utf-8")
        except OSError as e:
            if attempt == 2:
                fail("cannot download %s: %s" % (source, e))
            time.sleep(10)


def front_matter(fields):
    return ("---\n%s\n# Generated by scripts/bibliography.py from openmodelica.bib; do not edit.\n---\n"
            % fields)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--bib", default=URL, help="URL or file of openmodelica.bib (default: %(default)s)")
    ap.add_argument("--output-dir", default="content/research")
    ap.add_argument("--base", default="/research/", help="URL of the bibliography pages")
    args = ap.parse_args()

    entries = parse(read(args.bib))
    byKey = resolve(entries)
    os.makedirs(args.output_dir, exist_ok=True)

    def write(name, text):
        with open(os.path.join(args.output_dir, name + ".md"), "w", encoding="utf-8") as fout:
            fout.write(text)

    for t, (fields, kinds) in PAGES.items():
        # The bib has variants of some entries, e.g. "<key>:citerelated" with
        # a note or "<key>:workaround" for the User's Guide; a page shows
        # entries with the same title and year once, with the shortest key.
        unique = {}
        for e in sorted((e for e in entries if e.kind in kinds), key=lambda e: (len(e.key), e.key)):
            unique.setdefault((latex(e.get("title")).lower(), year(e)), e)
        cited = sorted(unique.values(), key=lambda e: (-year(e), -month(e), e.key.lower()))
        out, current = [front_matter(fields)], None
        for e in cited:
            if year(e) != current:
                current = year(e)
                out.append("\n## %s\n" % current)
            out.append("\n" + render(e, args.base, byKey) + "\n")
        write(t, "".join(out))

    def sortkey(e):
        """Sort by the last name of the first author or editor, like
        bibtex2html, or by the key field or the title."""
        who = e.get("author") or e.get("editor")
        if who:
            first = re.split(r"\s+and\s+", latex(who))[0]
            name = first.split(",")[0] if "," in first else first.split(" ")[-1]
        else:
            name = latex(e.get("key") or e.get("title"))
        return (name.lower(), -year(e), e.key.lower())
    out = [front_matter(ALL)]
    for e in sorted(entries, key=sortkey):
        out.append("\n" + render(e, args.base, byKey) + "\n")
    write("openmodelica", "".join(out))

    out = [front_matter(BIB)]
    for e in sorted(entries, key=sortkey):
        out.append('\n### [%s](%sopenmodelica#%s) {id="%s"}\n\n```bibtex\n%s\n```\n' % (md(e.key), args.base, e.key, e.key, e.source))
    write("openmodelica_bib", "".join(out))


if __name__ == "__main__":
    main()
