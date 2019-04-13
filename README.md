# bfheroes-offline
bfheroes-offline allows you to run your own Battlefield Heroes environment without any internet connection (localhost).

## Release Candidates (Full downloads)
As you might have noticed **game files** and some other executables **aren't** sourced **here**, therefore you **wont be able to run anything**.

Full **release candidates** can be found **in this Discord**: https://discord.gg/9uwyBVA *(channel: #bfheroes-offline)*

## Features
* Easily create heroes and edit their stats through noob-friendly .json files.
* All items and weapons in your inventory.
* Tutorial gamemode. Map and gamemode can be changed in `game/mods/bfheroes/Settings/maplist.con`

## To-do
* Local gameserver.
* A few tweaks in MagmaAPI to support fully enabled magma without unexpected crashes.

If you have any suggestions feel free to submit a pull request or contact my privately on Discord (linked above).

## Thanks to
* **LifeCoder**: Helping me resolve packet encoding issues, Phoenix Network's `dinput8.dll`
* **Marek Grzyb**: BFHeroes_MasterServer repository in Python 2.7

## Speed

| Action        | Time in seconds |
| ------------- |:---------------:|
| Login         | 11s             |
| Joining a game (tutorial)| ~20s             |
| Joining a game (gameserver)| ??s             |
