# Lesson 1

## String
title="Some title"

## Integer
years=80

## Boolean
expert_status=True

print("this is the title " +title)

[print("Expert status = "+str(expert_status))]

## F-string

print(f"Expert status = {expert_status}")

## Multi String

title= """Boss
Lady
Dude"""

## Lists
my_list=["Austin", "Dallas", "San Antonio"]
print(my_list)

## Add/remove element
my_list.append("Houston")
my_list.remove("Dallas")

## Access Element by index
print(my_list[2])

my_list.index["Dallas"]

# LISTS can change and use [] TUPLES are lists that cannot change and use () DICTIONARIES use {}

## Dictionaries "key:value"
actor={"name":"Tom Cruise",
"age":55,
"married":True}

## To find value
print(actor["name"])