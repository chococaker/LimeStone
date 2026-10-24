<p align="center">
  <img src="https://github.com/chococaker/LimeStone/blob/main/readme_assets/banner.png?raw=true" alt="LimeStone Banner" width="100%">
</p>

<h1 align="center">LimeStone Circuit Simulator</h1>

<p align="center">
  <strong>An accurate, web-based 2D Redstone simulator for testing Minecraft contraptions outside of the game.</strong>
</p>

<p align="center">
  <a href="https://limestone.chococaker.xyz/"><strong>Live Demo »</strong></a>
</p>

<br />

## About The Project

**LimeStone** is a custom-built, 2D Minecraft Redstone simulator designed to let players and engineers experiment with complex contraptions directly in the browser.

Replicating Minecraft's internal mechanics is a complex logic and state-management challenge. Through extensive playtesting and research into the Minecraft Wiki, this simulator was built to behave as close to true vanilla Minecraft Redstone as possible. If it works in Minecraft (in 2D), it works in LimeStone, from a simple Redstone lamp array to a full-fledged computational chess engine.

_Art by @SublimedLime!_

## Key Technical Achievements

* **Accurate Logic Simulation:** Engineered to accurately mimic Minecraft's intricate update order, tick delays, and signal strengths without using the game's actual source code.
* **Complex System Scaling:** Capable of handling hundreds of interconnected components for advanced logic gate computing (e.g., calculators, mini-games).
* **Zero-Dependency Frontend:** Built entirely from scratch using Vanilla JavaScript, HTML, and CSS for a lightweight, highly performant browser experience.

## Tech Stack

* **Logic & Engine:** Vanilla JavaScript (`ES6+`)
* **Styling & Structure:** HTML5, CSS3
* **Automation/Tooling:** Python (Utility scripts)

## Getting Started

To run LimeStone locally on your machine, simply follow these steps. No build tools or dependencies are required!

```bash
git clone https://github.com/chococaker/LimeStone.git
cd LimeStone
```

Open `index.html` in your favorite web browser, or use a local live server extension to serve the files.

## Roadmap (What's Next?)

* **Infinite Zoom & Scaling:** Overhauling the grid system to support scroll-wheel zoom for massive, sprawling builds rather than manually setting height/width.
* **More Components:** Implementing complex blocks like Honey Blocks (for SlimeStone machines) and Container Blocks (Droppers, Dispensers, Chests).
* **Interactive Tutorials:** A built-in, step-by-step guide to teach complete beginners the fundamentals of logic gates and Redstone.
* **Graphics & Polish:** Adding particle effects, smoother animations, and better visual feedback.

## License

Distributed under the MIT License. See `LICENSE` for more information.
