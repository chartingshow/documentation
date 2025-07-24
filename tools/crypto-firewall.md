<p align="center"><img src="https://github.com/chartingshow/crypto-firewall/blob/master/assets/images/firewall-icon.png" width="128" height="128"/></p>

<h1 align="center">📈 Charting Show: Crypto Firewall ✅</h1>

Crypto Firewall: Your Digital Shield in the Cryptocurrency Ecosystem

This security-centric repository offers a comprehensive suite of resources and tools designed to fortify your cryptocurrency trading activities and systems. We provide:

- Cutting-edge best practices
- Robust scripts and configurations
- In-depth security guides

Our primary focus is on:

1. Blocking browser-based crypto mining and cryptojacking attempts
2. Thwarting banking and crypto malware
3. Identifying and preventing access to phishing websites and malicious apps
4. Disrupting hackers' command-and-control (C2) server communications

**Disclaimer:** New websites are being created all the time to steal cryptocurrencies from users, this is a cat and mouse game and these filter lists are not intended to be a complete solution! User discretion is advised, care and diligence of cyber security to avoid scams are recommended.

## Installation ❤️

Choose whether to install the crypto firewall at the browser and/or operating system level.

### Browser Blocking 🌟

Install an ad blocker in your desktop or mobile browser that uses the [Adblock Plus](https://adblockplus.org/)' filter list:

#### Recommended Choice ⭐

Brave Browser offers built-in ad and tracker blocking, making it an excellent choice for enhanced privacy and security.

- ![Brave Desktop Browser](https://github.com/chartingshow/crypto-firewall/blob/master/assets/images/brave.png) **[Brave Desktop Browser Instructions Guide](https://github.com/chartingshow/crypto-firewall/blob/master/docs/help-guides/brave-desktop-browser-instructions.md)** - Provides robust privacy features, including a built-in ad blocker and Tor integration for anonymous browsing.

- ![Brave Desktop Browser](https://github.com/chartingshow/crypto-firewall/blob/master/assets/images/brave.png) **[Brave Mobile Browser Instructions Guide](https://github.com/chartingshow/crypto-firewall/blob/master/docs/help-guides/brave-mobile-browser-instructions.md)** - Offers similar privacy protections on mobile devices.

#### Other Browser Choices ✨

Explore additional secure browsers like [Firefox](https://www.mozilla.org/en-US/firefox/new/), [Opera](https://www.opera.com/) and [Carbon Browser](https://carbon.website/), each offering unique features such as ad-blocking, privacy enhancements and cryptocurrency support.

- ![AdBlock](https://github.com/chartingshow/crypto-firewall/blob/master/assets/images/adblock.png) **AdBlock** - Active by default, blocks ads and trackers.

- ![AdBlock Plus](https://github.com/chartingshow/crypto-firewall/blob/master/assets/images/adblock-plus.png) **Adblock Plus** - Popular ad-blocking extension for various browsers.

- ![uBock Origin](https://github.com/chartingshow/crypto-firewall/blob/master/assets/images/ublock.png) **[uBlock Origin (Manifest V2) Instructions Guide](https://github.com/chartingshow/crypto-firewall/blob/master/docs/help-guides/ublock-origin-instructions.md)** - Efficient, wide-spectrum content blocker.

- ![uBock Origin](https://github.com/chartingshow/crypto-firewall/blob/master/assets/images/ublock.png) **[uBlock Origin Lite (Manifest V3) Instructions Guide](https://github.com/chartingshow/crypto-firewall/blob/master/docs/help-guides/ublock-origin-lite-instructions.md)** - Is a _permission-less_ MV3-based content blocker.

- ![AdGuard Browser Extension](https://github.com/chartingshow/crypto-firewall/blob/master/assets/images/adguard.png) **AdGuard Browser Extension** - Comprehensive ad and tracker blocking solution.

- ![AdBlock Browser](https://github.com/chartingshow/crypto-firewall/blob/master/assets/images/adblock-browser.png) **Adblock Browser** - Available for Android and iOS devices with built-in ad blocking.

- ![Opera Browser](https://github.com/chartingshow/crypto-firewall/blob/master/assets/images/opera.png) **Opera Browser** - Includes ad blocking by default since Opera 50.

- <img src="https://github.com/chartingshow/crypto-firewall/blob/master/assets/images/chrome.png" alt="crypto" width="16" height="16" /> **Chrome Browser** - Includes [Manifest V3](https://developer.chrome.com/docs/extensions/develop/migrate/what-is-mv3) by default limiting adblocker rules to only 30,000. Is the most popular browser used on the internet.

### Operating System Blocking 🌟

For system-wide protection, consider modifying your device's hosts file:

<ul>
    <li><p><img src="https://github.com/chartingshow/crypto-firewall/blob/master/assets/images/linux.png" alt="Linux" width="16" height="16" /> <a href="https://github.com/chartingshow/crypto-firewall/blob/master/docs/help-guides/linux-hosts-instructions.md"><strong>Linux Hosts File Instructions Guide</strong></a> - Edit the hosts file to block unwanted domains at the system level.</p></li>
    <li><p><img src="https://github.com/chartingshow/crypto-firewall/blob/master/assets/images/mac-os.png" alt="MacOS" width="16" height="16" /> <a href="https://github.com/chartingshow/crypto-firewall/blob/master/docs/help-guides/mac-hosts-instructions.md"><strong>MacOS Hosts File Instructions Guide</strong></a> - Modify the hosts file to prevent access to specific websites and services.</p></li>
    <li><p><img src="https://github.com/chartingshow/crypto-firewall/blob/master/assets/images/microsoft.png" alt="Windows" width="16" height="16" /> <a href="https://github.com/chartingshow/crypto-firewall/blob/master/docs/help-guides/windows-hosts-instructions.md"><strong>Windows Hosts File Instructions Guide</strong></a> - Update the hosts file to block connections to undesired IP addresses.</p></li>
</ul>

### Perimeter blocking 🔓

You may use the hosts file with below applications to block these miners on whole networks. Simply add the link to the above hosts file in each system.

- ![pfSense](https://github.com/chartingshow/crypto-firewall/blob/master/assets/images/pfSense.png) **[pfSense with pfBlockerNG Instructions Guide](https://github.com/chartingshow/crypto-firewall/blob/master/docs/help-guides/pfsense-pfblockerng-instructions.md)** - Provides firewall capabilities by allowing users to filter both inbound and outbound traffic using IP and DNS blocklists.
- ![Pi-hole](https://github.com/chartingshow/crypto-firewall/blob/master/assets/images/pi-hole.png) **[Pi-hole Instructions Guide](https://github.com/chartingshow/crypto-firewall/blob/master/docs/help-guides/pi-hole-instructions.md)** - Provides a Linux network-level advertisement and Internet tracker blocking application which acts as a DNS sinkhole and optionally a DHCP server, intended for use on a private network.

## Basic usage 🔥

For a thorough explanation on how to add the to your adblocker, open one of the help guides found in this folder:

- https://github.com/chartingshow/crypto-firewall/tree/master/docs

## Recommended versions ✅

The firewall is known to reduce performance slightly and this is why we have several **different** versions.

Here's a suggested guide based on cpu processors:

- **Intel i3** - use `full` version (if you experience bad performance then try `lite` version instead).
- **Intel i5** - use `full` version (if you experience bad performance then try `lite` version instead).
- **Intel i7** - use `mega` version (if you experience bad performance then try `full` version instead).
- **Intel i9** - use `beta` or `mega` versions (if you experience bad performance then try `full` version instead).

- **AMD Ryzen 3** - use `lite` version (if you experience bad performance then try `full` version instead).
- **AMD Ryzen 5** - use `full` version (if you experience bad performance then try `lite` version instead).
- **AMD Ryzen 7** - use `mega` version (if you experience bad performance then try `full` version instead).
- **AMD Ryzen 9** - use `beta` or `mega` versions (if you experience bad performance then try `full` version instead).

Here's a suggested guide based on device:

- **Laptop** or **Computer** - use `beta` or `mega` versions (if you experience bad performance then try `full` version instead).
- **Tablet** - use `mega` or `full` versions (if you experience bad performance then try `full` version instead).
- **Powerful Smartphone** - use `full` version (if you experience bad performance then try `lite` version instead).
- **Low-End Smartphone** - use `lite` version.

## Issues and Suggestions

If you discover a false positive or need to add a new block, then feel free to raise an [Issue](https://github.com/chartingshow/crypto-firewall/issues/new/choose) or a [Pull request](https://github.com/chartingshow/crypto-firewall/pulls) to **add/remove** them to the lists.

**Disclaimer:** New websites are being created all the time to steal cryptocurrencies from users, this is a cat and mouse game and these filter lists are not intended to be a complete solution! User discretion is advised, care and diligence of cyber security to avoid scams are recommended.
