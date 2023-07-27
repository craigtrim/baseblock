#!/bin/bash

# Full path of the file
file="setup.py"
projectName="baseblock"
projectVersion="0.2.25"

# Remove the file if it exists
if [ -f "$file" ]; then
    rm "$file"
fi

pushd dist
tar -xf "./${projectName}-${projectVersion}.tar.gz"
mv "./${projectName}-${projectVersion}/setup.py" ..
rm -rf "${projectName}-${projectVersion}"
popd
