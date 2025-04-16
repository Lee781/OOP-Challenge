from pet import Pet

# Create your pet
my_pet = Pet("Buddy")

# Show starting status
my_pet.get_status()

# Feed, play, and rest
my_pet.eat()
my_pet.play()
my_pet.sleep()

# Teach a bunch of tricks!
tricks_to_learn = [
    "sit",
    "roll over",
    "fetch",
    "shake hands",
    "spin",
    "play dead",
    "stay",
    "come",
    "high five",
    "jump",
    "backflip",
    "dance",
]

# Train Buddy with all the tricks
for trick in tricks_to_learn:
    my_pet.train(trick)

# Show all learned tricks
my_pet.show_tricks()

# Show final status
my_pet.get_status()



