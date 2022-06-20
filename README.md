# DuBlast - Duduf Playblast

Quick Playblast tool for Blender

*DuBlast* is part of the DuBLF, the [Duduf Blender Framework](https://rainboxlab.org/tag/blender/), a toolset developped by [Duduf](https://duduf.com) & [Rainbox Laboratory](https://rainboxlab.org) for their productions.

*DuBlast* is an add-on for *Blender* which makes it easy to create and play animation playblasts, without having to change any render or output setting.

📖 A **comprehensive user documentation** is [available here](https://dublast-docs.rainboxlab.org).

🎥 You can **download the latest public version [here](https://rainboxlab.org/tools/dublast/)**.

📣 You can also **help the developper** (Nicolas "Duduf" Dufresne) **and access Beta versions** on [Patreon](https://patreon.com/duduf), or you can [make a donation to Rainbox Laboratory](https://rainboxlab.org/about/donate/) to help the maintenance and distribution of all our free tools.

## Community

🚀 [Join us and have a chat](http://chat.rainboxlab.org) to get started!

🤗 We'd be happy to welcome you on the [forum](https://forum.rainboxlab.org) too.

## Quick Render Buttons

The [_Quick Render Buttons_](https://github.com/Thane5/quickrenderbuttons) add-on [here](https://github.com/Thane5/quickrenderbuttons) is a simple but handy add-on which includes a button for Playblasts by _DuBlast_ (you'll need to install both addons).

## Screenshots

![Menu](https://github.com/blastframe/DuBlast/raw/master/docs/img/menu.png)

![Settings](https://github.com/blastframe/DuBlast/raw/master/docs/img/settings.png)

## Difference between *DuBlast* and the native *Viewport Render Animation* command

|DuBlast|Viewport Render Animation|
|---------|---------------------------|
|**Automatically plays** the rendered animation|Needs the user to **manually play** the animation [Ctrl] + [F11]|
|**Has its own output settings**, so the user can create playblasts without altering the output settings of the scene|**Shares the output settings** with the scene/render settings, which means the user has to alter the output settings even if they're already set for rendering the scene|
|Has **custom output format presets** for better animation playback and seek|Needs the user to **manually set the output** to an animator friendly format|
|**Scales down the size of the text for the metadata** according to the resolution %|**Keeps the same size for the text of the metadata**, no matter the output resolution, which results in huge texts at lower resolution|
|Atomatically adjusts the rendered animation dimension to **fit the *MP4* requirements** when set to use *MP4*|The user has to **find a fitting resolution %** for the dimensions to have an even number of lines and columns|
