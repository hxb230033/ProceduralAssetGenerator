import maya.cmds as cmds

FLAVORS = {
    "vanilla":(0.76, 0.69, 0.63),
    "chocolate":(0.12, 0.07, 0.04),
    "strawberry":(0.66, 0.36, 0.41),
    "cherry":(0.66, 0.12, 0.16),
}

class Parfait():

    def __init__(self):
        self.glass_size = 1.0
        self.scoop_amount  = 2
        self.glass_radius = 0.5
        self.scoop_radius = self.glass_radius
        self.cherry_radius = .1
        self.add_cherry = True
        self.straw_amount = 2
        self.flavor = "chocolate"
        self.grp_name = "customParfait"

    def create(self):
        if cmds.objExists(self.grp_name):
            cmds.delete(self.grp_name)

        self.create_glass()
        self.create_scoops()
        self.create_cherry()
        self.create_straws()
        parts = [self.glass_obj, self.scoops] + self.straws
        if self.add_cherry:
            parts.append(self.cherry_obj)
        cmds.group(parts, name=self.grp_name)

    def create_glass(self):
        self.glass_obj, self.glass_node = cmds.polyCone(name="glass", \
                                        height=self.glass_size, radius=0.5)
        cmds.setAttr(f"{self.glass_obj}.translateY", self.glass_size)
        cmds.xform(self.glass_obj, rotation=[180, 0, 0])
        cmds.xform(self.glass_obj, translation=[0, self.glass_size/2, 0])
        self.glassbtm_obj, self.glassbtm_node = cmds.polyCone \
            (name="glass_btm", height=self.glass_size/2, radius=0.25)
        cmds.xform(self.glassbtm_obj, translation=[0, self.glass_size/4, 0])

    def scoops_flavor(self, flavor):
        shader_name = f"{flavor}_shader"
        shadergrp_name = f"{shader_name}_GRP"
        if cmds.objExists(shadergrp_name):
            return shadergrp_name
        shader = cmds.shadingNode("lambert", asShader=True, name=shader_name)
        cmds.setAttr(f"{shader}.color", *FLAVORS[flavor], type="double3")
        shadergrp = cmds.sets(renderable=True, noSurfaceShader=True, \
                              empty=True, name=shadergrp_name)
        cmds.connectAttr(f"{shader}.outColor", f"{shadergrp}.surfaceShader", \
                          force=True)
        return shadergrp

    def assign_flavor(self, obj, flavor):
        shadergrp = self.scoops_flavor(flavor)
        cmds.sets(obj, edit=True, forceElement=shadergrp)

    def create_scoops(self):
        glass_rim = self.glass_size
        scoop_y = glass_rim + self.scoop_radius * 0.5
        scoop_spacing = self.scoop_radius * 1.5 
        self.scoop_obj, self.scoop_node = cmds.polySphere(name="scoop#", \
                                                    radius=self.scoop_radius)
        cmds.xform(self.scoop_obj, translation=[0, scoop_y, 0])
        self.assign_flavor(self.scoop_obj, self.flavor)
        self.scoops = [self.scoop_obj]
        for i in range(1, self.scoop_amount):
            scoop_multiple = cmds.instance(self.scoop_obj, name="scoop#")[0]
            cmds.xform(scoop_multiple, translation=[0, scoop_y + i * \
                                                    scoop_spacing, 0])
            self.scoops.append(scoop_multiple)
        self.scoops_grp = cmds.group(self.scoops, name="scoops") 

    def finalscoop_ylocation(self):
        final_scoop = self.scoops[-1]
        y_location = cmds.xform(final_scoop, query=True, translation=True, \
                                 worldSpace=True)[1]
        return y_location

    def create_cherry(self):
        if self.add_cherry:
            self.cherry_obj, self.cherry_node = cmds.polySphere(name="cherry",\
                                                     radius=self.cherry_radius)
            self.assign_flavor(self.cherry_obj, "cherry")
            cherry_y = self.finalscoop_ylocation() + self.scoop_radius + \
            self.cherry_radius
            cmds.xform(self.cherry_obj, translation=[0, cherry_y, 0], \
                       worldSpace=True)

    def create_straws(self):
        self.straws = []
        if self.straw_amount < 1:
            return
        self.straw_obj, self.straw_node = cmds.polyCylinder(name="straw#", \
                                                    radius=0.03, height=1.5)
        self.assign_flavor(self.straw_obj, "cherry")
        cmds.xform(self.straw_obj, translation=[.5, self.glass_size+.5, 0], \
                    rotation=[0, 0, -15])
        self.straws = [self.straw_obj]
        for i in range(1, self.straw_amount):
            straw_multiple = cmds.instance(self.straw_obj, name="straw#")[0]
            cmds.xform(straw_multiple, rotation=[-10, -10, -10])
            cmds.xform(straw_multiple, translation=[.5, self.glass_size+.5, \
                                                    -.1 * i])
            self.straws.append(straw_multiple)
