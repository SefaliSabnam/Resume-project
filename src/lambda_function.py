import json

def lambda_handler(event, context):
    html_content = """<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>My Resume</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            padding: 20px;
            background-color: #f4f4f4;
        }
        .container {
            max-width: 800px;
            background: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        }
        h1, h2 {
            color: #333;
        }
        .header {
            text-align: center;
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <div class=\"container\">
        <div class=\"header\">
            <h1>Sefali Sharon Sabnam</h1>
            <p> Software Engineer | DevOps Engineer</p>
        </div>

        <div class=\"contact-info\">
            <h2>Contact Information</h2>
            <p>Email: sefali.sabnam26@gmail.com</p>
            <p>Phone: +123 456 7890</p>
            <p>LinkedIn: <a href=\"https://www.linkedin.com/in/sefali-sharon-sabnam-621372187/?trk=opento_sprofile_topcard\" target=\"_blank\">linkedin.com/in/sefali-sharon-sabnam</a></p>
            <p>GitHub: <a href=\"https://github.com/SefaliSabnam\" target=\"_blank\">github.com/SefaliSabnam</a></p>
        </div>
    </div>
</body>
</html>"""
    
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/html"},
        "body": html_content
    }
