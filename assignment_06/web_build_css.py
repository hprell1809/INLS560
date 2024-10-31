import os  # OS module
import re  # Regular expression module

# This is the slugify function.
# This means that we're creating a a URL-friendly version of a string.
def slugify(title):
    """Convert the page title to a filename-friendly slug."""
    # If statement
    if title.lower() == "home":  # Ensure 'Home' becomes 'index.html'
        return "index.html"
    return re.sub(r'\W+', '-', title.strip().lower()) + ".html"
    # above is a regular expression tha treplaces non-word characters with hyphens!

# Navigation function
# This makes the top nav bar with links.
# It's designed so that if I change the names of the pages, the nav bar will update.
def generate_nav(titles, active_title):
    """Generate a dynamic navigation bar with an active page highlight."""
    nav_links = ""
    # For loop and if statement
    for title in titles:
        filename = slugify(title)  # Method call
        active_class = ' class="active"' if title == active_title else ""
        nav_links += f'\t\t\t<a href="{filename}"{active_class}>{title}</a>\n'
    return nav_links.strip()

# HTML file function
def create_html_file(title, titles, output_dir="build"):
    """Generate and write HTML content based on the page title."""
    filename = slugify(title)  # This means make it URL-friendly.
    nav = generate_nav(titles, active_title=title)  #Method call

    # f-string
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <nav>
            {nav}
        </nav>
        <div class="content">
            <h1>{title}</h1>
            <p>This is the {title.lower()} content.</p>
        </div>
    </body>
    </html>
    """
    #make the directory
    output_path = os.path.join(output_dir, filename)
    os.makedirs(output_dir, exist_ok=True)  # Ensure the directory exists

   # file.write
    with open(output_path, 'w') as file:
        file.write(html_content) #Method call

    # An f-string
    print(f"Created {filename} in the '{output_dir}' directory.")

# CSS file function
def create_css_file(output_dir="build"):
    """Generate and write the style.css file based on a dictionary of styles."""
   # This is a dictionary!
   # I can change the colors and fonts to whatever I want.
   # Currently, it's Carolina branded.
    styles = {
        "font-family": "Calibri",             # font family
        "body-background": "#7BAFD4",     # Background color for .content
        "nav-background": "#13294B",          # Background color for nav
        "nav-a-color": "#4B9CD3",              # Text color for nav links
        "nav-a-active-color": "#ffffff"
    }

    # f-string and dictionary
    css_content = f"""
    * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        font-family: {styles["font-family"]};
    }}

    body {{
        background-color: {styles["body-background"]};
    }}

    nav {{
        background-color: {styles["nav-background"]};
        padding: 10px;
    }}

    nav a {{
        color: {styles["nav-a-color"]};
        margin-right: 10px;
        text-decoration: none;
    }}

    nav a.active {{
        color: {styles["nav-a-active-color"]};
        font-weight: bold;
    }}

    .content {{
        background-color: #F8F8F8;
        padding: 20px;
        margin: 20px;
    }}
    """

    css_path = os.path.join(output_dir, "style.css")
    # Here is the with open() as file alongside file.write:
    with open(css_path, 'w') as file:
        file.write(css_content) # Method call

    print(f"Created style.css in the '{output_dir}' directory.")

# Main function
def main():
    # I can change these to be whatever I want! And the nav function will update.
    # This is the code to name the top nav bar links
    """Main function to generate pages and styles. MUST HAVE HOME!!!"""
    titles = ["Home", "About Us", "Products", "FAQs"]

    # Create HTML files for each title with a for loop
    for title in titles:
        create_html_file(title, titles)

    # Create the style.css file
    create_css_file() 

if __name__ == "__main__":
    main()

