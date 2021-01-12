# Lights Out Min v1

Command size is counted by the size of the text file with LF endings in bytes,
with each command on a new line. See commands.txt for a list of commands used.
All commands stored anywhere before initialization will be listed in the file.
Additional arbitrary goals include making the base system all one line, having
the smallest possible blocks used after initialization, and not use functions.


- Main Changes: Cats instead of AECs, absolute instead of relative coords
- Command Count: 18
- Original Size: 1947 bytes
- Reduced Size: 1057 bytes
- Reduction: 45.71%


## Challenge rules

Any cell interacted should toggle it's own color between white and black, as well as all immedately adjacent cells. Board must be a minimum of 4x4. There needs to be a win condition for both if player turns all lights off or on. Game must automatically randomize the board when generated in a win-able condition.


## Optimizations to reduce file size (compared to previous version)

- Absolute coordinates where possible
- Objectives, tags, and fake players changed to one character
- Blocks changed to white_wool, black_wool, and dirt instead of concrete and barriers to reduce char count
- Using conditional commands to reduce command length
- Summoning cats instead of AECs due to short 3 letter name
- Using scores={...} instead of if score
- Using as @s[...] instead of if entity
- Grabbing nearest cat instead of more exact location check, as we don't need perfect location check


## Compromises and considerations

- Conditional chain command blocks used
- Wool doesn't look quite as good compared to concrete but still works
- Cats appear in the void for a moment during summoning
- Can't be located anywhere vertically as we are using absolute coordinates


## Credits

- Code golf challenge by: FetchBot and Lyfeless
- World created by: Onnowhere
- Reduced with help from: Command Master
- Additional input from: Miestrode, boxbox, vdvman1, FetchBot, Lyfeless, tryashtar, ncfumction, ErrorCraft, Cloud Wolf, Arcensoth, nick