# LimeStone RS Simulator

Our entry for the [2025 Codesprout Hackathon](https://codesprout.devpost.com/).

![LimeStone banner](https://github.com/chococaker/LimeStone/blob/main/readme_assets/banner.png?raw=true)

|💡 Note|
|--|
| There is some Python used in the project because we are **generating assets**, mainly to transform used assets to conform to different states. This is a one-time operation, and was left in the repository for reference. |

The LimeStone Simulator is a project built to give people the ability to test Redstone contraptions, and to provide a fun and not-overwhelming way to children to learn some electrical engineering.

This is a Minecraft Redstone simulator build to be faithful to the original game as much as possible. Many hours were put into looking through the Wiki and playing the game, researching how _exactly_ Redstone works, down to a T. As long as it's 2D, anything from a couple lamps connected to a clock to a Redstone chess engine is possible, as long as you have the RAM and the technical skill.

## What's next
We plan to add a "tutorial," explaining basic Minecraft Redstone concepts to those who wish to go into it a bit more.

In terms of graphics, we want to add particles and animations to make the experience more interactive and realistic.

We also want to be able to scale up and down the graph infinitely (currently, all you can do is set the "height" and "width" in `script.js`) using the scrollwheel. This will allow for much larger-scale projects to be created using this program.

Additionally, while nearly all core Minecraft Redstone components have been implemented, just a couple haven't been added or completed as of yet. These are listed below:
- **Honey Blocks**: While not important to every Redstone contraption prior to 1.19, these blocks are vital towards building highly advanced slimestone structures. We left these out because we believed them to be too far out of the scope of this project to be vital.
- **Sticky Pistons**: We are on the final stages of adding these, but decided to leave them out so that people can become immersed with the accuracy of this model, instead of needing to face possible bugs.
- **Comparators**: We are currently in the process of drafting code for these as well.


