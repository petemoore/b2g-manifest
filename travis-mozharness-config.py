#!/usr/bin/env python
config = {
    "exes": {
        # Get around the https warnings
        "hg": ['/usr/bin/hg', "--config", "web.cacerts=/etc/ssl/certs/ca-certificates.crt"],
        "hgtool.py": ["HGTOOL"],
        "gittool.py": ["GITTOOL"],
    },
    'manifests_repo': 'B2G_MANIFEST_GIT_URL',
    'manifests_revision': 'B2G_MANIFEST_COMMIT',
    'skip_gaia_json': True,
}
