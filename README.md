
# D&D NPC & Place Manager

This is a command-line Python application for managing NPCs and Places in Dungeons & Dragons.

This program allows you to **create, edit, retrieve and export** NPC and place data.

This tool is ideal for DMs who could use a program to keep track of their NPCs and places

  

# Setup

  

Before you can use this project you have to change a few things.

  

### 1. Create the database

  

First you need to **create a database npc_manager.db**

For this there are 2 options:

- if you want an empty database change the name of npc_manager_empty.db to npc_manager.db (this is a database that includes the tables npc and place but these tables are empty.)

- if you want a database with some examples change the name of npc_manager_example.db to npc_manager.db (this is a database that also includes the tables npc and place but these tables have some example values.)

  

### 2. Install libraries

  

Secondly you need to **install the libraries** in requirements.txt.

This can easily be done by using the command **pip install -r requirements.txt**

  

# Running the program

  

You can start the program by typing Python NpcManager.py *arguments*

  

## Valid arguments:

  

### Without arguments

  

Using this you can get info about one NPC or place.

  

### -csv *table*  *filename*

  

Where **table** is the table you want (**npc or place**)

and **filename** the full name of the csv file you would like to save the info to (the file doesn't have to exist yet)

This will save all data from the table into a csv file.

  

### -excel *table*  *filename*

  

Where **table** is the table you want (**npc or place**)

and **filename** the full name of the excel file you would like to save the info to (the file doesn't have to exist yet)

This will save all data from the table into an excel file.

  

### -new *table*

  

Where **table** is the table you want (**npc or place**)

This will ask you info about a npc or place and add this npc or place to the given table.

  

### -edit *one_edit*  *table*

  

Where **one_edit** is **True** if you want to edit it for one row and **False** when you want to edit it for all rows

and **table** is the table you want (**npc or place**)

This will ask you some values to get what row(s) you want to edit and the value you want to change and change that value for those row(s)

**examples:**

- if you have a NPC that aged and now is older you can use **-edit True npc** to change the value for this specific NPC

- if you suddenly find out you've been writing the name of a city wrong the whole time you can use **-edit False place** to change the name of all the places in that city.

  

### -get *table*

  

Where **table** is the table you want (**npc or place**)

You can use this to get a list of all NPCs or places with a specific name.

  

# Database Structure

  

Here is the structure of the database. I recommend looking at this to learn what each table and column is.

  

## Place table

  

The place table is a table with the places in your D&D world. This could be caves, dungeons, castles, taverns, shops, ...

  

### Columns

  

**name:** This is the name of the place.

**city:** this is the city the place is in or near.

**danger_level:** This is a number from 1 to 10 that indicates how dangerous this place is.

**description:** this is a brief description of what this place is. This field can be left empty if you don't have a description yet

  

## NPC table

  

The NPC table is a table with NPCs in your world. This could be a villain, ally, bartender, musician, ...

  

### Columns

  

**name:** This is the name of the NPC.

**race:** This is the race of the NPC. (for example: Human, Dwarf, Elf, Orc, Tiefling, ...)

**gender:** This is the first letter of the gender of the NPC. (M for male, F for female or X for other) (if you don't know the gender yet you can leave this field empty.)

**age:** This is the age of the NPC. Because some races can grow very old there is no limit on the size of this field. (if you don't know the age yet you can leave this field empty.)

**role:** This is what the NPCs role to the party is in the campaign. (for example: Bartender, Main villain, Bard, Ally, ...)

**place_id:** This is the id of the place (from the table place) that this NPC is at right now. (You never have to give the place id yourself it will always be chosen based on the place's name)

<sub><sup>Jeroen Himpe -- Introduction to Python -- 2CYB -- Vives Kortrijk</sup></sub>