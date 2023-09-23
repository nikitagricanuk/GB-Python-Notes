def parse_args(args):
    for i in range(0, len(args)):
        if args[i] == "--title":
            note_title = args[i+1]
        elif args[i] == "--msg":
            note_body = args[i+1]
        elif args[i] == "--id":
            note_id = args[i+1]   
        else:
            print(f"Unknown option: {args[i]}")
    return note_id, note_title, note_body