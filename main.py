# Importing the Pet class
from pet import Pet

# Creating an instance of the Pet class for Gigi
gigi = Pet("Gigi")

# Gigi does some activities
gigi.eat()
gigi.sleep()
gigi.play()

# Gigi's status
gigi.get_status()

# Teaching Gigi some tricks
gigi.train("sit")
gigi.train("roll over")
gigi.train("fetch")
gigi.train("shake hands")
gigi.train("spin")

# Showing all tricks Gigi knows
gigi.show_tricks()

# Gigi's status after playing and eating
gigi.play()
gigi.eat()
gigi.get_status()
