#!/usr/bin/env python
# coding: utf-8

# In[14]:


test_string = 'hElLo   '

def initial_string_test(test_string):
    """Tests the initial_string function on other cases"""
    assert initial_string(test_string) == 'hello'
    assert isinstance(initial_string(test_string), str)
    assert callable(initial_string)
    


# In[21]:


def drop_checklist_test():
    """Tests the drop function to see if the items have been dropped from checklist"""
    counter = len(checklist)
    if msg == 'drop' or msg == '6':
        msg_drop == 'task' or msg_drop == '1'
        assert len(checklist) == counter - 3
        assert isinstance(msg_row, int)


# In[22]:


def drop_saved_links_test():
    """Tests the drop function to see if the items have been dropped from saved_links"""
    counter = len(saved_links)
    if msg == 'drop' or msg == '6':
        msg_drop == 'links' or msg_drop == '2' or msg_drop == 'link'
        assert len(saved_links) == counter - 2
        assert isinstance(msg_row, int)


# In[23]:


def add_test():
    counter_1 = len(task)
    counter_2 = len(infos)
    counter_3 = len(dates)
    if msg == 'add' or msg == '2':
        assert len(task) == counter_1 + 1
        assert len(infos) == counter_2 + 1
        assert len(dates) == counter_3 + 1


# In[24]:


def save_test():
    counter_4 = len(links)
    counter_5 = len(desc)
    if msg == 'save' or msg == '3':
        assert len(links) == counter_4 + 1
        assert len(desc) == counter_5 + 1

