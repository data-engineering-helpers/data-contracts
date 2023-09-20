Data Contracts - Datacontract.com
=================================

# Overview
[This page](https://github.com/data-engineering-helpers/data-contracts/blob/main/datacontract.com/README.md)
is a deep dive on the [datacontract.com](https://datacontract.com/) ecosystem,
which includes an
[open specification](https://datacontract.com/) and
[some utilities](https://cli.datacontract.com/).

It is part of the larger
[Data contracts initiative](https://github.com/data-engineering-helpers/data-contracts).

# References
* Data Contract Specification: https://datacontract.com/
* Data contract command-line (CLI) utility:
  https://cli.datacontract.com/ (GitHub: https://github.com/datacontract/cli)
* Data Contract Studio: https://studio.datacontract.com/

# Quickstart
* Check the validity of the data contract:
```bash
$ datacontract validate --file contracts/orders-latest-npii.yaml
🟢 data contract is valid!
```

* Generate a new data contract:
```bash
$ datacontract init
📄 data contract written to datacontract.yaml
```

* Open the newly created data contract in Data Contract Studio:
```bash
$ datacontract open
🌐 opening data contract at https://studio.datacontract.com/s/c8b27fe3-62dc-4a21-ae41-9471ce7859d7
```

* The data contract may be edited in Data Contract Studio directly:
  https://studio.datacontract.com/s/c8b27fe3-62dc-4a21-ae41-9471ce7859d7/edit

* Create a local replication of some existing data contract in
  Data Contract Studio:
```bash
$ datacontract init --from https://studio.datacontract.com/s/c8b27fe3-62dc-4a21-ae41-9471ce7859d7.yaml
📄 data contract written to datacontract.yaml
```

# Installation
* Install the `datacontract` CLI (command-line) utility

## On MacOS
* With HomeBrew
```bash
$ brew install datacontract/brew/datacontract
```

## On Linux
* Specify the platform and architecture of the machine:
```bash
export platform="$(uname | tr '[:upper:]' '[:lower:]')"
export architecture="$(uname -m|sed 's/x86_/amd/')"
```

* From the [GitHub releases](https://github.com/datacontract/cli/releases)
  + Specify the latest version:
```bash
$ DC_VERSION="0.1.1"
  DC_FN="datacontract-v$DC_VERSION-$platform-$architecture.tar.gz"
```
  + Download the CLI utility:
```bash
$ mkdir -p /tmp/datacontract
  pushd /tmp/datacontract
  curl -kL https://github.com/datacontract/cli/releases/download/v$DC_VERSION/$DC_FN -o $DC_FN
```
  + Install the CLI utility:
```bash
$ mkdir -p ~/.local/bin
  tar zxf $DC_FN && rm -f $DC_FN
  mv datacontract ~/.local/bin/ && rm -f LICENSE README.md
  popd
```

## General
* Check the version:
```bash
$ datacontract --version
datacontract version v0.1.1
```

