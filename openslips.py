import os
import webbrowser


def makePDF(data):
    print(data)
    s = f'''
    
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{os.path.abspath('bootstrap.min.css')}">
    <title>CRIMINAL POSTER</title>
</head>
<body onload="window.print()">
    <div id='printablediv'>
    <div class="container text-center my-5 jumbotron">
        <h1>CRIMINAL POSTER</h1>
    </div>
    <div class="container-fluid img-thumbnail">
        <img src="{os.path.abspath('criminals_dir')}/{data[-1]}" height="500px" width=100% />
    </div><br><br>
        <h2 class="my-3 text-center">WANTED CRIMINAL - {data[1]}</h2>
    
    <div class="container-fluid">

            <table class="table table-primary table-hover table-active text-capitalize text-center table-bordered">
                <tr>
                    <th scope="col">NAME</th>
                    <th scope="col">{data[1]}</th>
                </tr>
                <tr>
                    <th scope="col">FATHER-NAME</th>
                    <th scope="col">{data[2]}</th>
                </tr>
                <tr>
                    <th scope="col">MOBILE</th>
                    <tH SCOPE="col">{data[3]}</tH>
                </tr>
                <tr>
                    <th scope="col">E-MAIL</th>
                    <td scope="col">{data[4]}</td>
                </tr>
                <tr>
                    <th scope="col">ADDRESS</th>
                    <td scope="col">{data[5]}</td>
                </tr>

            </table>

    </div>
    </div>
    
    <script>
    
    </script>
    
</body>
</html>'''
    with open('criminal_poster.html', 'w') as file:
        file.write(s)
        file.close()

    path = os.path.abspath('criminal_poster.html')
    webbrowser.register('chrome', None,
                        webbrowser.BackgroundBrowser(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'))
    webbrowser.get('chrome').open_new_tab(path)
