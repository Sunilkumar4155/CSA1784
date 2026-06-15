def generate_blog_html(title, text, link_url, link_text):
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{title}</title>
    </head>
    <body>
        <h1>{title}</h1>
        <p>{text}</p>
        <a href="{link_url}">{link_text}</a>
    </body>
    </html>
    """
    return html

print(generate_blog_html("My First Blog", "Welcome to my tech blog.", "https://wordpress.org", "Visit WordPress"))
