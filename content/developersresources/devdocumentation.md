---
title: "Developer Documentation"
---

* <a href="/documents/">OpenModelica Eclipse Developement Tool, setup and workspace</a>
* <a href="https://github.com/OpenModelica/OpenModelica/blob/master/doc/OpenModelicaSystem.pdf">System Documentation</a>
* <a href="https://github.com/OpenModelica/OpenModelica/blob/master/doc/OpenModelicaMetaProgramming.pdf">MetaModelica Users Guide</a>
* <a href="https://build.openmodelica.org/Documentation/MetaModelica.html">MetaModelica language extension APIs</a>
* <a href="https://www.openmodelica.org/doc/OpenModelicaUsersGuide/latest/scripting_api.html">OpenModelica Scripting APIs documentation</a>
* <a href="https://build.openmodelica.org/Documentation/">Modelica functions documentation and implementation</a>
* <a href="https://github.com/OpenModelica/OpenModelica/blob/master/doc/OpenModelicaTemplateProgramming.pdf">OpenModelica Template Programming</a>
* <a href="https://trac.openmodelica.org/OpenModelica/wiki/WritingCompliantLibraries">Writing compliant libraries</a>
* <a href="https://libraries.openmodelica.org/branches/">OpenModelica library testing current status</a>
* <a href="https://github.com/OpenModelica/OpenModelica/tree/master/OMEdit/OMEditLIB/Resources/nls">OMEdit localizations, e.g. menus in different languages</a>
* <a href="https://trac.openmodelica.org/OpenModelica/wiki/WritingEfficientMetaModelica">Writing efficient MetaModelica</a>

Courses on MetaModelica are available <a href="/developersresources/courses">here</a>

OpenModelica is constantly evolving, especially from the developers point of view, developers are suggested to ask any question on <a href="https://github.com/OpenModelica/OpenModelica">GitHub</a>.

## Operating systems we support

The following is a list of the Linux operating systems we currently build releases for and need to continue working.
Once the end of life date set by the manufacturer, the operating systems in this list are automatically removed (but can be removed earlier than that if no OSMC organizational member needs it supported).

<table id="linux-supported-systems">
</table>

<script>
var getJSON = function(url, callback) {
  var xhr = new XMLHttpRequest();
  xhr.open('GET', url, true);
  xhr.responseType = 'json';
  xhr.onload = function() {
  var status = xhr.status;
  if (status === 200) {
    callback(null, xhr.response);
  } else {
    callback(status, xhr.response);
  }
  };
  xhr.send();
};
getJSON('/api/linux.json', function(err, data) {
  var content = [];
  if (err !== null) {
    content = "Failed to load JSON-file: " + err;
  } else {
    console.log(data);
    allOS = [...data.deb.amd64].concat(Object.keys(data.rpm.amd64))
    content += ['<tr><th class="headerSort" onclick="sortTable(0)">OS</th><th class="headerSort" onclick="sortTable(1)">EOL</th><th class="headerSort" onclick="sortTable(2)">cmake</th><th class="headerSort" onclick="sortTable(3)">gcc</th><th class="headerSort" onclick="sortTable(4)">clang</th></tr>']
    for (const os of allOS) {
        content += ["<tr><td>" + os + "</td><td>" + data.eol[os] + "</td><td>"+data.pkg.cmake[os]+"</td><td>"+data.pkg.gcc[os]+"</td><td>"+data.pkg.clang[os]+"</td></tr>"];
    }
  }
  console.log(content);
  document.getElementById("linux-supported-systems").innerHTML=content;
});
function sortTable(n) {
  var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
  table = document.getElementById("linux-supported-systems");
  switching = true;
  // Set the sorting direction to ascending:
  dir = "asc";
  /* Make a loop that will continue until
  no switching has been done: */
  while (switching) {
    // Start by saying: no switching is done:
    switching = false;
    rows = table.rows;
    /* Loop through all table rows (except the
    first, which contains table headers): */
    for (i = 1; i < (rows.length - 1); i++) {
      // Start by saying there should be no switching:
      shouldSwitch = false;
      /* Get the two elements you want to compare,
      one from current row and one from the next: */
      x = rows[i].getElementsByTagName("TD")[n];
      y = rows[i + 1].getElementsByTagName("TD")[n];
      /* Check if the two rows should switch place,
      based on the direction, asc or desc: */
      if (dir == "asc") {
        if (1==x.innerHTML.localeCompare(y.innerHTML, undefined, {numeric: true, sensitivity: 'base'})) {
          // If so, mark as a switch and break the loop:
          shouldSwitch = true;
          break;
        }
      } else if (dir == "desc") {
        if (-1==x.innerHTML.localeCompare(y.innerHTML, undefined, {numeric: true, sensitivity: 'base'})) {
          // If so, mark as a switch and break the loop:
          shouldSwitch = true;
          break;
        }
      }
    }
    if (shouldSwitch) {
      /* If a switch has been marked, make the switch
      and mark that a switch has been done: */
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
      // Each time a switch is done, increase this count by 1:
      switchcount ++;
    } else {
      /* If no switching has been done AND the direction is "asc",
      set the direction to "desc" and run the while loop again. */
      if (switchcount == 0 && dir == "asc") {
        dir = "desc";
        switching = true;
      }
    }
  }
}
</script>