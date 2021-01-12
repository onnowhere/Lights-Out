# Lights Out

## Download: https://github.com/onnowhere/Lights-Out/releases

## Table of Contents
- [Lights Out](Lights%20Out/README.md)
- [Lights Out Min v1](Lights%20Out%20Min%20v1/README.md)
- [Lights Out Min v2](Lights%20Out%20Min%20v2/README.md)
- [Lights Out Min v3](Lights%20Out%20Min%20v3/README.md)
- [Lights Out Min v4](Lights%20Out%20Min%20v4/README.md)
- [Lights Out Min v5](Lights%20Out%20Min%20v5/README.md)
- [Lights Out Min v6](Lights%20Out%20Min%20v6/README.md)
- [Lights Out Min v7](Lights%20Out%20Min%20v7/README.md)
- [Lights Out Min v8](Lights%20Out%20Min%20v8/README.md)
- [Lights Out Min v9](Lights%20Out%20Min%20v9/README.md)
- [Lights Out Min v10](Lights%20Out%20Min%20v10/README.md)


## Info

These maps were made for a challenge to implement Lights Out in the smallest way possible. Each version from 1 to 10 progressively makes more compromises and interpretations of the rules, for example, version 7 introduces structure blocks and version 9 allows the use of datapacks without functions. Each world has a corresponding README file detailing what optimizations, compromises, and considerations were used in its making, along with a list of commands used. In the end, this was moreso just a fun, non-serious experiment into different ways to achieve the same goal.


## Challenge rules

Any cell interacted should toggle it's own color between white and black, as well as all immedately adjacent cells. Board must be a Minimum of 4x4. There needs to be a win condition for both if player turns all lights off or on. Game must automatically randomize the board when generated in a win-able condition.


## Code golf criteria

Command size is counted by the size of the text file with LF endings in bytes,
with each command on a new line. See commands.txt for a list of commands used.
All commands stored anywhere before initialization will be listed in the file.
Additional arbitrary goals include making the base system all one line, having
the smallest possible blocks used after initialization, and not use functions.


## Credits

- Code golf challenge by: FetchBot and Lyfeless
- Worlds created by: Onnowhere
- Reduced with help from: Command Master
- Additional input from: Miestrode, boxbox, vdvman1, FetchBot, Lyfeless, tryashtar, ncfumction, ErrorCraft, Cloud Wolf, Arcensoth, nick