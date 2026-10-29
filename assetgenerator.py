import maya.cmds as cmds
# create a procedural asset generator that creates an ice cream parfait.
# create a class for the parfait


class Parfait():

    def __init__(self):
        self.glass_size = 1.0
        self.scoop_amount = 2.0
        self.cherry_amount = 3.0
        self.straw_amount = 1.0
    # parameters for parfait will be cup size, amount of scoops, and toppings.
    # get user input for cup size, scoops, flavor, cherries, and straws.

    # create all the assets in one group
    def create(self):
        self.create_glass()
        self.create_scoop()
        self.create_cherry()
        self.create_straw()
        cmds.group([self.glass_obj, self.scoop_obj, self.cherry_obj, self.straw_obj], name="customParfait")
    # create glass cup size function
    # use user input for small or large glass

    def create_glass(self):
        self.glass_obj, self.glass_node = cmds.polyCone(name="glass", height=self.glass_size, radius=0.5)
        cmds.setAttr(f"{self.glass_obj}.translateY", self.glass_size)
        cmds.xform(rotation=[180, 0, 0])
    # create ice cream scoop amount function
    # use user input for scoops (1-5)
    # use user input for ice cream flavor, use different shaders for each flavor

    # create cherry amount function
    # use user input for cherries (0-4)

    # create straw amount function
    # use user input for straw count (0-2)
