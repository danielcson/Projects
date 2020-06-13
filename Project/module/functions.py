#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

import webbrowser

'''
Sets up the pandas dataframe and webbrowser module

'''

task = []
infos = []
dates = []
links = []
desc = []
checklist = {'Item': task, 'Info': infos, 'Date': dates}
saved_links = {'Link': links, 'Description': desc}


def date():
    """Sets up date from datetime to display the current date.
    
    Parameters
    ----------
    datetime : module
    
    Returns
    -------
    Prints the current date as a string.
    """
    
    from datetime import date
    print(date.today())
    

def reminders():
    """Prints the startup prompt. Either the keyword or number will work.
    
    Parameters
    ----------
    
    Returns
    -------
    Prints the available inputs.
    """
    
    # Designed for personal use. Basic rundown of what each keyword does.
    # 'View' is to display checklist dictionary. 'Add' adds to checklist.
    # 'Save' adds to save_links, meant for links. 'Links' displays saved_links.
    # 'Open' will open a specified link from the links list.
    # 'Drop' will delete an entry.
    print('1. View')
    print('2. Add')
    print('3. Save')
    print('4. Links')
    print('5. Open')
    print('6. Drop')


def initial_string(input_string):
    """Sets up the input string so upper/lowercase and spaces do not matter.
    
    Parameters
    ----------
    input_string : string
        The input that the user types in.
    
    Returns
    -------
    out_string : string
        It is input_string that has been lowercased and stripped of spaces.
    
    """
    
    for string in input_string:
        out_string = input_string.lower()
        out_string = out_string.strip()
        
    return out_string
    

def to_do():
    """This is the core function that takes the input and carries out a certain action.
        
        Parameters
        ----------
        msg : string
            The input message
           
        Returns
        -------
        view_msg = pandas dataframe
            Output for the 'view' option that shows the saved items in checklist
        view_links = pandas dataframe
            Output for the 'links' option that shows the saved items in saved_links     
    
    """
    
    # Displays the current date and first input options when to_do is first run only
    date()
    reminders()
    
    # This section was taken from A3. It displays the chat box to type in an input.
    #It then runs the input through initial_string to make input format less strict
    prompt = True
    while prompt:
        msg = input('INPUT :\t')
        msg = initial_string(msg)
        
        # This is the 'view' route. Inputs can be either 'view' or the number next to it in reminders().
        # Similar concept for following blocks.
        if msg == 'view' or msg =='1':
            view_msg = pd.DataFrame(checklist)
            print(view_msg)          
        
        # Asks for item, info, then date sequentially in separate text boxes.
        if msg == 'add' or msg == '2':
            msg_add_item = input('ITEM :\t')
            task.append(msg_add_item) 
            msg_add_info = input('INFO :\t')
            infos.append(msg_add_info) 
            msg_add_date = input('DATE :\t')
            dates.append(msg_add_date)       
       
        # Adds the link to links list, and decription to desc list.
        if msg == 'save' or msg == '3':
            msg_save_link = input('URL :\t')
            links.append(msg_save_link)
            msg_add_desc = input('Note :\t')
            desc.append(msg_add_desc)
        
        # Displays saved_links in the pandas dataframe layout.
        if msg == 'links' or msg == '4':
            view_links = pd.DataFrame(saved_links)
            print(view_links)
            
        if msg == 'open' or msg == '5':    
            msg_open = input('OPEN :\t')
            webbrowser.get()
            
            # When typing the number instead of keyword, the length will be less than 2.
            ## Note: The input is a string, so it must be converted to an int to use on list. 
            if len(msg_open) < 2:
                webbrowser.open_new('http://' + links[int(msg_open)])
            
            # If it is not a number then it will open the link typed in.
            # Concatenated string with 'http://' so users do not have to type that.
            else:
                webbrowser.open_new('http://' + msg_open)
            
        ## Note: .drop() function for pandas does not permantely delete rows.
        # So instead I removed the items directly from the dictionary for each key.
        if msg == 'drop' or msg == '6':
            msg_drop = input('1.Task 2.Links : ')
            
            # Drops entries from saved_links dictionary
            if msg_drop == 'links' or msg_drop == '2' or msg_drop == 'link':
                msg_row = input('ROW :\t')
                msg_row = int(msg_row)
                saved_links['Link'].pop(msg_row)
                saved_links['Description'].pop(msg_row)              
                print(pd.DataFrame(saved_links))
           
            # Drops entries from checklist dictionary
            if msg_drop == 'task' or msg_drop == '1':
                msg_row = input('ROW :\t')
                msg_row = int(msg_row)
                checklist['Item'].pop(msg_row)
                checklist['Info'].pop(msg_row)
                checklist['Date'].pop(msg_row)
                print(pd.DataFrame(checklist))
            
            
                            
            

      

