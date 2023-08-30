Schemata - Quickstart
=====================

# Table of Content (ToC)
* [References](#references)
* [Initialization](#initialization)
  * [Java and Maven](#java-and-maven)
  * [Data contracts - Schema Quickstart](#data-contracts---schema-quickstart)
  * [Additional utilities](#additional-utilities)
* [Generate Schemata JAR artifact](#generate-schemata-jar-artifact)
* [Schemata utilities to validate and document the data contracts](#schemata-utilities-to-validate-and-document-the-data-contracts)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

# References
* [GitHub - Data Engineering helpers - Data contracts (this project)](https://github.com/data-engineering-helpers/data-contracts)

# Initialization

## Java and Maven
* If not already done so, install Java (JDK 17) and Maven. The easiest
  is to use [SDKMan](https://sdkman.io/)
  + To install SDKMan (behind some corporate firewalls, one may need to setup
    a proxy with `http` and `https` Shell environment variables):
```bash
$ curl -s "https://get.sdkman.io" | bash
```
  + Proceed as requested by SDKMan (check that the SDKMan
    initialization is done properly within the Shell init scripts)

* In order to check the currently installed versions of Java, Maven
  and so on, use `sdk list tool`, for instance:
  + Check the installed versions of Java:
```bash
$ sdk list java
```
  + Check the installed versions of Maven:
```bash
$ sdk list maven
```

* Install the Amazon Coretto JDK17 (or whatever else JDK you prefer,
  but it has to be some JDK with version 17):
```bash
$ sdk install java 17.0.6-amzn
```

* Install Maven:
```bash
$ sdk install maven 3.9.1
```

## Protobuf
* If not already done so, Install Protocol Buffer Compiler https://grpc.io/docs/protoc-installation/
On Mac: 
```bash
$ brew install protobuf
```

On Linux, using apt or apt-get:
```bash
$ apt install -y protobuf-compiler
```

## Data contracts - Schema Quickstart
* If not already done so, clone the
  [Data contracts Git repository](https://github.com/data-engineering-helpers/data-contracts)

* Go into the
  [Data contracts Schemata quickstart directory](https://github.com/data-engineering-helpers/data-contracts/tree/main/schemata/quickstart):
```bash
$ pushd ~/dev/infra/data-contracts/schemata/quickstart
```

## Additional utilities
* [JQ](https://stedolan.github.io/jq/) comes handy to parse JSON structures.
   It is packages on most of the systems (MacOS, Linux)

# Generate Schemata JAR artifact
As of April 2023, Schemata does not release its JAR artifact on public
repositories such as Maven Central. Hence, one has to clone the Schemata
Git repository and to generate the JAR artifact locally.

* If not already done so, clone the Schemata Git repository:
```bash
$ mkdir -p ~/dev/infra && \
  git clone git@github.com:ananthdurai/schemata.git ~/dev/infra/schemata
```

* Go into the Schemata directory:
```bash
  pushd ~/dev/infra/schemata
```

* Compile and package (generate the JAR artifact for) Schemata:
```bash
$ make build-all
```

* Check that the JAR artifacts have been correctly generated:
```bash
$ ls -lFh target/*.jar
-rw-r--r--  1 user  staff 112K Apr 13 16:27 target/original-schemata-1.0.jar
-rw-r--r--  1 user  staff 7.8M Apr 13 16:27 target/schemata-1.0-sources.jar
-rw-r--r--  1 user  staff  20M Apr 13 16:27 target/schemata-1.0.jar
```

* Leave the Schemata directory:
```bash
$ popd
```

* Go into the
  [Data contracts Schemata quickstart directory](https://github.com/data-engineering-helpers/data-contracts/tree/main/schemata/quickstart):
```bash
$ pushd ~/dev/infra/data-contracts/schemata/quickstart
```

* Copy the just generated Schemata JAR artifact:
```bash
$ cp ~/dev/infra/schemata/target/schemata-1.0.jar target/
```

* Leave the Data contracts Schemata quickstart directory:
```bash 
$ popd
```

# Schemata utilities to validate and document the data contracts
* Go into the
  [Data contracts Schemata quickstart directory](https://github.com/data-engineering-helpers/data-contracts/tree/main/schemata/quickstart):
```bash
$ pushd ~/dev/infra/data-contracts/schemata/quickstart
```

* Generate the data contract descriptors (they are needed by the Shell scripts
  and need to be refreshed/re-generated whenever the data contracts change):
```bash
$ make all
```

* Check that the data contract descriptors have been correctly generated:
```bash
$ ls -lFh *.desc
-rw-r--r--  1 user  staff 111K Apr 13 17:01 model.desc
$ strings model.desc | head -3
activity.proto

org.examplesB&
org.protocol.schemaB
```

* Validate the model:
```bash
$ ./validate.sh
...
Schema validation success. No error to report
```

* Score the model:
```bash
$ ./score.sh org.examples.User
...

Schemata score for org.examples.User : 0.19
```

* Document the model
  + Raw output:
```bash
$ ./document.sh
```
  + Parsed with JQ:
```bash
$ ./document.sh |grep -v "^[0-9]\{2\}"|jq
[
  {
    "name": "org.examples.Category",
    "description": "This is the description of the Category table",
    ...
  }
]
```


