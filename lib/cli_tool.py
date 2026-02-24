import argparse


# TODO: Define the add_task function
# This function should accept 'args' and print: ✅ Task added: <description>
def add_task(args):
    print(f"✅ Task added: {args.description}")

# TODO: Define the list_tasks function
# This function should accept 'args' and print: 📋 Listing all tasks...
def list_tasks(args):
    print(f"📋 Listing all tasks...")

# TODO: Define the main() function
def main():
    # - Create an ArgumentParser with a helpful description
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers()
    
    
# - Add subparsers for "add" and "list" commands

#add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", nargs="+", help="Description of the task")
    add_parser.set_defaults(func=add_task)
    
#list command
    list_parser = subparsers.add_parser("list", help="List of all tasks")
    list_parser.set_defaults(func=list_tasks)
    
    
# - Parse the arguments and call the appropriate handler (if exists)
    args = parser.parse_args()
    
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()
    
