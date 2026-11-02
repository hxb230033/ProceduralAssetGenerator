import maya.cmds as cmds
# create a procedural asset generator that creates an ice cream parfait.
# create a class for the parfait


class Parfait():

    def __init__(self):
        self.glass_size = 1.0
        self.scoop_amount = 2.0
        self.glass_radius = 0.5
        self.scoop_radius = self.glass_radius
        self.cherry_radius = .1
        self.cherry_amount = 3.0
        self.straw_amount = 2
    # parameters for parfait will be cup size, amount of scoops, and toppings.
    # get user input for cup size, scoops, flavor, cherries, and straws.

    # create all the assets in one group
    def create(self):
        self.create_glass()
        self.create_scoops()
        self.create_cherry()
        self.create_straw()
        cmds.group([self.glass_obj, self.scoop_obj, self.cherry_obj, self.straw_obj], name="customParfait")
    # create glass cup size function
    # use user input for small or large glass


def create_glass(self):
    self.glass_obj, self.glass_node = cmds.polyCone(name="glass", height=self.glass_size, radius=0.5)
    cmds.setAttr(f"{self.glass_obj}.translateY", self.glass_size)
    cmds.xform(rotation=[180, 0, 0])
    cmds.xform(translation=[0, self.glass_size/2, 0])


def create_scoops(self):
    glass_rim = self.glass_size
    scoop_y = glass_rim + self.scoop_radius * 0.5
    scoop_spacing = self.scoop_radius * 1.5 
    self.scoop_obj, self.scoop_node = cmds.polySphere(name="scoop#", radius=self.glass_size/2)
    cmds.xform(translation=[0, scoop_y, 0])
    self.scoops = [self.scoop_obj]

    for i in range(1, self.scoop_amount):
        scoop_multiple = cmds.instance(self.scoop_obj, name="scoop#")[0]
        cmds.xform(scoop_multiple, translation=[0, scoop_y + i * scoop_spacing, 0])
        self.scoops.append(scoop_multiple)
    cmds.group(self.scoops, name="scoops")
    # use user input for scoops (1-5)
    # use user input for ice cream flavor, use different shaders for flavors

    # create cherry amount function
    # use user input for cherries (0-4)


def create_cherries(self):
    pass
    self.cherry_obj, self.cherry_node = cmds.polySphere(name="cherry#", radius=self.cherry_radius)
    cmds.xform(translation=[0, 2, 0])
    self.cherries = [self.cherry_obj]

    for i in range(1, self.cherry_amount):
        cherry_multiple = cmds.instance(self.cherry_obj, name="cherry#")[0]


def create_straws(self):
    self.straw_obj, self.straw_node = cmds.polyCylinder(name="straw#", radius=0.03, height=1.5)
    cmds.xform(translation=[.5, self.glass_size+.5, 0])
    cmds.xform(rotation=[0, 0, -15])

    for i in range(1, self.straw_amount):
        straw_multiple = cmds.instance(self.straw_obj, name="straw#")[0]
        cmds.xform(straw_multiple, rotation=[-10, -10, -10])
        cmds.xform(translation=[.5, self.glass_size+.5, -.1])


# create straw amount function
    # use user input for straw count (0-2)