# bfheroes-offline
Allows you to run your own Battlefield Heroes environment without any internet connection (localhost).

## Release Candidates (Full downloads)
As you might have noticed **game files** and some other executables **aren't** sourced **here**, therefore you **wont be able to run anything**.

Full **release candidates** can be found **in this Discord**: https://discord.gg/9uwyBVA *(channel `#releases` under `bfheroes-offline` category)*

## Editing your hosts file
The following lines must be added to your hosts file (`Windows\System32\drivers\etc\hosts`)
```
127.0.0.1 www.battlefieldheroes.com
127.0.0.1 bfwest-dedicated.fesl.ea.com
127.0.0.1 bfwest-server.fesl.ea.com
127.0.0.1 fesl.ea.com
```

## Features
* Easily create heroes and edit their stats through noob-friendly .json files.
* All items and weapons in your inventory.
* Tutorial gamemode. Map and gamemode can be changed in `game/mods/bfheroes/Settings/maplist.con`
* Functional MagmaAPI (Magma has to be manually enabled in `src/config.ini`), which allows you to play around with entitlements/store/friends/bookmarks.

## To-do
* Local gameserver.

If you have any suggestions feel free to submit a pull request or contact my privately on Discord (linked above).

## Speed

| Action        | Time in seconds |
| ------------- |:---------------:|
| Login         | 11s             |
| Joining a game (tutorial)| ~20s             |
| Joining a game (gameserver)| ??s             |

## Thanks to
* **LifeCoder**: Helping me resolve packet encoding issues, Phoenix Network's `dinput8.dll`
* **Marek Grzyb**: BFHeroes_MasterServer repository in Python 2.7
