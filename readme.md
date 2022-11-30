# Treasure Chooser

This desktop application is being developed to assist the user in choosing the order in which treasure chests they should open while playing the mini-game A.M.A.N. Trove in Square Enix's MMORPG *Final Fantasy XI*.

## Description of Event
An indepth explanation of the event can be found [here](https://www.bg-wiki.com/ffxi/Category:A.M.A.N._Trove). 
A short explanation is that you enter an arena where there are 11 chests with unknown conditions: 
1) 1 chest is a fake, and if it is opened your character will be defeated and you lose all acquired treasure.
2) 1 chest located in the center of all the chests which allows you to leave the arena with all acquired treasure.
3) 9 chests that have varying levels of treasure going from noise(low) => thud(med) => loud thud(high) values.

The flow of the event is that you enter the arena, choose the treasure chests until you a) get the fake chest and lose the event or b) exit the event with treasure in hand. 

## Layout
The treasure is arranged in 3 rows with 5 treasure being on the top and bottom row and the 1 treasure chest that lets you leave with your goods in the center:<br>
[#] [#] [#] [#] [#] <br>
&emsp;&emsp;&emsp;[#] <br>
[#] [#] [#] [#] [#] <br>

## Functionality
The project will display the three rows of treasure chests and then place numbers over the pictures to show the order in which the treasure chests will be opened. A left click will show the chest as "opened" and a right click will show the chest as the "fake."

## Disclaimer
This project was conceived after watching a youtuber play through this event using a similar methodology. Crediting [CallMeKwetch](https://www.youtube.com/@Scottydeluxe) with the initial idea that I spun off of to make this. Should the creator release an official version, please visit their page and support the creator. This is for my educational purposes and to get better at programming in Python.


