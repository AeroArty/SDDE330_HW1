# SDDE330_HW1

## Assignment - Personal Blog:

Create the classes (with member variables and methods) for Personal Blog. Create all the entity classes as well as helper classes. You only need to provide the class structure and the method signatures. Implementation of the methods is not required. Aside from the code, please provide a class diagram. 

Use cases that must be supported by your design:

- Create Blog
- Read Blog Entry
- Read All Blog Entries
- Update Blog Entry
- Delete Blog Entry 

## Rubric:

- Complete class structure (1 point) (Entity Classes Required, Helper Classes Encouraged)
- Relationships between classes (1 point)
- Appropriate class variables to store the file system details (1 point)
- Appropriate methods signatures in the classes that support the following use cases (2 points)
###  Class Diagram 
#### Structure 
- Clearly shows class names, member variables, and methods. 
#### Relationships 
- Correct representation of inheritance, associations, and dependencies. 
#### Clarity 
- Neat and readable diagram, well-labeled. 

### Code Structure 
#### Access Modifiers 
- Correct use of public, private, and protected modifiers. 
#### Naming Conventions 
- Well-named variables and methods following standard conventions. 
#### Comments 
- Adequate comments explaining classes, variables, and methods


## Class Structure
Class: Blog
- Attributes: entry_list[Blog_Entry], title, subtitle, author, datetime_created, datetime_update, email_contact 
- Methods: get_entry(single or all), add_entry, update_entry, delete_entry

Class Blog_Entry
- Attributes: datetime_created, datetime_updated, title, subtitle, text, blurb, author
- Methods

Class Blog_Metadata
- Attributes: datetime_created, date_time_updated, title, subtitle, blurb, author