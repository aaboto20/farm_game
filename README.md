# Untitled Farm Game

## Introduction

*Untitled Farm Game* is a light puzzle game that is about the player living in a pocket universe constructed by an alien AI.  They aren't a prisoner, more like a guest, tasked with helping the AI "transcribe" alien circuit constructions to build and expand their world.  To start, the player will find themself in a small cottage next to a transcriber outpost.  In the beginning, it will be a cold, desolate place until the player helps the AI to learn how to build expansions, a garden, and eventually animals and people to interact with.  As the AI grows smarter it will eventually warm up to the player and try to help it find a new world to call home. 

To transcribe a new object, the player works with the AI in a card game laying down wire, design, and power cards to build up points to allow them the experience enough to buy new items.  

## Usage

To play the game, run the following command in the root directory:

```bash
python farm_game.py
```

## Beginning Stage

The player begins with just the cottage (bed, radio, storage) and transcriber work station.  After transcribing the first time, player builds a planter and basil seeds to grow first vegetable.  Has a conversation with the AI about herbs that piques its interest.  The AI then informs the player it can help them grow a wider garden so it can eat nicer food other than protein shakes.  The player can then transcribe to expand the space into a 4x4 garden, add a kitchen onto the cottage, and create robots to help it with mundane tasks.  

## Middle Stage

Eventually the player will stop wanting to be alone and be given the option to clone people or animals.  Cloning animals will allow for the player to create environmental biomes they can start populating with animals.  Since the pocket universe protects them from harm within itself they are in no danger.  This will also allow the player to have a dog or cat at the cottage.  They can also populate the pocket universe with a small town of cloned people.  

## Late Stage

The player will want an ending to the game.  By now, the AI has advanced enough to build a seed ship to take the player to a new planet they can begin repopulating if they want to.  The game ends with them stepping out onto the new planet and meeting some friendly aliens.  

## Traversal

The game will be constructed as a tile-based RPG in Pygame using sprites.  The player will navigate the world by pressing UP,DOWN,LEFT, and RIGHT to move around the screen.  Interactions will feature a USE button once the player has walked close enough to the object.  The sprites will be created in Aseprite.  

## Garden

The garden will be interacted with by using a seed on a plot of land, watering it, waiting a few days for it to grow, and harvesting.  I would like gardening to be more of a meditative exercise since survival won't be necessary in this world.  I think it might be good to implement a more detailed vegetable reward system by introducing factors like spacing, soil depth, soil quality, and water and sun amounts into gardening.  The player should be given ample time to think about these things and doing it right will result in better quality.  

Crop-growing in games like Stardew Valley feels more like a race against time on bigger farms and I'd like it to be something you do to relax and not think too much about.  Eventually, the player can also transcribe automatic watering tools and robots to help with growing.  

## Cooking

Cooking should be like a fun mini-game that should also feel meditative and reward based on quality of ingredients and your recipes.  Cooking should feel a little simpler and maybe have more of an action feel to it to make it a little more exciting to gardening.  Recipes can be comprised of certain ingredients and then the player must press a button at a certain time to cook the food well enough.  Using better ingredients will also improve the food quality.  Maybe a rhythm game?

## Cottage

The cottage is where the player will primarily sleep to pass time.  Sleeping will cause one day to pass.  The player can also store items here like new clothes, tools they aren't using, and eventually their pet will come and go here.  

## Transcriber Summary

The transcriber is a part of the AI-run cottage that transcribes Earth data into its knowledge-base so that it can learn to build new structures and robots to help the player.  In time, it can also be used to clone organic life forms.  The start of this is the vegetable garden and then animals and then people.

## Gameplay

Each player starts their turn with 20 cards in their deck.  On their turn, a player may choose to draw 5 cards from the top of the deck.  The player can then examine their hand and strategically lay down the circuit fragment cards on the playing area to form a complete circuit.  The goal is to create a looped circuit using the smallest number of cards possible.  Players may connect circuit fragment cards in any orientation or arrangement as long as they form a valid circuit.  A power card must be play   ted in order to complete a start a circuit.  When a power card is played, players must finish the round and then tally up their earned points.

### Winning Condition

The player who successfully completes a looped circuit by playing the loop piece card with the fewest total cards in their completed circuit is the winner.

### Assets List

Straight wires in different directions (horizontal, vertical, diagonal): 10

Curved wires in different orientations (clockwise, counterclockwise):5

Resistor or capacitor components: 4

LED or lightbulb components: 4

Power source symbols (battery or power plug): 4

Circuit breakers or fuses: 4

Intersection points: 5

transformer:  3

Switches or toggle buttons: 3

Resistor or capacitor components: 3

LED or lightbulb components: 3

Power source symbols: 3

Players work together to play construction pieces, with cooperative goal to build technology.  Use cards like LEDs or switches to give themselves points but don't help the build.  Player who gets the power source card must play it if its their last card.  Multiple power source cards are allowed and will give extra points.  Points are earned by how many build cards they used, design cards.  Straight and curved line cards are worth 1 point; LED, switch, and audio cards worth 2 points; and power card is worth 3 points.

Players are given 5 cards to start, take turns one at time laying down design cards, but can trade for new cards on their turn.  Can only trade 1,2, or 3 cards.

## Start Round

Dealer draws card at top of deck.  If power source, players just need to play enough cards to loop back to it.  Multiple power source cards can be played if in players' current hands, but round is over once the last player plays.

## Card Descriptions

straight card or curved - a card with a straight or curved wire.  1 point.  only goes in one direction so the player to the left would go next.

resistor or capacitor components - reduces the power of the power source card.

transformer - lowers the total draw of power from the power source, allowing for more power sources which also allows for more power-heavy cards like sound controllers or generators to be played

light bulb - creates light. uses a little power

heavy machinery - uses a lot of power

switch or toggle button - card that creates an alternative parallel circuit that also must be completed but doubles points

## Garden Work Breakdown Structure Outline

### Test soil

Use the transcriber to smarten the AI.   It tells you how to test the soil for PH balance.  You work together to find the soil is too acidic.  

Transcribe limestone to add to the soil to neutralize the acid.  

Transcribe earthworms to help the soil.

### Plant seeds

Transcribe spice and herb seeds.  You are given the option of starting with basil, sage, or chili peppers.

You plant the seeds.  

Water seeds.

Pass time.

Harvest plants.

Till soil.

Repeat.

From here, you can perform basic cooking. Your first recipe involves adding your plant to your oatmeal.  It is not good at first but the AI says if they can keep transcribing they'll help them expand their ingredients.

## Cooking Work Breakdown Structure

Begin cooking

Select recipe

Select ingredient 1

Select ingredient 2

Button press at correct time to take food off stove.

Quality will be determined by how in time they finish, quality of ingredients, and how many times they've cooked the food.

