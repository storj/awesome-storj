<img src="https://storj.io/press-kit/Storj-symbol.svg" width="140"/>

# Awesome Storj [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome) [![Storj.io](https://storj.io/img/storj-badge.svg)](https://storj.io)

> A curated list of projects, tools, and resources for the Storj platform.

# Client Libraries

Clients prepare files for uploading using encryption and erasure encoding and upload and download files to the Storj network directly to farmers *(running Storjshare)* and store meta data on the Storj Bridge.

- [libstorj](https://github.com/Storj/libstorj) - Asynchronous multi-platform C library and CLI for encrypted file transfer on the Storj network. 
- [node-libstorj](https://github.com/Storj/node-libstorj) - Bindings to libstorj for Node.js (work-in-progress)
- [hello-storj](https://github.com/kaloyan-raev/hello-storj) Bindings to libstorj for Java and Android (example, work-in-progress)
- [SwiftyStorj](https://github.com/angu/SwiftyStorj) - Bindings to libstorj for iOS (example, work-in-progress)
- [StorjDotNet](https://github.com/ssa3512/StorjDotNet) - Bindings to libstorj for .NET (work-in-progress)
- [Storj.js](https://github.com/Storj/storj.js) - Browser library for interacting with Storj (work-in-progress)
- [Storj Python Library](https://github.com/storj/storj-python-sdk) - Python library for interacting with Storj (work-in-progress)
- [Storj-PHP](https://github.com/WebWeave/storj-php) - Implementation of the Storj protocol for PHP (work-in-progress)

# Farming

Farmers store data on the Storj network in exchange for STORJ tokens based on contracts with any Storj Bridge.

- [Storj Share GUI](https://storj.io/share.html) - Earn money by sharing your extra hard drive space on the Storj network.
- [Storj Share Daemon](https://github.com/storj/storjshare-daemon) - :imp: Daemon + CLI for farming data on the storj network.
- [Payout Formula](https://gist.github.com/pgerbes1/8c0bdfc70055786cec43b885af5b249f) | [previous](https://gist.github.com/super3/a36a3d4967951ec678200f499364b81a) - Transparent formula that is used to calculate farmer payments.
- [Storj Wallet](https://github.com/hunterlong/storj-wallet) - Storj Wallet (unofficial) for Windows, Mac and Linux. Send and Receive Storj ERC20 Token and Ethereum.
- [KFS](https://github.com/Storj/kfs) - Kademlia inspired local file store based on LevelDB.
- [Storj Collectd Plugin](https://github.com/bobey/storj-collectd-plugin) - Monitor your Storj.io nodes along with some Grafana/influxdb like solution.
- [StorjStat](https://storjstat.com/) - Community made tool for monitoring your Storj farming node(s), the tool gives you both real-time and historical analysis.
- [storjshare-config-gen](https://jukeboxrhino.github.io/storjshare-config-gen/) - Easily generate configuration files for storjshare

# Bridge

Bridges store meta data of files and hold contracts with Storj farmers. A Bridge monitors the state of the metadata and will mirror, replicate and repair files when it's necessary.

- [Storj Bridge](https://github.com/Storj/bridge) - Access the Storj network via simple REST API.
- [Storj Complex](https://github.com/Storj/complex) - Manage many renter nodes with the same identity with remote control capabilities.
- [Storj Billing](https://github.com/Storj/billing) - Creates debits and credits for Storj Bridge users.
- [Storj Models](https://github.com/Storj/service-storage-models) - Database models for Storj Bridge
- [Storj Bridge GUI](https://github.com/Storj/bridge-gui) - Web application for managing your Storj Bridge account.

# Network

Description and implementation for the Storj protocol that all nodes and participants in the Storj network use to communicate.

- [SIPS](https://github.com/Storj/sips) - Storj Improvement Proposals.
- [Storj Core](https://github.com/Storj/core) - Implementation of the Storj protocol for Node.
- [Storj Node Map](http://storjmap.overnetcity.com/) - Uses Bridge API to display online nodes on a map. [[Github]](https://github.com/bobey/StorjMap)

# Client Applications & Tools
- [Storj CLI (C)](https://github.com/Storj/libstorj) - Newest and recommended CLI tool for Storj.  
- [Storj CLI (Javascript)](https://github.com/Storj/core-cli) - Deprecated CLI tool for Storj *(supports multifile uploads)*.
- [Heroku Add-on](https://elements.heroku.com/addons/storj) - Storj in your favorite cloud platform.
- [Storj@stdlib](https://github.com/storj/stdlib.com) - Deploy a serverless datastore on the stdlib network backed by Storj.
- [storj.pics](http://storj.pics) - Upload and share pictures using Storj 100% in browser. [[Example]](http://storj.pics/#/public/3c894b5bc1b2b8c8a69915c7/files/867cd8678ce8363eb6a38a28) [[Github]](https://github.com/nginnever/storj.pics)
- [storjrb-backupcore](https://bitbucket.org/DaveahamLincoln/storjrb-backupcore) - A generic Ruby script that facilitates the automation of multiple Storj backups.
- [storj-gui-client](https://github.com/lakewik/storj-gui-client) - GUI Client for Storj Network written in Python and PyQt4.

# Tutorials & Examples
- [Quickstart](https://docs.storj.io/) - Steps thought creating an acccount, and using CLI tools.
- [Tutorials](https://storj.github.io/core/) - Full documentation for Storj Core, with many example scripts.
- [Storj Node Heroku Example in Node.js](https://github.com/Storj/storj-node-heroku-example) - Authenticate, create key pairs, create buckets, and upload and download a file.
- [Working with the Storj API](https://docs.google.com/document/d/1ehsSHtwnwC-LSgygxYGFuWoCx1DuhA2-XbDw64nggNY/edit?usp=sharing) - Order of method calls for uploading and downloading with the Storj API.
- [FAQ](https://storj.io/faq.html) - Frequently Asked Questions.

# Whitepapers
- [Storj Whitepaper v2](https://storj.io/storj.pdf) - Published December 15, 2016.
- [Storj Whitepaper v1](https://storj.io/storj2014.pdf) - Published December 15, 2014.

# Community
- [Community Chat](https://community.storj.io/) - Open community chat. Our most active discussion area.
- [Community Page](https://storj.io/community.html) - Links to newsletter, chat, social media, and events.  

# Contribute to Storj
- [Storj on Github](https://github.com/storj) - All Storj repositories in one place.
- [Give Feedback](https://wantoo.io/storj-product-feedback/) - Suggest new product ideas or upvoting existing ones.
- [Write Guides](https://storj.io/get-paid-to-write.html) - Get paid to write guides and tutorials about our platform.
- [Submit Code](https://storj.io/developers.html) - Submit pull requests on our public repositories on GitHub.

# Support
- [Chat Support](https://community.storj.io/) - Recommend using our community chat for realtime support in many languages.
- [Issue Support](https://docs.storj.io/discuss) - If you any troubles or questions, please contact Storj support.
