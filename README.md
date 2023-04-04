Data contracts
==============

# Table of Contents
* [Overview](#overview)
* [Definitions](#definitions)
  * [Definition by David Jayatillake](#definition-by-david-jayatillake)
  * [Definition by Andrew James](#definition-by-andrew-james)
* [References](#references)
  * [Web sites, blogs](#web-sites-blogs)
    * [Data contracts for the warehouse on Substack](#data-contracts-for-the-warehouse-on-substack)
    * [Data products, Chad Sanderson on Substack](#data-products-chad-sanderson-on-substack)
  * [Collection of articles](#collection-of-articles)
    * [Awesome data contracts](#awesome-data-contracts)
  * [Articles](#articles)
    * [Data contracts, the missing foundation](#data-contracts-the-missing-foundation)
    * [Data contracts for the warehouse](#data-contracts-for-the-warehouse)
    * [Data contracts wrapped 2022](#data-contracts-wrapped-2022)
    * [Data contracts in practice](#data-contracts-in-practice)
    * [An Engineer's guide to Data Contracts](#an-engineers-guide-to-data-contracts)
    * [The production\-grade Data Pipeline](#the-production-grade-data-pipeline)
    * [Yet another post on Data Contracts](#yet-another-post-on-data-contracts)
    * [Fine, let us talk about data contracts](#fine-let-us-talk-about-data-contracts)
    * [Data contracts \- From zero to hero](#data-contracts---from-zero-to-hero)
    * [Contracts have consequences](#contracts-have-consequences)
    * [Data Person: Attorney At Law](#data-person-attorney-at-law)
    * [The rise of data contracts](#the-rise-of-data-contracts)
    * [Interfaces and breaking stuff](#interfaces-and-breaking-stuff)
    * [Implementing Data Contracts: 7 Key Learnings](#implementing-data-contracts-7-key-learnings)
    * [Shifting left on governance: DataHub and schema annotations](#shifting-left-on-governance-datahub-and-schema-annotations)
    * [Data contracts at GoCardless, 6 months on](#data-contracts-at-gocardless-6-months-on)
    * [Improving data quality with data contracts](#improving-data-quality-with-data-contracts)
* [Tools and frameworks](#tools-and-frameworks)
  * [Schemata](#schemata)
  * [OpenDataMesh](#opendatamesh)
  * [API specifications](#api-specifications)
* [Specifications](#specifications)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

# Overview
[This project](https://github.com/data-engineering-helpers/data-contracts)
intends to document requirements and referential material to implement
data contracts in the perspective of data engineering on a
modern data stack (MDS).

Data contracts are essential to decouple data producers from data consumers,
while having both parties taking responsibility for their respective parts.

Even though the members of the GitHub organization may be employed by
some companies, they speak on their personal behalf and do not represent
these companies.

# Definitions

## Definition by David Jayatillake
* Source: https://davidsj.substack.com/p/yet-another-post-on-data-contracts

In short, **a Data Contract is an enforceable agreement on structure
and format between the producer and consumer of data**.
You could even define it in a simpler way:
**a Data Contract is a guarantee on structure and format by a producer of data**.

## Definition by Andrew James
* Source: https://andrew-jones.com/blog/data-contracts/

Almost all data platforms start with a
[change data capture (CDC) service](https://en.wikipedia.org/wiki/Change_data_capture)
to extract data from an organisations transactional databases - the source of truth
for their most valuable data. That data is then transformed, joined,
and aggregated to drive analysis, modelling, and other downstream services.

However, this data has not been designed for these use cases - it has been designed
to satisfy the needs and requirements of the source applications and their day-to-day use.
It can then take significant effort to transform, deduce, and derive the data
in order to make it useful for downstream use cases.

Furthermore, breaking changes and data migrations will be a regular part of
the applications evolution and will be done without knowledge of how it has been
used downstream, leading to breaking changes affecting key reports and data-driven products.

For downstream users to confidently build on this valuable data, they need to know
the data they are using is accurate, complete, and future proof.
This is the _data contract_.

# References
* [Architecture principles for data engineering pipelines on the Modern Data Stack (MDS)](https://github.com/data-engineering-helpers/architecture-principles)
* Specifications/principles for a
  [data engineering pipeline deployment tool](https://github.com/data-engineering-helpers/data-pipeline-deployment)

## Web sites, blogs

### Data contracts for the warehouse on Substack
* Link to the web site/blog: https://dataproducts.substack.com/p/data-contracts-for-the-warehouse

### Data products, Chad Sanderson on Substack
* Link to Chad Sanderson's profile: https://substack.com/profile/12566999-chad-sanderson
* Link to the newsletter subscription form: https://dataproducts.substack.com/

## Collection of articles

### Awesome data contracts
* Link to the reference documentation on GitHub: https://github.com/AltimateAI/awesome-data-contracts

## Articles

### Data contracts, the missing foundation
* Title: Data contracts: The missing foundation
* Date: March 2023
* Author: Tom Baeyens
* Link to the article: https://medium.com/@tombaeyens/data-contracts-the-missing-foundation-3c7a98544d2a
* Publisher: Medium

### Data contracts for the warehouse
* Title: Data contracts for the warehouse
* Date: January 2023
* Authors: Chad Sanderson and Daniel Dicker
* Link to the web site/blog: https://dataproducts.substack.com/p/data-contracts-for-the-warehouse
* Publisher: Substack

### Data contracts wrapped 2022
* Title: Data contracts wrapped - 2022
* Date: December 2022
* Author: Shirshanka Das ([Shirshanka Das on LinkedIn](https://www.linkedin.com/in/shirshankadas/))
* Link to the article: https://medium.com/datahub-project/data-contracts-wrapped-2022-470e0c43365d
* Publisher: Medium

### Data contracts in practice
* Title: Data contracts in practice
* Date: December 2022
* Author: Andrea Gioia ([Andrea Gioia on LinkedIn](https://www.linkedin.com/in/andreagioia/))
* Link to the article: https://betterprogramming.pub/data-contracts-in-practice-93e58d324f34
* Publihser: Medium

### An Engineer's guide to Data Contracts
* Title: An Engineer's guide to Data Contracts
* Date: October 2022
* Authors: Chad Sanderson and Adrian Kreuziger
* Part 1: https://dataproducts.substack.com/p/an-engineers-guide-to-data-contracts
* Part 2: https://dataproducts.substack.com/p/an-engineers-guide-to-data-contracts-6df
* Publisher: Substack

### The production-grade Data Pipeline
* Title: The production-grade Data Pipeline
* Date: September 2022
* Author: Chad Sanderson
* Link to the article: https://dataproducts.substack.com/p/the-production-grade-data-pipeline
* Publisher: Substack

### Yet another post on Data Contracts
* Title: Yet another post on Data Contracts
* Date: September 2022
* Author: David Jayatillake ([David Jayatillake on Substack](https://substack.com/profile/64081583-david-jayatillake),
  [David Jayatillake on LinkedIn](https://www.linkedin.com/in/david-jayatillake/))
* Part 1: https://davidsj.substack.com/p/yet-another-post-on-data-contracts
* Part 2: https://davidsj.substack.com/p/yet-another-post-on-data-contracts-9f0
* Part 3: https://davidsj.substack.com/p/yet-another-post-on-data-contracts-dad
* Publisher: Substack

### Fine, let us talk about data contracts
* Title: Fine, let's talk about data contracts
* Date: September 2022
* Author: Benn Stancil ([Benn Stancil on Substack](https://benn.substack.com/about), [Benn Stancil on LinkedIn](https://www.linkedin.com/in/benn-stancil/))
* Link to the article: https://benn.substack.com/p/data-contracts
* Publisher: Substack

### Data contracts - From zero to hero
* Title: Data contracts - From zero to hero
* Date: September 2022
* Author: Mehdi Ouazza ([Mehdi Ouazza on LinkedIn](https://www.linkedin.com/in/mehd-io/))
* Link to the article: https://towardsdatascience.com/data-contracts-from-zero-to-hero-343717ac4d5e
* Publisher: Medium

### Contracts have consequences
* Title: Contracts have consequences
* Date: September 2022
* Author: Tristan Hardy ([Tristan Hardy on Substack](https://substack.com/profile/1135298-tristan-handy))
* Link to the article: https://roundup.getdbt.com/p/contracts-have-consequences
* Publisher: Substack

### Data Person: Attorney At Law
* Title: Data Person: Attorney At Law
* Date: September 2022
* Author: Stephen Bailey ([Stephen Bailey on Substack](https://substack.com/profile/16953086-stephen-bailey), [Stephen Bailey on LinkedIn](https://www.linkedin.com/in/stkbailey/))
* Link to the article: https://stkbailey.substack.com/p/data-person-attorney-at-law
* Publisher: Substack

### The rise of data contracts
* Title: The rise of data contracts
* Date: August 2022
* Author: Chad Sanderson
* Link to the article: https://dataproducts.substack.com/p/the-rise-of-data-contracts
* Publisher: Substack

### Interfaces and breaking stuff
* Title: Interfaces and breaking stuff
* Date: July 2022
* Author: Tristan Handy ([Tristan Handy on Substack](https://substack.com/profile/1135298-tristan-handy), [Tristan Handy on LinkedIn](https://www.linkedin.com/in/tristanhandy/))
* Link to the article: https://roundup.getdbt.com/p/interfaces-and-breaking-stuff
* Publisher: Substack

### Implementing Data Contracts: 7 Key Learnings
* Title: Implementing Data Contracts: 7 Key Learnings
* Date: July 2022
* Author: Barr Moses, CEO at Monte Carlo
* Link to the article: https://barrmoses.medium.com/implementing-data-contracts-7-key-learnings-d214a5947d5e
* Publisher: Medium

### Shifting left on governance: DataHub and schema annotations
* Title: Shifting left on governance: DataHub and schema annotations
* Date: May 2022
* Author: Joshua Shinavier
* Link to the article: https://engineering.linkedin.com/blog/2022/shifting-left-on-governance--datahub-and-schema-annotations
* Publisher: LinkedIn

### Data contracts at GoCardless, 6 months on
* Title: Data contracts at GoCardless, 6 months on
* Date: May 2022
* Author: Andrew Jones
* Link to the article: https://medium.com/gocardless-tech/data-contracts-at-gocardless-6-months-on-bbf24a37206e
* Publisher: Medium

### Improving data quality with data contracts
* Title: Improving data quality with data contracts
* Date: December 2021
* Author: Andrew Jones ([Andrew Jones on LinkedIn](https://www.linkedin.com/in/andrewrhysjones))
* Link to the article: https://medium.com/gocardless-tech/improving-data-quality-with-data-contracts-238041e35698
* Publisher: Medium

# Tools and frameworks

## Schemata
* Homepage: [GitHub - Schemata](https://github.com/ananthdurai/schemata)
* Underlying technology: Protobuf

## OpenDataMesh
* Title: Data Product Descriptor Specification
* Homepage: https://dpds.opendatamesh.org
* An open specification that declaratively defines a data product in all its components
  using a JSON or YAML descriptor document. It is released under Apache 2.0 license.

## Avro / Schema Registry
* [Schema Registry overview](https://docs.confluent.io/platform/current/schema-registry/index.html)
* [Avro overview](https://avro.apache.org/docs/)

### Support by cloud vendors
* [AWS Glue Schema Registry](https://docs.aws.amazon.com/glue/latest/dg/schema-registry.html)

## Protocol buffers (Protobuf)
* [Protobuf homepage](https://protobuf.dev/)

## API specifications
* [OpenAPI](https://www.openapis.org/)
* [AsyncAPI spec](https://www.asyncapi.com/docs/reference/specification/v2.6.0)
* [DatastoreAPI](https://dpds.opendatamesh.org/resources/standards/dsapi-spec/)

# Specifications
* Data contract as code (DCaC) principle: the data contracts must be specified thanks
  to an [Interface Definition Language (IDL)](https://en.wikipedia.org/wiki/Interface_description_language),
  for instance [Smithy](https://smithy.io/) or [Protobuf](https://protobuf.dev/)
* Shift-left principle: as much as meta-data as possible should be written directly
  within the IDL-based data contracts, potentially through annotations and/or
  naming conventions as comments
* The idea behind the two above-mentioned principles is to have the IDL-based specifications
  materializing the
  [single version of the truth (SVOT)](https://en.wikipedia.org/wiki/Single_version_of_the_truth)
  for the data sets, while benefitting from the whole automation and tooling that an open standard
  such as Smithy and Protobuf bring

