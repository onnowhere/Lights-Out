# Lights Out Min v3

Command size is counted by the size of the text file with LF endings in bytes,
with each command on a new line. See commands.txt for a list of commands used.
All commands stored anywhere before initialization will be listed in the file.
Additional arbitrary goals include making the base system all one line, having
the smallest possible blocks used after initialization, and not use functions.


- World: Lights Out Min v3
- Main Changes: Skip deleting init commands, fill command blocks, arrows to trigger button
- Command Count: 10
- Original Size: 1947 bytes
- Reduced Size: 461 bytes
- Reduction: 76.32%


## Challenge rules

Any cell interacted should toggle it's own color between white and black, as well as all immedately adjacent cells. Board must be a minimum of 4x4. There needs to be a win condition for both if player turns all lights off or on. Game must automatically randomize the board when generated in a win-able condition.


## Optimizations to reduce file size (compared to previous version)

- Removed the fill command to delete the init commands
- Move the init commands higher so that player can access board even if init commands remain
- Fill command blocks that clone the source column instead of recursively cloning in steps
- This means we can delete the command that uses entity position selector to stop generation
- Use wooden buttons that can trigger by arrows
- Perform randomization by summoning arrows with life:9000 that trigger the buttons and then despawn
- Place clay & sand below commands that fill the 8x8 area during generation to use for WIN check
- Use execute if blocks vs checking a score with clone to compare with blocks below commands
- Result of above means we no longer need a score objective init command
- Use GG instead of WIN for win notification
- Use me instead of say


## Compromises and considerations

- Wooden buttons take longer to depress than stone buttons
- Lag during generation as everything happens at once
- Arrow sounds in addition to cod sounds are noisy
- Init commands must be moved higher up to give space for the board
- The init commands stay present in the world and don't look the best
- Fixes issue of printing WIN in generation because summon command is after arrow command
- Unicode symbol instead of WIN would be more bytes than GG, must clearly indicate winning
- Can't remove [facing=up] as commands layed out sideways would cause implementation to be longer
- Arrow needs nbt tag else it takes too long to despawn before player can play, even with life:999
- Randomizer needs to limit to 1 to avoid issues with randomization in one tick


## Credits

- Code golf challenge by: FetchBot and Lyfeless
- World created by: Onnowhere
- Reduced with help from: Command Master
- Additional input from: Miestrode, boxbox, vdvman1, FetchBot, Lyfeless, tryashtar, ncfumction, ErrorCraft, Cloud Wolf, Arcensoth, nick