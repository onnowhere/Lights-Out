# Lights Out Min v7

Command size is counted by the size of the text file with LF endings in bytes,
with each command on a new line. See commands.txt for a list of commands used.
All commands stored anywhere before initialization will be listed in the file.
Additional arbitrary goals include making the base system all one line, having
the smallest possible blocks used after initialization, and not use functions.


- World: Lights Out Min v7
- Main Changes: Structure blocks, cod in structure
- Command Count: 8
- Original Size: 1947 bytes
- Reduced Size: 319 bytes
- Reduction: 83.62%


## Challenge rules

Any cell interacted should toggle it's own color between white and black, as well as all immedately adjacent cells. Board must be a minimum of 4x4. There needs to be a win condition for both if player turns all lights off or on. Game must automatically randomize the board when generated in a win-able condition.


## Optimizations to reduce file size (compared to previous version)

- Removed summon cod command in favor of a structure block that loads the cod directly
- Structure block is auto activated on clone by powered lever block update
- The cod can now be invisible, silent, and have no death animation due to being preloaded


## Compromises and considerations

- Requires the use of structure blocks
- Cod is now totally invisible and silent to the player, making generation cleaner
- Allowing structure blocks raises the question of simply loading a redstone-only implementation
- Due to this, there will be more focus on making the resulting system contain as few blocks as possible from here on, by using commands together with redstone and structure blocks without functions
- This change in goal may not be ideal, and the goals become somewhat more arbitrary from here on


## Credits

- Code golf challenge by: FetchBot and Lyfeless
- World created by: Onnowhere
- Reduced with help from: Command Master
- Additional input from: Miestrode, boxbox, vdvman1, FetchBot, Lyfeless, tryashtar, ncfumction, ErrorCraft, Cloud Wolf, Arcensoth, nick