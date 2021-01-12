# Lights Out Min v8

Command size is counted by the size of the text file with LF endings in bytes,
with each command on a new line. See commands.txt for a list of commands used.
All commands stored anywhere before initialization will be listed in the file.
Additional arbitrary goals include making the base system all one line, having
the smallest possible blocks used after initialization, and not use functions.


- World: Lights Out Min v8
- Main Changes: Commands in structures, no command changes, no barriers, redstone powered but not active
- Command Count: 8
- Original Size: 1947 bytes
- Reduced Size: 319 bytes
- Reduction: 83.62%


## Challenge rules

Any cell interacted should toggle it's own color between white and black, as well as all immedately adjacent cells. Board must be a minimum of 4x4. There needs to be a win condition for both if player turns all lights off or on. Game must automatically randomize the board when generated in a win-able condition.


## Optimizations to reduce file size (compared to previous version)

- No commands have been shortened or removed
- The system is now cleaner to use with commands in structure blocks
- All commands that will be duplicated have been stored in the structure block
- The cloned structure block is stored at the back, where it will not be block updated
- The structure block and command blocks are redstone powered but not running before initialization
- Cloned structure block and redstone block pairs will block update and place the structure
- The comparators were set by directly editing the region files to float and avoid block updates
- The generated system will be directly below the initial commands
- Because the commands are powered but not running at the start, the comparators do not update
- The floating redstone torch will force the commands to run once block updated
- After generation, the generated commands become the floor for the comparators and redstone torch
- Then, the command blocks and comparators will block update and start running win detection


## Compromises and considerations

- Barriers are no longer required, true 1x1xN initialization system
- Requires having commands in structure blocks
- Commands in all structure files count towards total
- If more than one copy of a structure block is in the world before initialization, the - Command Count will be doubled
- After initialization, created structure blocks won't be added to count (similar to clone)


## Credits

- Code golf challenge by: FetchBot and Lyfeless
- World created by: Onnowhere
- Reduced with help from: Command Master
- Additional input from: Miestrode, boxbox, vdvman1, FetchBot, Lyfeless, tryashtar, ncfumction, ErrorCraft, Cloud Wolf, Arcensoth, nick