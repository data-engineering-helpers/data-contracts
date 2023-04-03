Data contracts
==============

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

### Data contracts in practice
* Title: Data contracts in practice
* Date: December 2022
* Author: Andrea Gioia ([Andrea Gioia on LinkedIn](https://www.linkedin.com/in/andreagioia/))
* Link to the article: https://betterprogramming.pub/data-contracts-in-practice-93e58d324f34
* Publihser: Medium

### Fine, let us talk about data contracts
* Title: Fine, let's talk about data contracts
* Date: September 2022
* Author: Benn Stancil ([Benn Stancil on Substack](https://benn.substack.com/about), [Benn Stancil on LinkedIn](https://www.linkedin.com/in/benn-stancil/))
* Link to the article: https://benn.substack.com/p/data-contracts
* Publisher: Substack

### Interfaces and breaking stuff
* Title: Interfaces and breaking stuff
* Date: July 2022
* Author: Tristan Handy ([Tristan Handy on Substack](https://substack.com/profile/1135298-tristan-handy), [Tristan Handy on LinkedIn](https://www.linkedin.com/in/tristanhandy/))
* Link to the article: https://roundup.getdbt.com/p/interfaces-and-breaking-stuff
* Publisher: Substack

### Shifting left on governance: DataHub and schema annotations
* Title: Shifting left on governance: DataHub and schema annotations
* Date: May 2022
* Author: Joshua Shinavier
* Link to the article: https://engineering.linkedin.com/blog/2022/shifting-left-on-governance--datahub-and-schema-annotations
* Publisher: LinkedIn

### Implementing Data Contracts: 7 Key Learnings
* Title: Implementing Data Contracts: 7 Key Learnings
* Date: July 2022
* Author: Barr Moses, CEO at Monte Carlo
* Link to the article: https://barrmoses.medium.com/implementing-data-contracts-7-key-learnings-d214a5947d5e
* Publisher: Medium

### Yet another post on Data Contracts
* Title: Yet another post on Data Contracts
* Date: September 2022
* Author: David Jayatillake ([David Jayatillake on Substack](https://substack.com/profile/64081583-david-jayatillake),
  [David Jayatillake on LinkedIn](https://www.linkedin.com/in/david-jayatillake/))
* Part 1: https://davidsj.substack.com/p/yet-another-post-on-data-contracts
* Part 2: https://davidsj.substack.com/p/yet-another-post-on-data-contracts-9f0
* Part 3: https://davidsj.substack.com/p/yet-another-post-on-data-contracts-dad
* Publisher: Substack

### An Engineer's guide to Data Contracts
* Title: An Engineer's guide to Data Contracts
* Date: October 2022
* Authors: Chad Sanderson and Adrian Kreuziger
* Part 1: https://dataproducts.substack.com/p/an-engineers-guide-to-data-contracts
* Part 2: https://dataproducts.substack.com/p/an-engineers-guide-to-data-contracts-6df
* Publisher: Substack

### Data contracts for the warehouse
* Title: Data contracts for the warehouse
* Date: January 2023
* Authors: Chad Sanderson and Daniel Dicker
* Link to the web site/blog: https://dataproducts.substack.com/p/data-contracts-for-the-warehouse
* Publisher: Substack

### The production-grade Data Pipeline
* Title: The production-grade Data Pipeline
* Date: September 2022
* Author: Chad Sanderson
* Link to the article: https://dataproducts.substack.com/p/the-production-grade-data-pipeline
* Publisher: Substack

### The rise of data contracts
* Title: The rise of data contracts
* Date: August 2022
* Author: Chad Sanderson
* Link to the article: https://dataproducts.substack.com/p/the-rise-of-data-contracts
* Publisher: Substack

### Improving data quality with data contracts
* Title: Improving data quality with data contracts
* Date: December 2021
* Author: Andrew Jones ([Andrew Jones on LinkedIn](https://www.linkedin.com/in/andrewrhysjones))
* Link to the article: https://medium.com/gocardless-tech/improving-data-quality-with-data-contracts-238041e35698
* Publisher: Medium

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

