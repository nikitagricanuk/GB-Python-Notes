def parse_args(args):
    for i in range(0, len(args)):
        if args[i] == "--title":
            note_title = args[i+1]
        elif args[i] == "--msg":
            note_body = args[i+1]
        else:
            print(f"Unknown option: {args[i]}")
    return note_body, note_title