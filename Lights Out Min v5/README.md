# Lights Out Min v5

Command size is counted by the size of the text file with LF endings in bytes,
with each command on a new line. See commands.txt for a list of commands used.
All commands stored anywhere before initialization will be listed in the file.
Additional arbitrary goals include making the base system all one line, having
the smallest possible blocks used after initialization, and not use functions.


- World: Lights Out Min v5
- Main Changes: Redstone torch cell toggle, directly setting clay (all boards solveable)
- Command Count: 11
- Original Size: 1947 bytes
- Reduced Size: 383 bytes
- Reduction: 80.33%


## Challenge rules

Any cell interacted should toggle it's own color between white and black, as well as all immedately adjacent cells. Board must be a minimum of 4x4. There needs to be a win condition for both if player turns all lights off or on. Game must automatically randomize the board when generated in a win-able condition.


## Optimizations to reduce file size (compared to previous version)

- Instead of toggling cells using 5 fill commands, we can use redstone logic
- The above change lets us implement block swapping in 4 commands instead
- We set a redstone torch to activate 5 cells in a plus shape above the torch
- Each cell will toggle only its own block above it instead of the entire plus shape
- Since we realized all 8x8 boards are solvable, we directly set 1 clay to randomize instead


## Compromises and considerations

- Player may set clay randomly, which can be confusing, but shouldn't disrupt generation or gameplay
- Board size cannot be 4x4, 5x5, or 9x9 due to chance of unsolvability
- The following is the result of calculating how many boards with only lights on the bottom row are solveable:

Board Size: 1, solvable: 2, unsolveable: 0
Board Size: 2, solvable: 4, unsolveable: 0
Board Size: 3, solvable: 8, unsolveable: 0
Board Size: 4, solvable: 1, unsolveable: 15
Board Size: 5, solvable: 8, unsolveable: 24
Board Size: 6, solvable: 64, unsolveable: 0
Board Size: 7, solvable: 128, unsolveable: 0
Board Size: 8, solvable: 256, unsolveable: 0
Board Size: 9, solvable: 2, unsolveable: 510
Board Size: 10, solvable: 1024, unsolveable: 0
Board Size: 11, solvable: 32, unsolveable: 2016
Board Size: 12, solvable: 4096, unsolveable: 0
Board Size: 13, solvable: 8192, unsolveable: 0
Board Size: 14, solvable: 1024, unsolveable: 15360
Board Size: 15, solvable: 32768, unsolveable: 0
Board Size: 16, solvable: 256, unsolveable: 65280
Board Size: 17, solvable: 32768, unsolveable: 98304
Board Size: 18, solvable: 262144, unsolveable: 0
Board Size: 19, solvable: 8, unsolveable: 524280
Board Size: 20, solvable: 1048576, unsolveable: 0


## Credits

- Code golf challenge by: FetchBot and Lyfeless
- World created by: Onnowhere
- Reduced with help from: Command Master
- Additional input from: Miestrode, boxbox, vdvman1, FetchBot, Lyfeless, tryashtar, ncfumction, ErrorCraft, Cloud Wolf, Arcensoth, nick