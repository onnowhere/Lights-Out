# Lights Out Min v6

Command size is counted by the size of the text file with LF endings in bytes,
with each command on a new line. See commands.txt for a list of commands used.
All commands stored anywhere before initialization will be listed in the file.
Additional arbitrary goals include making the base system all one line, having
the smallest possible blocks used after initialization, and not use functions.


- World: Lights Out Min v6
- Main Changes: Flip system to be horizontal, observer for inputs, comparator win output
- Command Count: 9
- Original Size: 1947 bytes
- Reduced Size: 331 bytes
- Reduction: 83.00%


## Challenge rules

Any cell interacted should toggle it's own color between white and black, as well as all immedately adjacent cells. Board must be a minimum of 4x4. There needs to be a win condition for both if player turns all lights off or on. Game must automatically randomize the board when generated in a win-able condition.


## Optimizations to reduce file size (compared to previous version)

- Rotated entire system 90 degrees to be horizontal
- This allows us to remove [facing=up] from the fill command block command
- Using observers allows us to directly pick up the input and trigger a plus sign of cells
- The input now must use levers to trigger observers one time on click
- Since observer has delay, we can use ice as intermediate block to save one character
- Win check uses two comparators to trigger one win command block, reducing need for two outputs
- Instead of printing GG, we can just say a single letter and name the command block to 'You Win!!!'
- `me *` will output '* You Win!!! *' where the text comes from the command block name


## Compromises and considerations

- No longer requires custom superflat
- Comparators prevent win output spam by running once on detection
- Levers are more confusing than buttons as toggling acts as a button press instead of on/off
- Comparators require barriers underneath for support, which bend the one line rule


## Credits

- Code golf challenge by: FetchBot and Lyfeless
- World created by: Onnowhere
- Reduced with help from: Command Master
- Additional input from: Miestrode, boxbox, vdvman1, FetchBot, Lyfeless, tryashtar, ncfumction, ErrorCraft, Cloud Wolf, Arcensoth, nick