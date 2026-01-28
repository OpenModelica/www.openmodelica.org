# Fix Joomla export from com_j2grav
# Do not convert HTML to markdown using markdownify

find . -name "*.md" -exec dos2unix "{}" ";"
find . -name "*.md" -exec mac2unix "{}" ";"
sed -i 's/^title: \([^"].*\)/title: "\1"/' */*/*.md
for f in `find . -name "item.md"`; do mv $f `echo $f | sed s,/item.md\$,.md,`; done
find . -type d -exec rmdir "{}" ";"
mv free-and-open-source-software/nightly-builds.md download/nightlybuildsdownload.md
rm free-and-open-source-software/rafael-nadal-all-court-king-95483398.md free-and-open-source-software/top-10-sporting-romances.md
mv uncategorised/download-linux.md download/download-linux.md
mv uncategorised/download-mac.md download/download-mac.md
mv uncategorised/download-virtual-machine.md download/virtual-machine.md
mv uncategorised/download-windows.md download/download-windows.md
mv uncategorised/introduction.md index.md
mv uncategorised/source-code.md download/sourcecodeuser.md
rm free-and-open-source-software/open-source-modelica-consortium.md
mkdir -p home
mv uncategorised/consortium.md home/consortium.md
mv uncategorised/the-goal.md home/goal.md
mv ./uncategorised/roadmap.md home/
mv ./free-and-open-source-software/contact-us.md home/
mkdir -p openmodelicaworld/
mv uncategorised/tools.md openmodelicaworld/
mv uncategorised/commercial-apps.md openmodelicaworld/related-products.md
mkdir -p useresources/
mv uncategorised/userdoc.md useresresources/userdocumentation.md
mv uncategorised/modelicacourses.md useresresources/modelica-courses.md
rm uncategorised/modelicacourses-2.md
mv uncategorised/mailing-lists.md useresresources/mailing-list.md
rm free-and-open-source-software/mailing-list.md
mv free-and-open-source-software/license.md useresresources/
mkdir -p events/modprod/
mv uncategorised/modprod-2021-program.md events/modprod/modprod-2021.md
mv open-modelica/modprod-2020-program.md events/modprod/modprod-2020.md
mv uncategorised/modprod-2019-program.md events/modprod/modprod-2019a.md
mv news/modprod-2018-program.md events/modprod/modprod-2018.md
mv uncategorised/modprod-2017-program.md events/modprod/modprod-2017.md
mv open-modelica/modprod-2016.md events/modprod/modprod-2016.md
mv open-modelica/modprod-2015-program.md events/modprod/modprod-2015.md
mv open-modelica/modprod-2014-program.md events/modprod/modprod-2014.md
mv free-and-open-source-software/modprod.md events/modprod/modprod-2013.md
mv free-and-open-source-software/modprod-2012.md events/modprod/modprod-2012.md
mv free-and-open-source-software/modprod-workshop2011.md events/modprod/modprod-2011.md
rm uncategorised/modprod2011.md
mv free-and-open-source-software/modprod-workshop.md events/modprod/modprod-2010.md
mkdir -p developersresources
mv uncategorised/contributor-license.md developersresources/contributor-license-agreement.md
mkdir -p events/openmodelica-workshop
mv news/openmodelica-annual-workshop-2022-news.md events/openmodelica-workshop/openmodelica-program-2022-a.md
rm news/program-openmodelica-annual-workshop-2021.md
mv news/openmodelica-annual-workshop-2021.md events/openmodelica-workshop/openmodelica-program-2021.md
ln -s ../modprod/modprod-2018.md events/openmodelica-workshop/openmodelica-program-2018.md
mv news/program-openmodelica-annual-workshop-2017.md events/openmodelica-workshop/openmodelica-program-2017.md
mv news/openmodelica-program-2016.md events/openmodelica-workshop/openmodelica-program-2016.md
mv news/openmodelica-program-2015.md events/openmodelica-workshop/openmodelica-program-2015.md
mv news/cfp-openmodelicamodprod-workshops-february-2014.md events/openmodelica-workshop/openmodelica-program-2014.md
mv free-and-open-source-software/final-program-openmodelica-annual-workshop-february-4-2013.md events/openmodelica-workshop/openmodelica-program-2013.md
mv free-and-open-source-software/final-program-openmodelica-annual-workshop-february-6-2012.md events/openmodelica-workshop/program.md
mv free-and-open-source-software/workshop2011.md events/openmodelica-workshop/2011.md
mv free-and-open-source-software/workshop2010.md events/openmodelica-workshop/2010.md
mv uncategorised/sims-2015-conference.md events/sims-2015.md # And need to update links to tutorials+invited talks
mv uncategorised/sims-tutorials.md events/sims-2015-tutorials.md
mv uncategorised/sims-2015-invited-talks.md events/
rm uncategorised/moses-2016.md
mv uncategorised/moses-2016-workshop.md events/moses-2016.md
mv news/eoolt-2017.md events/
rm uncategorised/ifip-wg24-meeting-vadstena-may-20-25-2012.md
rm uncategorised/wg24meeting-in-vadstena-may-20-25-2012.md
rm uncategorised/meeting-vadstena2.md
mkdir -p events/othermeetings
mv uncategorised/meeting-vadstena.md events/othermeetings/ifip-wg24.md
mv uncategorised/seminarium-av-johan-ehrenberg-27-okt-2016.md events/othermeetings/seminarium-av-johan-ehrenberg.md
mv free-and-open-source-software/workshop-contact.md events/contact.md
mkdir -p research
mv free-and-open-source-software/phd-lic-theses.md research/phd-and-licentiate-theses.md
mv free-and-open-source-software/journal-papers.md research/
mv free-and-open-source-software/conference-papers.md research/
mv free-and-open-source-software/recentlycompletedtheses.md research/
mv uncategorised/books.md research/booksproceedings.md
mv latest-news/open-positions.md research/
mv latest-news/open-master-theses.md research/
rm free-and-open-source-software/omoptim-38644409.md
mv uncategorised/omoptim.md research/
mkdir -p research/omoptim
mv free-and-open-source-software/edop.md research/omoptim/
mv uncategorised/moses.md research/
mkdir -p research/moses
ln -s ../../events/moses-2016.md research/moses
mv uncategorised/europrojarticle.md research/europrojects.md
ln -s ../download/sourcecodeuser.md developersresources/source-code.md
ln -s ../download/nightlybuildsdownload.md developersresources/nightly-builds.md
mv uncategorised/devdoc.md developersresources/devdocumentation.md
mv uncategorised/metamodelicacourses.md developersresources/courses.md
mv uncategorised/the-openmodelica-integrated-environment-for-modeling-simulation-and-model-based-development.md research/
mv uncategorised/open-modelica-notebook-1477050.md free-and-open-source-software/omnotebook.md
mv uncategorised/omconnectioneditoromedit.md free-and-open-source-software/
mv uncategorised/modelica-development-tooling-mdt.md free-and-open-source-software/
mv uncategorised/omsimulator.md free-and-open-source-software/

sed -i 's,href="index.php/,href="/,g' */*.md */*/*.md
sed -i 's,href="download/,href="/download/,g' */*.md */*/*.md
sed -i 's,href="doc/,href="/doc/,g' */*.md */*/*.md
sed -i 's,href="svn/,href="https://openmodelica.org/svn/,g' */*.md */*/*.md

sed -i 's,/images/M_images/ModelicaTools,/images/ModelicaTools,g' */*.md */*/*.md

# linkchecker --ignore-url=https://hugo.openmodelica.org/forum --ignore-url=https://hugo.openmodelica.org/doc https://hugo.openmodelica.org |& tee log
