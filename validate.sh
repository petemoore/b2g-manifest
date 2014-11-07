#!/bin/bash

# This script is run by travis for the CI of b2g-manifest.
# It is designed to catch problems that would otherwise only
# be found when b2g bumper bot runs in production, that
# potentially can cause tree closures.
# It installs and runs b2g bumper locally, without committing
# nor pushing back to hg, to check that repos referenced exist
# and are readable, referenced heads/tags exist, and that they
# are correctly mirrored on git.mozilla.org.
# Gaia is excluded from testing, since access to cruncher is
# required to map hg sha to git sha, whereas these tests are
# more concerned with invalid repos/branches/tags getting
# added to a manifest.

# Please note the retry function is intentionally not disabled
# just as the real b2g bumper in production uses a retry
# function, so that bad changes to b2g-manifest that cause
# breakage will take several minutes to fail after several
# iterations of retries. This is to avoid that an intermittent
# failure will cause travis CI to fail.

function replace {
    local file="${1}"
    local tokenname="${2}"
    local replacestring="${3}"
    # don't use sed -i so we can test on mac
    mv "${file}" "${file}.orig"
    cat "${file}.orig" | sed "s@${tokenname}@${replacestring}@g" > "${file}"
    rm "${file}.orig"
}

set -xv
B2G_MANIFEST_GIT_URL="$(git config --get remote.origin.url)"
B2G_MANIFEST_COMMIT="${TRAVIS_COMMIT}"

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
replace "${B2GBUMPER_DIR}/travis-mozharness-config.py" B2G_MANIFEST_GIT_URL "${B2G_MANIFEST_GIT_URL}"
replace "${B2GBUMPER_DIR}/travis-mozharness-config.py" B2G_MANIFEST_COMMIT "${B2G_MANIFEST_COMMIT}"

echo "Running b2g bumper..."
mozharness/scripts/b2g_bumper.py -c "mozharness/configs/b2g_bumper/master.py" -c "${B2GBUMPER_DIR}/travis-mozharness-config.py" --no-check-treestatus --no-commit-manifests
