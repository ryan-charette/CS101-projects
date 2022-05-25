#In this project, you’ll use Git to keep track of meal guidelines for animals at the Manhattan Zoo.
pwd
cd Desktop/'Computer Science'
git clone https://github.com/ryan-charette/CS101-projects
cd CS101-projects
mkdir basic_git_workflow
cd basic_git_workflow
mkdir manhattan_zoo
cd manhattan_zoo
touch meal-regimens.txt
sudo echo -e "Manhattan Zoo
Zookeeper Intern Onboarding:
Meal Guidelines

1. California Sea Lions
Meal: 40 lbs. salmon, 40 lbs. herring, 20 lbs. Northern Anchovy, 20 lbs. Octupus
Times: 6:00 am, 9:00 am, 12:00 pm, 3:00 pm, 6:00 pm, 9:00 pm
Directions: Leave buckets for trainer at 12:00 pm and 3:00 pm, otherwise, follow standard protocol.

2. Ring-tailed Lemurs
Meal: 10 bags Tamarind pods
Times: 6:00 am, 3:00 pm, 8:00 pm
Directions: Empty bags over meadow area during designated times
" >> meal-regimens.txt
git status
git add meal-regimens.txt
git commit -m "Create meal-regimens.txt"
sudo echo -e "3. Long-Tailed Chinchillas
Meal: 1 bag animal pellets, 1 bag dried fruit, 1/2 bag cashews, 5 carrots, 3 stalks kale
Times: 8:00 am
Directions: disperse contents throughout Chinchilla habitat
" >> meal-regimens.txt
git add meal-regimens.txt
git status
git commit -m "Add Chinchilla meal regimen"
git log
sudo echo -e "4. Poison Dart Frogs
Meal: 1 bag small crickets
Times: 6:00 am
Directions: empty bag in frog habitat once daily. Do not touch frogs! Extremely poisonous.
 
5. Western Lowland Gorilla
Meal: (Morning) 20 lbs. kale, 10 lbs. celery, 10 lbs. green beans, 5 lbs. carrots, 1 bag sweet potatoes. (Evening) 10 Bananas, 10 apples, 5 oranges, 5 mango, 20 lbs. grapes, 10 lbs. turnips, 5 lbs. white potatoes
Times: 6:30 am, 12:00 pm, 7:00 pm
Directions: feed Gorillas in the morning as group, spread forage items during noon meal, and divide quantities for individual feeding in evening
" >> meal-regimens.txt
git add meal-regimens.txt
git commit -m "Add Frog and Gorilla meal regimen"
git push origin main
