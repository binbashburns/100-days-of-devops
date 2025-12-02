#!/usr/bin/env python3
"""
Helper script to create new day files with proper template
"""

import os
import sys
from pathlib import Path

def create_day_template(day_number, title):
    """Create a new day file with proper template"""
    
    template = f"""# Day {day_number:03d}: {title}

**Time**: 15 minutes

## Objective
[Describe what you'll accomplish in this challenge]

## Technologies Used
- [List main technologies]

## Steps

1. [Step 1 description]

    ```bash
    # Commands here
    ```

2. [Step 2 description]

    ```bash
    # More commands
    ```

## Key Takeaways
- [Important learning point 1]
- [Important learning point 2]
"""
    
    return template

def main():
    """Main function to create new day file"""
    if len(sys.argv) < 3:
        print("Usage: ./add_day.py <day_number> <title>")
        print("Example: ./add_day.py 68 'Setup CI/CD Pipeline'")
        return
    
    try:
        day_number = int(sys.argv[1])
        title = sys.argv[2]
        
        # Create filename
        filename = f"days/{day_number:03d}.md"
        
        # Check if file already exists
        if Path(filename).exists():
            print(f"Error: File {filename} already exists!")
            return
        
        # Create the file
        content = create_day_template(day_number, title)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Created {filename}")
        print(f"Title: {title}")
        print(f"")
        print(f"Next steps:")
        print(f"   1. Edit {filename} with your solution")
        print(f"   2. Commit changes to update README.md")
        
    except ValueError:
        print("Error: Day number must be an integer")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()