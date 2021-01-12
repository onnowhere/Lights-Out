# Lights Out Min v10

Command size is counted by the size of the text file with LF endings in bytes,
with each command on a new line. See commands.txt for a list of commands used.
All commands stored anywhere before initialization will be listed in the file.
Additional arbitrary goals include making the base system all one line, having
the smallest possible blocks used after initialization, and not use functions.


- World: Lights Out Min v10
- Main Changes: Redstone ore board, random tick randomizer, fireworks for the win
- Command Count: 3
- Original Size: 1947 bytes
- Reduced Size: 116 bytes
- Reduction: 94.04%


## Challenge rules

Any cell interacted should toggle it's own color between white and black, as well as all immedately adjacent cells. Board must be a minimum of 4x4. There needs to be a win condition for both if player turns all lights off or on. Game must automatically randomize the board when generated in a win-able condition.


## Optimizations to reduce file size (compared to previous version)

- Redstone ore has a random time to turn from lit to unlit
- By setting random tick speed to 2000, we can get this to happen faster
- Now we only need two commands to change clay to lit redstone ore and unlit redstone ore to clay
- This block update triggers the lamp and updates the observer, causing the line to flip colors
- Since this is random, at a certain point in time, the system will 'stabilize' its observers
- This means no more redstone ore updates will trigger the line to flip colors after a time
- This means we no longer need loot tables or entities for randomization
- Resource pack now replaces dirt with redstone ore as well
- Instead of a command for announcing win, now it is just a firework dispenser
- A block tag can have no name, allowing for `#[lit=false]`


## Compromises and considerations

- This requires randomTickSpeed to be 2000
- There is a chance, if a player presses too quickly, that the ore may not stop being lit in time
- This setup allows for the game to be reset infinite times without bugs by initializing again
- The player no longer places a stray clay block as the randomization is built in to redstone ore
- Initial randomization may be less 'random' than running the structure again to reset
- This is due to some quirkiness with the setup timings
- It is still suitably random, just less of one color will appear on the board initially
- A predicate can have no name, but cannot be referred in game with just `if predicate` alone
- This is the final implementation and smallest implementation
- 6x8x9 blocks in size after initialization without using any extra space


## Credits

- Code golf challenge by: FetchBot and Lyfeless
- World created by: Onnowhere
- Reduced with help from: Command Master
- Additional input from: Miestrode, boxbox, vdvman1, FetchBot, Lyfeless, tryashtar, ncfumction, ErrorCraft, Cloud Wolf, Arcensoth, nick