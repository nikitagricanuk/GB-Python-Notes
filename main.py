import sys
import args

note_title = None
note_body = None
if sys.argv[1] == 'add':
    print(args.parse_args(sys.argv[2:]))


