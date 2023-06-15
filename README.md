<img src="https://assets.website-files.com/602eda09fc78afc76e9706b6/60917840ebdae99bf420b0a3_dcs.svg" width="140"/>

# Awesome Storj [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

> A curated list of projects, tools, and resources for the Storj platform. 

Note: this list contains only projects which are compatible with the current (v3) version of Storj network. Earlier projects and integrations were removed.

# Core links

- **[Start here](https://www.storj.io/) - Register on satellites operated by Storj Labs**
- [Documentation](https://docs.storj.io/dcs/) - Entrypoint to the official documentation
- [Community support / forum](forum.storj.io/) - Community and support forum
- [Storj Status](https://status.storj.io/) - Status of the Storj network
- [Usage statistic dashboard](https://storjstats.info/) - Statistics about the full Storj network ([raw data](https://stats.storjshare.io/))
- [Roadmap](https://github.com/storj/roadmap/) - Official roadmap of Storj development
- [Whitepaper v3](https://storj.io/storj.pdf) - Actual version of Storj white-paper 
- [FAQ](https://docs.storj.io/dcs/support/faqs) - Frequently Asked questions and answers 
- [Storj on Twitter](https://twitter.com/storj/) - Official twitter channel of Storj Labs
- [Storj on Youtube](https://www.youtube.com/c/StorjLabs) - Official Youtube channel of Storj

## Clients with Storj support and integrations 

* **[uplink](https://github.com/storj/storj/releases) - Uplink is the official CLI for Storj. Can be downloaded from the release page** 
* [Storj Mobile](https://play.google.com/store/apps/details?id=com.storj_mobile) (beta) - Android application to access Storj ([forum post](https://forum.storj.io/t/storj-mobile-beta-for-android/15578))
* [rclone](https://rclone.org/tardigrade/) - Tool to sync your files to cloud storage including Storj 
* [restic]() - Restic is a modern backup program. Supports Storj via the rclone . [howto](https://docs.storj.io/dcs/how-tos/backup-with-restic), [docs](https://restic.readthedocs.io/en/stable/030_preparing_a_new_repo.html#other-services-via-rclone)
* [Storj Photo Gallery Uploader (Early Access)](https://play.google.com/store/apps/details?id=io.storj.photogalleryuploader) - Upload you photos to Storj DCS and show them within a nice gallery
* [FileZilla](https://docs.storj.io/dcs/how-tos/set-up-filezilla-for-decentralized-file-transfer) - New protocol for Storj is being added to FileZilla. 
* [NextCloud](https://apps.nextcloud.com/apps/storj) - Adds Storj external storage to NextCloud 
* [Duplicati](https://www.duplicati.com/) - Free backup software to store encrypted backups online ([howto](https://docs.storj.io/dcs/how-tos/backup-with-duplicati))
* [transfer.sh](https://github.com/dutchcoders/transfer.sh) - Easy and fast file sharing from the command-line.
* [Storj Cloud UI](https://github.com/FazioNico/storj-cloud-ui) - Cross platform UI application that allows users to upload, download and manage files from the @storj network
* [Terraform provider](http://github.com/mjpitz/terraform-provider-storj) - Terraform provider for Storj
* [quickshare](https://github.com/TopperDEL/Quickshare) - dotnet tool to quickly upload files to Storj from Windows, Linux and Mac

# Client Libraries & language bindings

Storj can be used via the native interface (uplink CLI and uplink libraries) or as an S3 compatible backend with any S3 compatible tool. The following list focuses on the native protocol.

- [uplink](https://github.com/storj/uplink) - Go library to use Storj (documentation)[https://pkg.go.dev/storj.io/uplink]
- [uplink-c](https://github.com/storj/uplink-c) - C library of the Uplink

* [uplink-python](https://github.com/storj-thirdparty/uplink-python) - Python bindings for libuplink
* [uplink-php](https://github.com/storj-thirdparty/uplink-php/pull/20#pullrequestreview-818737763) - PHP binding for libuplink
* [uplink-ruby](https://forum.storj.io/t/uplink-for-ruby) - Ruby gem ([forum post](https://forum.storj.io/t/uplink-for-ruby/22929?u=bre))
* [uplink-rust](https://github.com/storj-thirdparty/uplink-rust) - Storj Uplink Rust bindings for the Rust programming language.
* [TopperDEL/uplink.net](https://github.com/TopperDEL/uplink.net)  A .Net-wrapper to connect to the storj v3 network.

# Storage node operation (SNO/Farming)

Farmers store data on the Storj network in exchange for STORJ tokens based on contracts with any Storj Bridge.

- [Getting started with hosting Storagenode](https://www.storj.io/host-a-node/)
- [SNO Payment FAQ](https://forum.storj.io/t/sno-payment-mega-faq/16228) - Huge list of questions answered on the forum
- [Node FAQ](https://docs.storj.io/node/resources/faq) - FAQ about operating Storage Nodes
- [Grafana dashboard](https://gist.github.com/littleskunk/b16567743626d9dd33454463a2e8a5d4) - Grafana dashboard for the native Prometheus endpoint of storagenodes ([forum post](https://forum.storj.io/t/tech-preview-email-alerts-with-grafana-and-prometheus/16156/8))
- [Grafana dashboard](https://github.com/anclrii/Storj-Exporter-dashboard) for external [Prometheus exporter](https://github.com/anclrii/Storj-Exporter)
- [Earnings calculator](https://github.com/ReneSmeekes/storj_earnings) - Python script prints out estimated earnings based on local data of Storagenode ([forum post](https://forum.storj.io/t/earnings-calculator-update-2022-01-13-v11-0-0-detailed-earnings-info-and-health-status-of-your-node-including-vetting-progress/1794/432))
- [Storj deployment](https://github.com/tomaae/storj-deployment) - Ready to use docker definitions (including Grafana, prometheus exporters, etc...)

## Services based on / with support of Storj 

* [Fastly](https://fastly.com) - Content delivery network with Storj support ([docs](https://docs.fastly.com/en/guides/storj-dcs-object-storage))
* [Opensea](https://opensea.io/) -- NFT marketplace. Supports hosting NFT resources on Storj ([howto](https://docs.storj.io/dcs/how-tos/nft-storage))
* [Pixelexperience](https://download.pixelexperience.org/) - Android ROMS are [distributed with the help of Storj](https://www.storj.io/blog/pixelexperience-scales-up-software-distribution-with-storj-dcs)
* [media.network](https://docs.media.network/storj-about/) - Media Network is a privacy-first and community-governed CDN.

## Tokeneconomics

STORJ is an ERC-20 utility token for the Storj network.

* [STORJ on Coinmarketcap](https://coinmarketcap.com/currencies/storj/)
* [Latest STORJ Token Balance & Flows Report](https://www.storj.io/category/token-report)
* [Coingecko, Storj markets](https://www.coingecko.com/en/coins/storj#markets) - Exchanges support STORJ token
* Storj Node operator payouts, supported chains:
  * Ethereum: STORJ ERC-20 token (default)
  * [ZkSync](https://storj-labs.gitbook.io/node/dependencies/storage-node-operator-payout-information/zk-sync-opt-in-for-snos)

# Contribution

- [Contribution guideline](https://github.com/storj/storj/blob/main/CONTRIBUTING.md) - How to contribute to Storj
- [Give Feedback](https://forum.storj.io/c/ideas-and-suggestions/5) - Suggest new product ideas in the community forum
- [Ideas and suggestions](https://forum.storj.io/c/ideas-and-suggestions/5) on Storj forum
- [Storj illustrated](https://github.com/storj/illustrated) - diagrams to explain internals of Storj architecture
- [storj-up](https://github.com/storj/up) - docker-compose based helper utility to startup full network (satellite + storage nodes) locally
- [Storj on Github](https://github.com/storj) - All Storj repositories in one place.

## Tools, utilities, experiments

- [Ansible role to install and configure single-tenant S3 gateway](https://gitlab.phowork.fr/phowork/iac/ansible/roles/storj-gateway-st)
- [Tool to directly read files from uploaded ZIP files](https://github.com/storj/zipper)
- [Using Storj as IPFS backend](https://github.com/kaloyan-raev/ipfs-go-ds-storj)
