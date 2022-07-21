
bl_info = {
    "name" : "Chain Renamer",
    "author": "BlenderBoi",
    "version": (1, 0),
    "blender": (2, 82, 0), 
    "description": "Rename an object parent child chain",
    "warning": "This Addon is No Longer Being Maintained by BlenderBoi, Feel free to Fork this Addon and Maintain it. ",
    "wiki_url": "",
    "category": "Object",
}

import bpy

def renameActive(object, ActiveName="Default", isRenameDataBlock=False, isAdvanced = False, isRenameDataBlockPrefix=True, seperator="_"):
    ParentObject = object
    ParentObject.name = ActiveName
    
    if isRenameDataBlock:
        if bpy.context.mode == "OBJECT":
            if isAdvanced:
                
                if isRenameDataBlockPrefix:
                    ParentObject.data.name = "Data" + seperator + ActiveName
                else:
                    ParentObject.data.name = ActiveName
            


def chainRename(object, CHILDLEVEL=0, SIBLINGSTACK="", LIMITCOUNTER=0, isSiblingPrefix=False, isSiblingGroup=True, sibling_prefix="obj",sibling_prefix_position = "0", chainame = "default", isLimit = False, limit_amt="3", seperator="_", isAdvanced=False, padding=2, start_int=1, isRenameDataBlock="false", isRenameDataBlockPrefix="True", isHasSibling=False): 
    
    #Get Parent Object
    Parent = object
    Parent_Name = object.name
    
    #Get Children List
    Child_List = Parent.children
    
    #Set Current Level
    ChildrenLevel_Current = CHILDLEVEL
    ChildrenLevel_Next = CHILDLEVEL + 1
    
    #Set Sibling Number
    Sibling_Number = 0
    SiblingGroup_Add = ""
    
    #Execute Rename to the child_list
    
    if Child_List:                      #Check if the parent have any child
        for child in Child_List:        #Access each child in child list
            

            #Offset Level Numnber
            ChildrenLevel_Number_Offset = ChildrenLevel_Next + start_int - 1
            
            #Padding Level Number
            ChildrenLevel_Number_Padding = str(ChildrenLevel_Number_Offset).zfill(padding)
            
            Child_Name_Leveled = chainame + seperator + ChildrenLevel_Number_Padding
            
            
            #Check if there are multiple Child
            if len(Child_List) > 1 or isHasSibling == True:
                
                isHasSibling=True
                
                ###Sibling Handling###
                
                #Add Number for each sibling
                Sibling_Number = Sibling_Number+1
                
                #Padding Sibling Number
                Sibling_Number_Padding = str(Sibling_Number+start_int-1).zfill(padding)
                
                

                
                if isAdvanced:
                    
                    if isRenameDataBlock==False:
                        isRenameDataBlockPrefix=False
                    
                    if isSiblingPrefix==True and isSiblingGroup == False:
                    
                            Sibling_Stack_Current = SIBLINGSTACK + sibling_prefix + Sibling_Number_Padding + seperator
                            SiblingGroup_Add = ""
                        
                    else:                        
                        
                        if isSiblingPrefix==False:
                            isSiblingGroup=False
                        else:
                            pass
                        
                            
                        if isSiblingGroup == True:
                            SiblingGroup_Add = sibling_prefix + seperator
                            
                            Sibling_Stack_Current = SIBLINGSTACK + Sibling_Number_Padding + seperator
                        else:
                            SiblingGroup_Add = ""
                            
                            Sibling_Stack_Current = SIBLINGSTACK + Sibling_Number_Padding + seperator
                            
                
  
                else:
                    isSiblingPrefix=False
                    isSiblingGroup=False
                    seperator ="_"
                    sibling_prefix_position = "0"
                    padding=2
                    start_int=1
                    isRenameDataBlock="false"
                    isRenameDataBlockPrefix="false"
                    
                    SiblingGroup_Add = ""
                    
                    Sibling_Stack_Current = SIBLINGSTACK + Sibling_Number_Padding + seperator
                    
 
                
                
                if sibling_prefix_position == "0":
                    if isSiblingGroup==True:
                        Child_Name_Set = Child_Name_Leveled + seperator + SiblingGroup_Add + Sibling_Stack_Current
                        Child_Name_Set = Child_Name_Set[:-1]
                    else:
                        Child_Name_Set = Child_Name_Leveled + seperator + Sibling_Stack_Current
                        Child_Name_Set = Child_Name_Set[:-1]
                
                else:
                    
                    Child_Name_Set = Sibling_Stack_Current + SiblingGroup_Add + Child_Name_Leveled
                
                
                
                
                #Check if Advanced option is on
#                if isAdvanced:
#                    
#                    #If Prefix are off
#                    if isSiblingPrefix == False:
#                        Sibling_Stack_Current = SIBLINGSTACK + Sibling_Number_Padding + seperator
#                        
#                    if isSiblingPrefix == True:
#                        
#                        if isSiblingGroup == True:
#                            Sibling_Stack_Current = SIBLINGSTACK + Sibling_Number_Padding + seperator
#                            
#                        if isSiblingGroup == False:
#                            Sibling_Stack_Current = SIBLINGSTACK + sibling_prefix + seperator + Sibling_Number_Padding + seperator
#                else:
#                    Sibling_Stack_Current = Sibling_Number_Padding + SIBLINGSTACK + seperator
#                    
#                   
#                #Set Final Name
#                
#                #Check Prefix Position         
#                if sibling_prefix_position == "0":
#                    
#                    if isSiblingGroup == True:
#                        Child_Name_Set = Child_Name_Leveled + seperator + sibling_prefix  + Sibling_Stack_Current
#                        
#                    if isSiblingGroup == False:
#                        Child_Name_Set = Child_Name_Leveled  + Sibling_Stack_Current
#                
#                if sibling_prefix_position == "1":
#                    
#                    if isSiblingGroup == True:
#                     
#                        Child_Name_Set = sibling_prefix + seperator+ Sibling_Stack_Current +  Child_Name_Leveled
#                    
#                    if isSiblingGroup == False:
#                        
#                        Child_Name_Set = Sibling_Stack_Current +  Child_Name_Leveled
            
            #If there is only One Child, Skip Sibling Handling
            if isHasSibling == False:
                if len(Child_List) == 1:
                    isHasSibling = False
                    Child_Name_Set = Child_Name_Leveled
                    Sibling_Stack_Current = SIBLINGSTACK
                    
                else:
                    pass
                        
            child.name = Child_Name_Set
            
            if bpy.context.mode == "OBJECT":
                if isAdvanced==True and isRenameDataBlock==True:
                    
                    if isRenameDataBlockPrefix==True:
                        child.data.name = "Data" + seperator + Child_Name_Set
                    else:
                        child.data.name = Child_Name_Set
            else:
                pass
                        

            
            
            #If Limit there is no limit
            if isLimit == False:
#                Sibling_Stack_Current = SIBLINGSTACK
                
                chainRename(CHILDLEVEL=ChildrenLevel_Next, SIBLINGSTACK=Sibling_Stack_Current, isSiblingPrefix=isSiblingPrefix, isSiblingGroup=isSiblingGroup, sibling_prefix=sibling_prefix, sibling_prefix_position=sibling_prefix_position, object = child, chainame=chainame, isLimit=isLimit, limit_amt=limit_amt, seperator=seperator, isAdvanced=isAdvanced, padding=padding, start_int=start_int, isRenameDataBlockPrefix=isRenameDataBlockPrefix, isRenameDataBlock=isRenameDataBlock, isHasSibling=isHasSibling)
            
            elif isLimit == True:
                if LIMITCOUNTER == limit_amt-1:
                    print("Hit the Limit Amout")
                    

                else:
                    Limit_Counter_Next = LIMITCOUNTER+1
                
                    chainRename(CHILDLEVEL=ChildrenLevel_Next, SIBLINGSTACK=Sibling_Stack_Current, LIMITCOUNTER = Limit_Counter_Next, isSiblingPrefix=isSiblingPrefix, isSiblingGroup=isSiblingGroup, sibling_prefix=sibling_prefix, sibling_prefix_position=sibling_prefix_position, object = child, chainame=chainame, isLimit=isLimit, limit_amt=limit_amt, seperator=seperator, isAdvanced=isAdvanced, padding=padding, start_int=start_int, isRenameDataBlockPrefix=isRenameDataBlockPrefix, isRenameDataBlock=isRenameDataBlock, isHasSibling=isHasSibling)
                    
    else:
        print("No Children Found")
                
                     
                     

class OT_Chain_Rename(bpy.types.Operator):
    """Rename your object along the parent chain"""
    bl_idname= "renamer.chain_rename"
    bl_label= "Chain Rename"
    bl_options = {'REGISTER', 'UNDO'}
    
    default_Chain_Name = "Child"
    
    ChainRename_Name : bpy.props.StringProperty(name="", default=default_Chain_Name)
    ChainRename_isRenameActive : bpy.props.BoolProperty(name="Rename Active", default=True)
    
    ChainRename_isAdvanced : bpy.props.BoolProperty(name="Advanced", default=False)
    
    ChainRename_isRenameDataBlock : bpy.props.BoolProperty(name="Rename Datablock", default=False)
    ChainRename_isRenameDataBlockPrefix: bpy.props.BoolProperty(name='"Data" Prefix', default=True)
    
    ChainRename_StartNumber : bpy.props.IntProperty(name="Start from", default=1, min=0, soft_max=5)
    ChainRename_Padding : bpy.props.IntProperty(name="Padding", default=2, min=0, soft_max=5)
    
    ChainRename_isCustomSeperator: bpy.props.BoolProperty(name="Custom", default=False)
    ChainRename_Seperator: bpy.props.StringProperty(name="Seperator", default="_")
    ChainRename_Enum_Seperator: bpy.props.EnumProperty(name="Seperator", default="0", items=(("0", "_", "Underscore"),("1", ".", ".Period."),("2", "-", "Dash"),("3", " ","Space")))
    
    ChainRename_LimitChain : bpy.props.IntProperty(name="", default=3, min=1, soft_max=10)
    ChainRename_isLimit: bpy.props.BoolProperty(name="Limit Chain", default=False)
    
    ChainRename_isSiblingPrefix : bpy.props.BoolProperty(name="Sibling Prefix", default=False)
    ChainRename_isSiblingGroup : bpy.props.BoolProperty(name="Group", default=True)
    ChainRename_Sibling_Prefix_Position: bpy.props.EnumProperty(name="Position", default="0", items=(("1", "Front", "Front"),("0", "Back", "Back"),))
    ChainRename_SiblingPrefix : bpy.props.StringProperty(name="", default="")

    @classmethod
    def poll(cls, context):
        if context.area.type == "VIEW_3D":
            if context.mode == "POSE" or context.mode == "EDIT_ARMATURE" or context.mode == "OBJECT":
                return True
            else:
                return False
            
        elif context.area.type == "OUTLINER":
            return True
        
        else:
            return False

        
    def execute(self, context):
        
        Seperator = "_"
        
        
            
            
        
        if context.mode == "OBJECT":
            if self.ChainRename_isRenameActive:
                renameActive(object = context.active_object, ActiveName=self.ChainRename_Name, isRenameDataBlock=self.ChainRename_isRenameDataBlock, isAdvanced=self.ChainRename_isAdvanced, isRenameDataBlockPrefix=self.ChainRename_isRenameDataBlockPrefix)
            
            
            
            
            if context.active_object:
                if self.ChainRename_isAdvanced:
                    if self.ChainRename_isCustomSeperator:
                        Seperator = self.ChainRename_Seperator
                        
                    else:
                        
                        dict={
                        "0" : "_",
                        "1" : ".",
                        "2" : "-",
                        "3" : " "
                        }
                        Seperator = dict[self.ChainRename_Enum_Seperator]
                        
                chainRename(object = context.active_object, isSiblingPrefix=self.ChainRename_isSiblingPrefix, isSiblingGroup=self.ChainRename_isSiblingGroup, sibling_prefix=self.ChainRename_SiblingPrefix,sibling_prefix_position = self.ChainRename_Sibling_Prefix_Position, chainame = self.ChainRename_Name, isLimit = self.ChainRename_isLimit, limit_amt=self.ChainRename_LimitChain, seperator=Seperator, isAdvanced=self.ChainRename_isAdvanced, padding=self.ChainRename_Padding, start_int=self.ChainRename_StartNumber, isRenameDataBlock = self.ChainRename_isRenameDataBlock, isRenameDataBlockPrefix = self.ChainRename_isRenameDataBlockPrefix)
            
        if context.mode == "POSE" or context.mode == "EDIT_ARMATURE":
            
            if self.ChainRename_isRenameActive:
                renameActive(object=context.active_bone, ActiveName=self.ChainRename_Name, isRenameDataBlock=self.ChainRename_isRenameDataBlock, isAdvanced=self.ChainRename_isAdvanced, seperator=Seperator)
            
            if context.active_bone:
                if self.ChainRename_isAdvanced:
                    if self.ChainRename_isCustomSeperator:
                        Seperator = self.ChainRename_Seperator
                        
                    else:
                        
                        dict={
                        "0" : "_",
                        "1" : ".",
                        "2" : "-",
                        "3" : " "
                        }
                        Seperator = dict[self.ChainRename_Enum_Seperator]
                        
                chainRename(object = context.active_bone, isSiblingPrefix=self.ChainRename_isSiblingPrefix, isSiblingGroup=self.ChainRename_isSiblingGroup, sibling_prefix=self.ChainRename_SiblingPrefix,sibling_prefix_position = self.ChainRename_Sibling_Prefix_Position, chainame = self.ChainRename_Name, isLimit = self.ChainRename_isLimit, limit_amt=self.ChainRename_LimitChain, seperator=Seperator, isAdvanced=self.ChainRename_isAdvanced, padding=self.ChainRename_Padding, start_int=self.ChainRename_StartNumber)
            
        reportmessage = ""
        
        #self.report({"INFO"},reportmessage)
        
        
        return{'FINISHED'}
    
    def draw(self, context):
        
        layout = self.layout
        
        
        
        if context.mode=="OBJECT":
            layout.label(text="Object Name", icon="OBJECT_DATA")
                
        
            
            
        elif context.mode=="POSE" or context.mode=="EDIT_ARMATURE":
            layout.label(text="Bone Name", icon="BONE_DATA")
        else:
            layout.label(text="Name")
            
            
        layout.prop(self,"ChainRename_Name")
        layout.prop(self,"ChainRename_isRenameActive")
    
        
        row=layout.row()
        
        row.prop(self,"ChainRename_isLimit")
        if self.ChainRename_isLimit:
            row.prop(self,"ChainRename_LimitChain")
            
        layout.prop(self,"ChainRename_isAdvanced")
        
        if self.ChainRename_isAdvanced:
            
            box = layout.box()
            
            box.label(text="Options:")
            
            
            if self.ChainRename_isCustomSeperator:
                box.prop(self,"ChainRename_Seperator")
            else:    
                box.prop(self,"ChainRename_Enum_Seperator")
            
            
            box.prop(self,"ChainRename_isCustomSeperator")
            
            box.label(text="Siblings")
            
            
            
        
            row = box.row()
            
            row.prop(self,"ChainRename_isSiblingPrefix")
            if self.ChainRename_isSiblingPrefix:
                row.prop(self,"ChainRename_isSiblingGroup")
                box.prop(self,"ChainRename_SiblingPrefix")
                
                
            box.prop(self,"ChainRename_Sibling_Prefix_Position")
            
            
            box.label(text="Format")
            
            
            row = box.row()
            
            row.prop(self,"ChainRename_StartNumber")
            row.prop(self,"ChainRename_Padding")
            
            
            if context.mode=="OBJECT":
                box = layout.box()
                
                box.label(text="Extra")
                
                row = box.row()
                
                row.prop(self,"ChainRename_isRenameDataBlock")
                
                if self.ChainRename_isRenameDataBlock:
                
                    row.prop(self,"ChainRename_isRenameDataBlockPrefix")

            else:
                pass

            
            
            
            
            
        
        
        
#        box.prop(self,"ChainRename_StartNumber")
#        box.prop(self,"ChainRename_Seperator")
#        layout.prop(self,"ChainRename_Seperator")
#        layout.prop(self,"ChainRename_isRenameActive")
#        layout.prop(self,"ChainRename_isRenameActive")
        


    

#    
#    
#    
#    ChainRename_StartNumber
#    ChainRename_Padding
#    

        
        
    
    def invoke(self, context, event):
        
        if context.mode == "OBJECT":
            if context.active_object:
                self.ChainRename_Name = context.active_object.name
        
        if context.mode == "POSE" or context.mode == "EDIT_ARMATURE":
            if context.active_bone:
                self.ChainRename_Name = context.active_bone.name


        #self.ChainRename_Name = context.active_bone.name

        
        return context.window_manager.invoke_props_dialog(self)


class ChainRename_preferences(bpy.types.AddonPreferences):
    bl_idname= __name__
    
    tabs: bpy.props.EnumProperty(name="Tabs", items = [("INFORMATION", "Info", ""), ("KEYMAPS", "Keymap", "")], default="INFORMATION")
    
    def draw(self, context):
        
        layout = self.layout
        row = layout.row()
        row.prop(self, "tabs", expand=True)
        
        box = layout.box()
        
        if self.tabs == "INFORMATION":
            self.draw_info(context, box)
            
        elif self.tabs == "KEYMAPS":
            self.draw_keymaps(context, box)
        

        
    def draw_info(self, context, layout):
        col = layout.column()
        
        col.label(text= "Chain Renamer can be found in:", icon="INFO")
        col = layout.column()
        
        col.label(text="Object Mode: 3D View > Object > Chain Rename")
        col.label(text="Pose Mode: 3D View > Pose > Chain Rename")
        col.label(text="Edit Armature Mode: 3D View > Armature > Chain Rename")
        col = layout.column()
        
        
        
        col = layout.column()
        
    
    def draw_keymaps(self, context, layout):
        col = layout.column()
        col.label(text="Keymap:")
        col = layout.column()
        
        keymap = context.window_manager.keyconfigs.user.keymaps["3D View"]
        keymap_items = keymap.keymap_items

        col.prop(keymap_items["renamer.chain_rename"], "type", text="Chain Rename", full_event=True)

addon_keymaps =[]



def object_chainrename_menu_draw(self, context):
    self.layout.operator("renamer.chain_rename", text="Chain Rename")
    

classes=[OT_Chain_Rename, ChainRename_preferences]

def register():
    
    for c in classes:
        bpy.utils.register_class(c)
    

    
    bpy.types.VIEW3D_MT_object.append(object_chainrename_menu_draw)
    bpy.types.VIEW3D_MT_edit_armature_names.append(object_chainrename_menu_draw)
    bpy.types.VIEW3D_MT_pose.append(object_chainrename_menu_draw)
    
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name="3D View", space_type="VIEW_3D")
        kmi = km.keymap_items.new("renamer.chain_rename", type="F", value="PRESS", shift=True)
        
        addon_keymaps.append((km, kmi))
    
    
    
    
def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
    
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()    
    


    
    bpy.types.VIEW3D_MT_object.remove(object_chainrename_menu_draw)
    bpy.types.VIEW3D_MT_edit_armature_names.remove(object_chainrename_menu_draw)
    bpy.types.VIEW3D_MT_pose.remove(object_chainrename_menu_draw)
    
    
if __name__ == '__main__':
    register()
