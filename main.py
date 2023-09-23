import sys
import args
import notes
if sys.argv[1] == 'add':
    arg = args.parse_args(sys.argv[2:])
    notes.add_note(arg[1], arg[2])
elif sys.argv[1] == 'del':
    arg = args.parse_args(sys.argv[2:])
    notes.del_note(arg[0], arg[1])
elif sys.argv[1] == 'read':
    arg = args.parse_args(sys.argv[2:])
    notes.read_note(arg[0])
elif sys.argv[1] == 'edit':
    arg = args.parse_args(sys.argv[2:])
    notes.edit_note(arg[0], arg[1])  
else:
    print("Error: Unknown command")
