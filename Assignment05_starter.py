import os.path
# ------------------------------------------------------------------------ ##
#Title: Assignment 05
#Description: Working with Dictionaries and Files
#             When the program starts, load each "row" of data
#             in "ToDoToDoList.txt" into a python Dictionary.
#             Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# Ali Hajisomo ,2.18.2020,Started script
# <Ali Hajisomo>,<2.23.2020>, Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
filepath = 'ToDoList.txt'
table = []
todos = {}
id = ''
t = []


# -- Processing -- #
# Step 1 - When the program starts, load  any data you have
# in a text file called ToDoList.txt into a python Dictionary.
if os.path.isfile(filepath):
  with open(filepath, 'r') as objFile:
    for line in objFile:
      row = line.split(',')
      todos = {
        'id': row[0],
        'task': row[1],
        'pri': row[2]
      }
      table.append(todos)
else:
  print('creating new file')
  with open(filepath, 'a'): pass

#-- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
  print("""    
      Menu of Options    
      1) Show current data    
      2) Add a new item.    
      3) Remove an existing item.    
      4) Save Data to File    
      5) Exit Program    """)
  option = str(input(' Which option would you like to perfom? '))

# Step 3 - Show the current items in the table
  if option == '1':
    for task in table:
      print(task.get('id'), task.get('task'), task.get('pri').replace('\n',''))

# Step 4 - Add a new item to the list/Table
  elif option == '2':
    id = []
    new_id = ''
    for task in table:
      id.append(task.get('id'))
    task = str(input('task name : '))
    pri  = str(input('task priority : '))
    if todos:
      new_id = int(id[-1]) + 1
    else:
      new_id = 1
    new_task = {'id': new_id, 'task': task, 'pri': pri}
    table.append(new_task)
    t.append(new_task)

  # Step 5 - Remove a new item to the list/Table   
  elif option == '3':
    print('remove', table)
    task_id = str(input('enter task id here : '))
    for task in table:
      if task.get('id') == task_id:
        print('removing')
        table.pop(table.index(task))
# Step 6 - Save tasks to the ToDoToDoList.txt file
  elif option == '4':
    print('save data to file', t)
    for task in t:
      newtask = '\n{},{},{}'.format(task.get('id'), task.get('task'), task.get('pri'))
      with open(filepath, 'a') as file:
        file.write(newtask)    
# Step 6 - Save tasks to the ToDoList.txt file
  elif option == '5':
    break