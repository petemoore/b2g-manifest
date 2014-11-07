#!/usr/bin/env python
config = {
    "exes": {
        # Get around the https warnings
        "hg": ['/usr/bin/hg', "--config", "web.cacerts=/etc/ssl/certs/ca-certificates.crt"],
        "hgtool.py": ["HGTOOL"],
        "gittool.py": ["GITTOOL"],
    },
    'gecko_pull_url': 'https://hg.mozilla.org/users/pmoore_mozilla.com/b2g-manifest-test/',
    'gecko_push_url': 'ssh://hg.mozilla.org/users/pmoore_mozilla.com/b2g-manifest-test/',
    'manifests_repo': 'B2G_MANIFEST_GIT_URL',
    'manifests_revision': 'B2G_MANIFEST_COMMIT',
    'skip_gaia_json': True,
}
