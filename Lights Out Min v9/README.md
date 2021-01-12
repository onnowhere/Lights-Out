# Lights Out Min v9

Command size is counted by the size of the text file with LF endings in bytes,
with each command on a new line. See commands.txt for a list of commands used.
All commands stored anywhere before initialization will be listed in the file.
Additional arbitrary goals include making the base system all one line, having
the smallest possible blocks used after initialization, and not use functions.


- World: Lights Out Min v9
- Main Changes: Datapacks, resource packs, block tags, predicates, loot tables
- Command Count: 6
- Original Size: 1947 bytes
- Reduced Size: 163 bytes
- Reduction: 91.63%


## Challenge rules

Any cell interacted should toggle it's own color between white and black, as well as all immedately adjacent cells. Board must be a minimum of 4x4. There needs to be a win condition for both if player turns all lights off or on. Game must automatically randomize the board when generated in a win-able condition.


## Optimizations to reduce file size (compared to previous version)

- Utilizes a datapack
- Block tags a, b, and c shorten the fill replace commands
- Predicate l will output true if all blocks on board are clay OR all dirt
- This means only one repeating command is needed for win detection
- This leaves only one comparator needed
- Activation is now done with a structure block instead of a fill command
- The structure block places more structure blocks which then load commands each
- Avoids duplicate commands as there is only one set of commands in the structure at initialization
- Custom block loot table for redstone wire allows 50/50 chance of dropping TNT or nothing
- Redstone wire breaks immediately above air, allowing for board randomization with dropped item
- The resource pack makes the system look clean visually, and levers to look like buttons


## Compromises and considerations

- Requires a structure block nested in a structure block
- Requires datapacks (no functions)
- Resource pack is cosmetic and not necessarily needed, but makes the user experience clearer


## Credits

- Code golf challenge by: FetchBot and Lyfeless
- World created by: Onnowhere
- Reduced with help from: Command Master
- Additional input from: Miestrode, boxbox, vdvman1, FetchBot, Lyfeless, tryashtar, ncfumction, ErrorCraft, Cloud Wolf, Arcensoth, nick