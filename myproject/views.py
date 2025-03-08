from django.http import HttpResponse

def portfolio(request):
    html_content = """
    <html>
    <head>
        <title>Name</title>
        <style>
            p {
                color: blue;
                font-size: 20px;
                text-align: center;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <p>My Name Is: Mustafa Musab</p>
    </body>
    </html>
    """
    return HttpResponse(html_content)
