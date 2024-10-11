Summary:        SSU configuration for the SailfishOS:Chum community repository
License:        MIT
Name:           sailfishos-chum-repo-config
Version:        0.6.8
Release:        1
# The Group tag should comprise one of the groups listed here:
# https://github.com/mer-tools/spectacle/blob/master/data/GROUPS
Group:          Software Management/Package Manager
BuildArch:      noarch
URL:            https://github.com/sailfishos-chum/%{name}
Vendor:         chum
# Note that the git-tag format for release versions must be `%%{release}/%%{version}`:
Source0:        %{url}/archive/%{release}/%{version}/%{name}-%{version}.tar.gz
# Note that the rpmlintrc file shall be named so according to
# https://en.opensuse.org/openSUSE:Packaging_checks#Building_Packages_in_spite_of_errors
Source99:       %{name}.rpmlintrc
Requires:       ssu
Requires(post): ssu
Requires(postun): ssu
# The oldest SailfishOS release which SailfishOS:Chum supports, because it is the
# oldest useable DoD-repo at https://build.sailfishos.org/project/subprojects/sailfishos
Requires:       sailfish-version >= 3.1.0
# Provide (anti-)dependencies to sibling packages:
Conflicts:      sailfishos-chum-repo-config-testing
Obsoletes:      sailfishos-chum-repo-config-testing
Conflicts:      sailfishos-chum-testing
Obsoletes:      sailfishos-chum-testing
Conflicts:      sailfishos-chum
Obsoletes:      sailfishos-chum
Conflicts:      sailfishos-chum-gui
Conflicts:      sailfishos-chum-gui-installer
Provides:       sailfishos-chum-repository

%description
%{name} is a helper RPM package, which solely provides an appropriate
local repository configuration for utilising the SailfishOS:Chum community
repository with command line tools as pkcon or zypper.

Note that the SailfishOS:Chum GUI application provides the same local
repository configuration, while also providing a GUI app, which can be used in
addition to pkcon or zypper.  Furthermore it offers easy switching between the
regular SailfishOS:Chum repository and the SailfishOS:Chum:Testing repository.
Hence you might rather install the sailfishos-chum-gui RPM package (e.g. via the
sailfishos-chum-gui-installer), instead of the %{name} RPM package.

%if 0%{?_chum}
Title: SailfishOS:Chum repository configuration RPM
Type: generic
Categories:
 - System
 - Utility
 - Settings
 - PackageManager
 - ConsoleOnly
DeveloperName: SailfishOS:Chum community
Custom:
  Repo: %{url}
PackageIcon: %{url}/raw/main/.icons/sailfishos-chum.svg
Links:
  Homepage: https://openrepos.net/content/olf/sailfishoschum-repo-config-rpm
  Help: %{url}/issues
  Bugtracker: %{url}/issues
%endif


%package testing
Summary:        SSU configuration for the SailfishOS:Chum:Testing repository
License:        MIT
Group:          System
BuildArch:      noarch
Requires:       ssu
Requires(post): ssu
Requires(postun): ssu
# The oldest SailfishOS release which SailfishOS:Chum supports, because it is the
# oldest useable DoD-repo at https://build.sailfishos.org/project/subprojects/sailfishos
Requires:       sailfish-version >= 3.1.0
# Provide (anti-)dependencies to sibling packages:
Conflicts:      sailfishos-chum-repo-config
Obsoletes:      sailfishos-chum-repo-config
Conflicts:      sailfishos-chum
Obsoletes:      sailfishos-chum
Conflicts:      sailfishos-chum-testing
Obsoletes:      sailfishos-chum-testing
Conflicts:      sailfishos-chum-gui
Conflicts:      sailfishos-chum-gui-installer
Provides:       sailfishos-chum-repository

%description testing
%{name}-testing is a helper RPM package, which solely provides an appropriate
local repository configuration for utilising the SailfishOS:Chum:Testing
repository with command line tools as pkcon or zypper.

Note that the SailfishOS:Chum:Testing repository is primarily aimed at
software developers.

Also note that the SailfishOS:Chum GUI application provides the same local
repository configuration, while also providing a GUI app, which can be used in
addition to pkcon or zypper.  Furthermore it offers easy switching between the
regular SailfishOS:Chum repository and the SailfishOS:Chum:Testing repository.
Hence you might rather install the sailfishos-chum-gui RPM package (e.g. via the
sailfishos-chum-gui-installer), instead of the %{name}-testing RPM package.

%if 0%{?_chum}
PackageName: SailfishOS:Chum:Testing repository configuration RPM
Type: generic
Categories:
 - System
 - Utility
 - Settings
 - PackageManager
 - ConsoleOnly
DeveloperName: SailfishOS:Chum community
Custom:
  Repo: %{url}
PackageIcon: %{url}/raw/main/.icons/sailfishos-chum.svg
Url:
  Homepage: https://openrepos.net/content/olf/sailfishoschumtesting-repo-config-rpm
  Help: %{url}/issues
  Bugtracker: %{url}/issues
%endif


%define _binary_payload w6.gzdio
%define _source_payload w6.gzdio

%prep
%setup -q

%build

%install

%files

%files testing

%post
# The %%post scriptlet is deliberately run when installing and updating.
# Add sailfishos-chum repository configuration, depending on the installed
# SailfishOS release (3.1.0 is the lowest supported, see lines 22 and 76):
source %{_sysconfdir}/os-release
# Three equivalent variants, but the sed-based ones have additional, ugly
# backslashed quoting of all backslashes, curly braces and brackets (likely
# also quotation marks), and a double percent for a single percent character,
# because they were developed as shell-scripts for `%%define <name> %%(<script>)`
# (the same applies to scriplets with "queryformat-expansion" option -q, see 
# https://rpm-software-management.github.io/rpm/manual/scriptlet_expansion.html#queryformat-expansion ):
# %%define _sailfish_version %%(source %%{_sysconfdir}/os-release; echo "$VERSION_ID" | %%{__sed} 's/^\\(\[0-9\]\[0-9\]*\\)\\.\\(\[0-9\]\[0-9\]*\\)\\.\\(\[0-9\]\[0-9\]*\\).*/\\1\\2\\3/')
# ~: sailfish_version="$(source %%{_sysconfdir}/os-release; echo "$VERSION_ID" | sed 's/^\([0-9][0-9]*\)\.\([0-9][0-9]*\)\.\([0-9][0-9]*\).*/\1\2\3/')"
# Using an extended ("modern") RegEx shortens the sed script, but busybox's sed
# does not support the POSIX option -E for that!  Hence one must resort to the
# non-POSIX option -r for that, without a real gain compared to the basic RegEx:
# %%define _sailfish_version %%(source %%{_sysconfdir}/os-release; echo "$VERSION_ID" | %%{__sed} -r 's/^(\[0-9\]+)\\.(\[0-9\]+)\\.(\[0-9\]+).*/\\1\\2\\3/')
# ~: sailfish_version="$(source %%{_sysconfdir}/os-release; echo "$VERSION_ID" | sed -r 's/^([0-9]+)\.([0-9]+)\.([0-9]+).*/\1\2\3/')"
# Note: Debug output of RPM macros assigned by a %%define statement is best
# done by `echo`s / `printf`s at the start of the %%build section.
# The variant using `cut` and `tr` instead of `sed` does not require extra quoting,
# regardless where it is used (though escaping each quotation mark by a backslash
# might be advisable, when using it inside a %%define statement's `%%()` ).
sailfish_version="$(echo "$VERSION_ID" | cut -s -f 1-3 -d '.' | tr -d '.')"
# Must be an all numerical string of at least three digits:
if echo "$sailfish_version" | grep -q '^[0-9][0-9][0-9][0-9]*$'
then
  if [ "$sailfish_version" -lt 460 ]
  then ssu ar sailfishos-chum 'https://repo.sailfishos.org/obs/sailfishos:/chum/%%(release)_%%(arch)/'
  else ssu ar sailfishos-chum 'https://repo.sailfishos.org/obs/sailfishos:/chum/%%(releaseMajorMinor)_%%(arch)/'
  fi
# Should be enhanced to proper debug output, also writing to systemd-journal:
else echo "Error: VERSION_ID=$VERSION_ID => sailfish_version=$sailfish_version"
fi
ssu ur
exit 0

%post testing
source %{_sysconfdir}/os-release
sailfish_version="$(echo "$VERSION_ID" | cut -s -f 1-3 -d '.' | tr -d '.')"
# Must be an all numerical string of at least three digits:
if echo "$sailfish_version" | grep -q '^[0-9][0-9][0-9][0-9]*$'
then
  if [ "$sailfish_version" -lt 460 ]
  then ssu ar sailfishos-chum-testing 'https://repo.sailfishos.org/obs/sailfishos:/chum:/testing/%%(release)_%%(arch)/'
  else ssu ar sailfishos-chum-testing 'https://repo.sailfishos.org/obs/sailfishos:/chum:/testing/%%(releaseMajorMinor)_%%(arch)/'
  fi
# Should be enhanced to proper debug output, also writing to systemd-journal:
else echo "Error: VERSION_ID=$VERSION_ID => sailfish_version=$sailfish_version"
fi
ssu ur
exit 0

%postun
if [ "$1" = 0 ]
# Removal
then
  ssu rr sailfishos-chum
  rm -f /var/cache/ssu/features.ini
  ssu ur
fi
exit 0

%postun testing
if [ "$1" = 0 ]
# Removal
then
  ssu rr sailfishos-chum-testing
  rm -f /var/cache/ssu/features.ini
  ssu ur
fi
exit 0

# BTW, `ssu`, `rm -f`, `mkdir -p` etc. *always* return with "0" ("success"), hence
# no appended `|| true` needed to satisfy `set -e` for failing commands outside of
# flow control directives (if, while, until etc.).  Furthermore Fedora Docs etc.
# state that solely the final exit status of a whole scriptlet is crucial: 
# See https://docs.pagure.org/packaging-guidelines/Packaging%3AScriptlets.html
# or https://docs.fedoraproject.org/en-US/packaging-guidelines/Scriptlets/#_syntax
# committed on 18 February 2019 by tibbs ( https://pagure.io/user/tibbs ) in
# https://pagure.io/packaging-committee/c/8d0cec97aedc9b34658d004e3a28123f36404324
# Hence only the main section of a spec file and likely also `%%(<shell-script>)`
# statements are executed in a shell called with the option `-e', but not the
# scriptlets: `%%pre*`, `%%post*`, `%%trigger*` and `%%file*`

%changelog
* Thu Sep  9 1999 olf <Olf0@users.noreply.github.com> - 99.99.99
- See %{url}/releases
