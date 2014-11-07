#!/bin/bash -euxv

function replace {
    local file="${1}"
    local tokenname="${2}"
    local replacestring="${3}"
    # don't use sed -i so we can test on mac
    mv "${file}" "${file}.orig"
    cat "${file}.orig" | sed "s@${tokenname}@${replacestring}@g" > "${file}"
    rm "${file}.orig"
}

find . -name '*.xml' | while read file; do
    replace "${file}" '^.*path="gaia".*' '<!-- filter out gaia for CI test & -->'
done
B2GBUMPER_DIR="$(pwd)"
cd ..
echo "Installing mozharness..."
echo "Current directory: '$(pwd)'"
git clone -b bug1091084 https://github.com/petemoore/build-mozharness mozharness
echo "Installing tools..."
git clone https://github.com/mozilla/build-tools tools

HGTOOL_PATH="$(find "$(pwd)/tools" -name hgtool.py)"
GITTOOL_PATH="$(find "$(pwd)/tools" -name gittool.py)"

echo "Replacing references to hgtool.py and gittool.py to versions checked out in tools repo..."
replace "${B2GBUMPER_DIR}/travis-mozharness-config.py" HGTOOL "${HGTOOL_PATH}"
replace "${B2GBUMPER_DIR}/travis-mozharness-config.py" GITTOOL "${GITTOOL_PATH}"

echo "Running b2g bumper..."
mozharness/scripts/b2g_bumper.py -c "${B2GBUMPER_DIR}/travis-mozharness-config.py" --no-check-treestatus --no-commit-manifests
