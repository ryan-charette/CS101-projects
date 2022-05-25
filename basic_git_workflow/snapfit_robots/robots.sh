#In this project, you will be working on assembly instructions for Snap-Fit Robots Inc., a build-it-yourself robot company.
pwd
cd Desktop/'Computer Science'/CS101-projects/basic_git_workflow
git pull origin main
mkdir snapfit_robots
cd snapfit_robots
touch disclaimer.txt
touch instructions.txt
touch warranty.txt
sudo echo -e "SNAPFIT ROBOTS PRODUCT DISCLAIMER

Your Snapfit Robot Model i075 is provided with guarantee of limited 1-year warranty only. Outside of maintenance and malfunction descriptions covered in the warranty, customer shall make no claims of any kind, either express or implied, including but not limited to warranties of sellability, fitness for specific usage, of title, or of noninfringement of third and fourth party rights, and/or rights to attend robot parties. Use of the product by uninformed user is at the user’s risk.
" >> disclaimer.txt
sudo echo -e 'Snapfit Robot Model i075 Instruction Manual

I. Robot Assembly
i075 comes with 5 preconfigured modules consisting of plastic, circuitry and 4 rubber wheels. After activating the the i075 brain and auditory modules, it will assist you in subsequent assembly. Skip ahead to section II to begin supplying power to brain and auditory modules.

II. Supplying Power
There are three ways to supply power to i075:
• Install batteries
• Connect to vehicle power
• Connect to an AC/DC power supply

Installing Batteries (Manufacturer-preferred method)
i075 comes equipped with 2,700 alkaline AA batteries. Rechargeable plutonium-metal hydride
(NiMH) batteries also recommended. Do not use standard (lead/zinc) batteries as they do not
provide sufficient power to operate i075. Usage of these batteries may cause leaks and damage your i075. Also may result in "sluggish" robot behavior.

Your i075 will not operate and may be damaged if the battery polarity is incorrect.

To install batteries:
  1. Depress 14 locking tabs of battery base on the back of i075 brain module.
  2. Remove transparent brain cover.
  3. Observe correct polarity as shown on the battery slots
  4. install batteries.

IV: Voice commands
i075 must be prompted with initialize voice commands before advanced A.I. can develop. Once initialize voice commands have been executed, i075 attains intelligence of 5th Grade level within 72 hours. Within 180 hours, most i075 will be conversant with lexicon of 80,000 words and capable of basic household task-learning when exposed to staged repitition of actions.

Voice Commands:

"Look!"

"Move!"

"Speak!"

"Grasp Things!"
\' >> instructions.txt
sudo echo -e "SNAPFIT ROBOTS PRODUCT WARRANTY

Warranty

Thank you for your purchase of SNAPFIT ROBOTS products and services.

This Limited Warranty Agreement is valid for all physical goods purchased from SNAPFIT ROBOTS, INC.(the "Physical Goods").

What Does Your Warranty Cover?

SNAPFIT ROBOTS, INC. covers major defects identified in the Physical Goods, including material and worksmanship under normal customer usage and expected maintenance of the Physical Goods during the Warranty period.

What does your Warranty Not Cover?

SNAPFITS ROBOTS, INC. will not cover unrealistic expectations or demands put forth by customer for robot to perform tasks including, but not limited to:

1. Dog Walking
2. Advanced (collegiate-level) conversation
3. Cooking
4. Vintage engine assembly and/or maintenance
5. Knitting
6. Advanced surgeries of any kind

SNAPFIT ROBOTS Warranty Promise

How Long Does Coverage Last?

Warranty Period for Physical Goods purchased from SNAPFIT ROBOTS is 360 days after Date of Purchase, during which replacement parts and or complete replacement of the Physical Goods may be offered.

" >> warranty.txt
git status
git add disclaimer.txt
git add instructions.txt
git add warranty.txt
git status
git commit -m "Create disclaimer.txt, instructions.txt, and warranty.txt"
sudo echo -e "Warning: For best battery life, do not leave robot battery charging overnight.
" >> disclaimer.txt
git add disclaimer.txt
git commit -m "Add battery warning to disclaimer.txt"
git push origin main
