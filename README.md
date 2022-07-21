# Chain-Renamer

## IMPORTANT: 

This Addon is No Longer Being Maintained By Me, You Are Free to Fork, Maintain, or Contribute to this. 

## About Chain Renamer

This Add-on is a simple renaming tool that helps you to organize your scene by renaming your object or bones. It renames all the child of the active object. Chain rename 1.0 can help you save time by name all the child object numbered in a very neat manner. 

![image_processing20200619-4-10a4yf1](https://user-images.githubusercontent.com/79613445/180131953-c67c32cc-4ace-4beb-9923-6219f64544ff.jpeg)

Chain Renamer 1.0 is designed to be simple, and easy to use, instead of setting up some complicated naming system, this is a simple tool that you use like a helper. While this add-on is designed for, and works best with Single chain Hierarchy (one child all the way down). But it works for multiple child as well.

![uploads_1588264148597-Chain+Rename+Screenshot](https://user-images.githubusercontent.com/79613445/180131916-e8d82343-4810-4682-81a7-9d6b24c74b93.png)

It is best used for renaming things like branches, fingers, hairs and tail. 

## Features:

Rename all children of an object or bone in the scene.


## How to use:

Press SHIFT-F and put in the name you want to rename

Alternately, you can find the operator in:

Object Mode
View 3D -> Object -> Chain Rename

Pose Mode
View 3D -> Pose -> Chain Rename

Armature Edit Mode = View 3D -> Armature -> Chain Rename


# Chain Renamer Documentation

To use Chain renamer, first select the parent of the child you want to rename, make sure that it is an active object, and press Shift F to activate the tool. 

You can also find Chain Renamer in:

## Object Mode

View 3D -> Object -> Chain Rename

## Pose Mode

View 3D -> Pose -> Chain Rename

## Armature Edit Mode

View 3D -> Armature -> Chain Rename

When Chain Renamer is executed, it will check if the parent have more than one child. If the Child have sibling, extra numbers will be attached to the name to avoid conflicting name. 

Example Result if Parent only have one direct child.

Bone_Tail

      Bone_Tail01

             Bone_Tail02

                    Bone_Tail03

Example Result if Parent have multiple direct child. 

Bone_Branch

         01_Bone_Branch_01

                         01_01_Bone_Branch_02

                         02_01_Bone_Branch_02

         02_Bone_Branch_01

                         01_02_Bone_Branch_02

                         02_02_Bone_Branch_02

## Options:

### Rename Active

Check this if you want to rename the parent or the active object. 


### Limit Chain

Limit how many "levels" or "generation" of children that will be renamed. 


### Seperator

Something to put in between the name. Options are _underscore, .period, -dash and  empty space. 

You can use Custom Separator by checking the Custom Checkbox and input the Separator desired. 


### Sibling Prefix

If Sibling is present, add a prefix to the sibling number. 


### Group

Only add the sibling prefix once instead of adding to evert sibling number. 


### Position

The position of the Sibling Number and Sibling Prefix, whether before the base name, or at the end of the name. 


### Start From

Choose what number to start from. 


### Padding

Pad the number, think of it as how many 0 you want to include in the number. 
