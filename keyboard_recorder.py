import tkinter as tk
import sys

dump_file = sys.argv[1]
my_file = open(dump_file, 'w')
        

def two_keys_generator(key):
    
    # replace - with + if key is not empty.
    key = key.replace('-', '+')
    
    def key_Key(event):
            
        action = str(event.time) + ': ' + key + event.keysym + '\n'
        my_file.write(action)
    return key_Key
    
main = tk.Tk()

# keys that can be held. including the empty string (for when only one key is pressed)
keys = ['', 'Control-', 'Shift-', 'Alt-']
for key in keys:
    main.bind_all('<{}Key>'.format(key), two_keys_generator(key))
    
main.bind_all('<Escape>', lambda x: main.destroy())

main.mainloop() 
my_file.close()
