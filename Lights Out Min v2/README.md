# Lights Out Min v2

Command size is counted by the size of the text file with LF endings in bytes,
with each command on a new line. See commands.txt for a list of commands used.
All commands stored anywhere before initialization will be listed in the file.
Additional arbitrary goals include making the base system all one line, having
the smallest possible blocks used after initialization, and not use functions.


- World: Lights Out Min v2
- Main Changes: Cod instead of cats, clay and sand instead of wool, sort=random instead of UUID
- Command Count: 15
- Original Size: 1947 bytes
- Reduced Size: 639 bytes
- Reduction: 67.18%


## Challenge rules

Any cell interacted should toggle it's own color between white and black, as well as all immedately adjacent cells. Board must be a minimum of 4x4. There needs to be a win condition for both if player turns all lights off or on. Game must automatically randomize the board when generated in a win-able condition.


## Optimizations to reduce file size (compared to previous version)

- Using a fake player instead of a player selector
- Using a 0 character objective and fake player name (apparently this is allowed)
- Third line deletion command means we do not need to check the entity in later commands
- From above, we can remove execute from the clone commands in line 4 and 5
- Use clay and sand instead of wool to reduce block name length to 4
- Summon cod instead of cat, and use no position and tag argument
- Since it summons at the command and lands on the board, cod is best as it dies fast out of water
- Cod remaining for a short time allows the randomizer to function well
- Instead of UUID randomizer, select 9 random entities to run their cell per generation step
- Use one clone and score check to determine win with 1..63


## Compromises and considerations

- Due to possibility of win check returning 0 in first step, may print WIN once in generation
- Gamerule doMobLoot must be disabled to prevent cod drops (cosmetic reasons)
- Clay and sand look less pretty but still are dicernable from each other on the board
- Cannot use ice and tnt as they either blow up or cause the command to trigger twice from unpowering


## Credits

- Code golf challenge by: FetchBot and Lyfeless
- World created by: Onnowhere
- Reduced with help from: Command Master
- Additional input from: Miestrode, boxbox, vdvman1, FetchBot, Lyfeless, tryashtar, ncfumction, ErrorCraft, Cloud Wolf, Arcensoth, nick