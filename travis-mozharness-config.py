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
    'gecko_local_dir': 'b2g-inbound',

    'manifests_repo': 'B2G_MANIFEST_GIT_URL',
    'manifests_revision': 'B2G_MANIFEST_COMMIT',

    'hgtool_base_bundle_urls': ['https://ftp-ssl.mozilla.org/pub/mozilla.org/firefox/bundles'],

    'skip_gaia_json': True,

    'devices': {
        'dolphin': {
            'ignore_projects': ['gecko'],
            'ignore_groups': ['darwin'],
        },
        'emulator-kk': {
            'ignore_projects': ['gecko'],
            'ignore_groups': ['darwin'],
        },
        'emulator-jb': {
            'ignore_projects': ['gecko'],
            'ignore_groups': ['darwin'],
        },
        'emulator-ics': {
            'ignore_projects': ['gecko'],
            'ignore_groups': ['darwin'],
            'manifest_file': 'emulator.xml',
        },
        # Equivalent to emulator-ics - see bug 916134
        # Remove once the above bug resolved
        'emulator': {
            'ignore_projects': ['gecko'],
            'ignore_groups': ['darwin'],
            'manifest_file': 'emulator.xml',
        },
        'flame': {
            'ignore_projects': ['gecko'],
            'ignore_groups': ['darwin'],
        },
        'flame-kk': {
            'ignore_projects': ['gecko'],
            'ignore_groups': ['darwin'],
        },
        'hamachi': {
            'ignore_projects': ['gecko'],
            'ignore_groups': ['darwin'],
        },
        'helix': {
            'ignore_projects': ['gecko'],
            'ignore_groups': ['darwin'],
        },
        'nexus-4': {
            'ignore_projects': ['gecko'],
            'ignore_groups': ['darwin'],
        },
        'wasabi': {
            'ignore_projects': ['gecko'],
            'ignore_groups': ['darwin'],
        },
    },
    'repo_remote_mappings': {
        'https://android.googlesource.com/': 'https://git.mozilla.org/external/aosp',
        'git://codeaurora.org/': 'https://git.mozilla.org/external/caf',
        'git://github.com/mozilla-b2g/': 'https://git.mozilla.org/b2g',
        'git://github.com/mozilla/': 'https://git.mozilla.org/b2g',
        'https://git.mozilla.org/releases': 'https://git.mozilla.org/releases',
        'http://android.git.linaro.org/git-ro/': 'https://git.mozilla.org/external/linaro',
        'http://sprdsource.spreadtrum.com:8085/b2g/android': 'https://git.mozilla.org/external/sprd-aosp',
        'git://github.com/apitrace/': 'https://git.mozilla.org/external/apitrace',
        'git://github.com/t2m-foxfone/': 'https://git.mozilla.org/external/t2m-foxfone',
        # Some mappings to ourself, we want to leave these as-is!
        'https://git.mozilla.org/external/aosp': 'https://git.mozilla.org/external/aosp',
        'https://git.mozilla.org/external/caf': 'https://git.mozilla.org/external/caf',
        'https://git.mozilla.org/b2g': 'https://git.mozilla.org/b2g',
        'https://git.mozilla.org/external/apitrace': 'https://git.mozilla.org/external/apitrace',
        'https://git.mozilla.org/external/t2m-foxfone': 'https://git.mozilla.org/external/t2m-foxfone',
    },
}
