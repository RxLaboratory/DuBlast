# DuBlast - Duduf Playblast

Quick Playblast tool for Blender

[![Blender](https://img.shields.io/badge/Blender-Win%20|%20Mac%20|%20Linux-informational?color=lightgrey&logo=blender)](#) [![GitHub](https://img.shields.io/github/license/RxLaboratory/DuBlast?color=lightgrey)](LICENSE.md)

<!-- status -->
**Status:**  
[![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/RxLaboratory/DuBlast?color=brightgreen)](https://github.com/RxLaboratory/DuBlast/releases) [![GitHub Release Date](https://img.shields.io/github/release-date/RxLaboratory/DuBlast)](https://github.com/RxLaboratory/DuBlast/releases) [![GitHub tag (latest SemVer pre-release)](https://img.shields.io/github/v/tag/RxLaboratory/DuBlast?include_prereleases&label=testing)](https://github.com/RxLaboratory/DuBlast/tags)
<!-- end:status -->

## What's this?

*DuBlast* is an add-on for *Blender* which makes it easy to create and play animation playblasts, without having to change any render or output setting.

📖 A **comprehensive user documentation** is [available here](http://dublast.rxlab.guide/).

[![Website](https://img.shields.io/badge/website-RxLab-informational)](https://rxlaboratory.org/tools/dublast-for-blender/) [![Doc](https://img.shields.io/badge/documentation-dublast.rxlab.guide-informational)](http://dublast.rxlab.guide)

🎥 You can **download the latest public version [here](https://rxlaboratory.org/tools/dublast-for-blender/)**.

📣 You can also **help the developper** (Nicolas "Duduf" Dufresne) **and access Beta versions** on [Patreon](https://patreon.com/duduf), or you can [make a donation to RxLaboratory](https://donate.rxlab.info) to help the maintenance and distribution of all our free tools.

<!-- join -->
## Join the community

Join us if you need any help, if you want to contribute (we're always in need for translations, writing the doc, fixing bugs, making tutorials, developing new features...) or just want to show what you're doing with our tools!

We need your support to release our free tools. You can [donate](donate.rxlab.info) or [join the development fund to get an early access to the tools](https://rxlaboratory.org/early-access/).

**Funding:**  
[![Donate Now!](https://img.shields.io/badge/donate%20now!-donate.rxlab.info-blue?logo=heart)](http://donate.rxlab.info) [![Income](https://img.shields.io/endpoint?url=https%3A%2F%2Fversion.rxlab.io%2Fshields%2F%3FmonthlyIncome)](http://donate.rxlab.info) [![Sponsors](https://img.shields.io/endpoint?url=https%3A%2F%2Fversion.rxlab.io%2Fshields%2F%3FnumBackers)](http://donate.rxlab.info)  

**Community:**  
[![Discord](https://img.shields.io/discord/480782642825134100)](http://chat.rxlab.info) [![Contributor Covenant](https://img.shields.io/badge/contributor%20covenant-2.1-4baaaa.svg)](CODE_OF_CONDUCT.md) [![GitHub contributors](https://img.shields.io/github/contributors-anon/RxLaboratory/DuBlast)](https://github.com/RxLaboratory/DuBlast/graphs/contributors)  
[![Discord](https://img.shields.io/discord/480782642825134100?logo=discord&style=social&label=Discord)](http://chat.rxlab.info)
[![Facebook](https://img.shields.io/badge/Facebook-1877F2?logo=facebook&style=social)](https://www.facebook.com/rxlaboratory) [![Instagram](https://img.shields.io/badge/Instagram-E4405F?logo=instagram&style=social)](https://www.instagram.com/rxlaboratory/) [![Twitter Follow](https://img.shields.io/twitter/follow/RxLaboratory?label=Twitter&style=social)](https://www.twitter.com/rxlaboratory/) [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?logo=linkedin&style=social)](https://www.linkedin.com/company/RxLaboratory/) [![YouTube Channel Views](https://img.shields.io/youtube/channel/views/UC64qGypBbyM-ia-yf0nFSTg?label=Youtube)](https://www.youtube.com/channel/UC64qGypBbyM-ia-yf0nFSTg) [![Github](https://img.shields.io/github/stars/RxLaboratory?style=social&label=Github)](https://github.com/RxLaboratory)
<!-- end:join -->

## Quick Render Buttons

The [_Quick Render Buttons_](https://github.com/Thane5/quickrenderbuttons) add-on [here](https://github.com/Thane5/quickrenderbuttons) is a simple but handy add-on which includes a button for Playblasts by _DuBlast_ (you'll need to install both addons).

## Screenshots

![Menu](https://github.com/RxLaboratory/DuBlast/raw/master/docs/img/menu.png)

![Settings](https://github.com/RxLaboratory/DuBlast/raw/master/docs/img/settings.png)

## Difference between *DuBlast* and the native *Viewport Render Animation* command

|DuBlast|Viewport Render Animation|
|---------|---------------------------|
|**Automatically plays** the rendered animation|Needs the user to **manually play** the animation [Ctrl] + [F11]|
|**Has its own output settings**, so the user can create playblasts without altering the output settings of the scene|**Shares the output settings** with the scene/render settings, which means the user has to alter the output settings even if they're already set for rendering the scene|
|Has **custom output format presets** for better animation playback and seek|Needs the user to **manually set the output** to an animator friendly format|
|**Scales down the size of the text for the metadata** according to the resolution %|**Keeps the same size for the text of the metadata**, no matter the output resolution, which results in huge texts at lower resolution|
|Atomatically adjusts the rendered animation dimension to **fit the *MP4* requirements** when set to use *MP4*|The user has to **find a fitting resolution %** for the dimensions to have an even number of lines and columns|

## Current status

<!-- statistics -->
**Statistics:**  
[![GitHub all releases](https://img.shields.io/github/downloads/RxLaboratory/DuBlast/total)](https://github.com/RxLaboratory/DuBlast/releases) [![GitHub release (latest by SemVer)](https://img.shields.io/github/downloads/RxLaboratory/DuBlast/latest/total?sort=semver)](https://github.com/RxLaboratory/DuBlast/releases) [![GitHub issues](https://img.shields.io/github/issues-raw/RxLaboratory/DuBlast)](https://github.com/RxLaboratory/DuBlast/issues) [![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/RxLaboratory/DuBlast?color=lightgrey)](https://github.com/RxLaboratory/DuBlast/issues?q=is%3Aissue+is%3Aclosed) [![GitHub commit activity](https://img.shields.io/github/commit-activity/m/RxLaboratory/DuBlast)](https://github.com/RxLaboratory/DuBlast/graphs/commit-activity)<!-- end:statistics -->  

<!-- contribution -->
## Contribution and development

We're always in need for translations, code, documentation, examples, tutorials, quick tips, bug fixes...

[![Discord](https://img.shields.io/discord/480782642825134100)](http://chat.rxlab.info) [![Contributing](https://img.shields.io/badge/contributing%20guide-docs.rxlab.io-informational.svg)](http://docs.rxlab.io) [![Contributor Covenant](https://img.shields.io/badge/contributor%20covenant-2.1-4baaaa.svg)](CODE_OF_CONDUCT.md) [![GitHub contributors](https://img.shields.io/github/contributors-anon/RxLaboratory/DuBlast)](https://github.com/RxLaboratory/DuBlast/graphs/contributors)
<!-- end:contribution -->
