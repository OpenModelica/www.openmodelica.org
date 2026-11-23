// Shows the BibTeX source of a bibliography entry in a dialog when its
// "BibTeX" link is clicked. The link still leads to the BibTeX page without
// JavaScript, or when /api/bibtex.json, written by scripts/bibliography.py,
// cannot be loaded.
(function () {
  "use strict";
  var links = document.querySelectorAll('a[href*="/research/openmodelica_bib#"]');
  if (!links.length) {
    return;
  }

  var sources = null;
  function load() {
    if (!sources) {
      sources = fetch("/api/bibtex.json").then(function (response) {
        if (!response.ok) {
          throw new Error(response.status);
        }
        return response.json();
      });
      sources.catch(function () {
        sources = null;
      });
    }
    return sources;
  }

  var dialog = document.createElement("dialog");
  dialog.className = "bibtex-dialog";
  dialog.innerHTML =
    '<div class="bibtex-box">' +
    '<div class="bibtex-head"><strong></strong>' +
    '<button type="button" class="bibtex-copy">Copy</button>' +
    '<button type="button" class="bibtex-close" aria-label="Close">&times;</button></div>' +
    "<pre></pre></div>";
  document.body.appendChild(dialog);
  var title = dialog.querySelector("strong");
  var pre = dialog.querySelector("pre");
  var copy = dialog.querySelector(".bibtex-copy");

  dialog.querySelector(".bibtex-close").addEventListener("click", function () {
    dialog.close();
  });
  // A click on the backdrop closes the dialog; Escape closes it too.
  dialog.addEventListener("click", function (event) {
    if (event.target === dialog) {
      dialog.close();
    }
  });
  copy.addEventListener("click", function () {
    navigator.clipboard.writeText(pre.textContent).then(
      function () {
        copy.textContent = "Copied";
      },
      function () {
        var range = document.createRange();
        range.selectNodeContents(pre);
        var selection = window.getSelection();
        selection.removeAllRanges();
        selection.addRange(range);
      }
    );
  });

  links.forEach(function (link) {
    link.addEventListener("click", function (event) {
      if (event.button !== 0 || event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) {
        return;
      }
      event.preventDefault();
      var key = decodeURIComponent(link.hash.slice(1));
      load().then(
        function (data) {
          if (!(key in data)) {
            window.location.href = link.href;
            return;
          }
          title.textContent = key;
          pre.textContent = data[key];
          copy.textContent = "Copy";
          dialog.showModal();
        },
        function () {
          window.location.href = link.href;
        }
      );
    });
  });
})();
