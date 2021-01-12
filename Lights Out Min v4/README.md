# Lights Out Min v4

Command size is counted by the size of the text file with LF endings in bytes,
with each command on a new line. See commands.txt for a list of commands used.
All commands stored anywhere before initialization will be listed in the file.
Additional arbitrary goals include making the base system all one line, having
the smallest possible blocks used after initialization, and not use functions.


- World: Lights Out Min v4
- Main Changes: Custom superflat, separate repeating win checker
- Command Count: 12
- Original Size: 1947 bytes
- Reduced Size: 452 bytes
- Reduction: 76.78%


## Challenge rules

Any cell interacted should toggle it's own color between white and black, as well as all immedately adjacent cells. Board must be a minimum of 4x4. There needs to be a win condition for both if player turns all lights off or on. Game must automatically randomize the board when generated in a win-able condition.


## Optimizations to reduce file size (compared to previous version)

- Moved win check commands to a separate third repeating line
- Separated execute if blocks from me GG in two commands to avoid 'run' keyword in execute
- The world now uses a custom superflat void with void_air on y=0 and y=1
- This prevents the new win checker printing multiple times in generation due to void_air difference
- Moving bottom commands down means the arrow now summons at y=8 instead of y=11, removing 1 char


## Compromises and considerations

- Win checker will print GG repeatedly on win
- Requires a non-default superflat generation
- Win checker prints once during generation of first column
- Conditional chain command blocks required for me GG commands
- Requires two extra command blocks but reduces command file size


## Credits

- Code golf challenge by: FetchBot and Lyfeless
- World created by: Onnowhere
- Reduced with help from: Command Master
- Additional input from: Miestrode, boxbox, vdvman1, FetchBot, Lyfeless, tryashtar, ncfumction, ErrorCraft, Cloud Wolf, Arcensoth, nick