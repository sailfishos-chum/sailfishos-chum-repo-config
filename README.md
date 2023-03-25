# SailfishOS:Chum repository configuration RPM(s)
The SailfishOS:Chum community repository configuration RPMs work on any SailfishOS release ≥ 3.1.0 and on all CPU-architectures.

### How to deploy the configuration for command line tools
See https://github.com/sailfishos-chum/main#how-to-deploy-the-configuration-for-command-line-tools.

### Important note
Note that, before software can be build for a SailfishOS release at the SailfishOS-OBS, Jolla must create a corresponding "download on demand (DoD)" OBS-repository.  It may take a little time after a new SailfishOS release is published before the corresponding "DoD" repository is being made available, during which installing  or updating any software from the SailfishOS:Chum community repository on a device with the new SailfishOS release already installed does not work, because it cannot be compiled for this new SailfishOS release at the Sailfish-OBS, yet; consequently this is always the case for "closed beta (cBeta)" releases of SailfishOS.

But because this is a SailfishOS release independent `noarch` package, you can simply install a [recent RPM file from OpenRepos](https://openrepos.net/content/olf/sailfishoschum-repo-config-rpm) (e.g., conveniently via [Storeman](https://openrepos.net/content/olf/sailfishoschum-gui-installer)), a [recent RPM file from GitHub's releases page](https://github.com/sailfishos-chum/sailfishos-chum-repo-config/releases), manually select an RPM file built for any SailfishOS release or CPU architecture from [chumrpm.netlify.app](https://chumrpm.netlify.app/), or fully manually select an RPM file built for any SailfishOS release or CPU architecture from [the SailfishOS-OBS](https://build.merproject.org/package/show/sailfishos:chum/sailfishos-chum-repo-config).
