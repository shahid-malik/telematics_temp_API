BASIC_EMAIL_TEMPLATE = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title></title>
    <style type="text/css">
        @font-face {
            font-family: 'flama-condensed';
            font-weight: 100;
            src: url('http://assets.vervewine.com/fonts/FlamaCond-Medium.eot');
            src: url('http://assets.vervewine.com/fonts/FlamaCond-Medium.eot?#iefix') format('embedded-opentype'),
            url('http://assets.vervewine.com/fonts/FlamaCond-Medium.woff') format('woff'),
            url('http://assets.vervewine.com/fonts/FlamaCond-Medium.ttf') format('truetype');
        }
        @font-face {
            font-family: 'Muli';
            font-weight: 100;
            src: url('http://assets.vervewine.com/fonts/muli-regular.eot');
            src: url('http://assets.vervewine.com/fonts/muli-regular.eot?#iefix') format('embedded-opentype'),
            url('http://assets.vervewine.com/fonts/muli-regular.woff2') format('woff2'),
            url('http://assets.vervewine.com/fonts/muli-regular.woff') format('woff'),
            url('http://assets.vervewine.com/fonts/muli-regular.ttf') format('truetype');
        }
    </style>
</head>
<body style="margin: 0px;padding: 0px;background-color: #e1e5e8">
    <div style="max-width: 520px;margin-left: auto;margin-right: auto;text-align: center;">
        <p style="font-family:'flama-condensed','Arial Narrow',Arial;font-weight:100;font-size:30px;margin: 30px 0px">Telemeatics</p>
    </div>
    <div style="max-width: 520px;margin-left: auto;margin-right: auto;text-align: center">
        <div style="background-color: #ffffff;padding: 20px;clear: both">
            <p class="" style="font-family:'Muli','Arial Narrow',Arial;color:#000000;line-height:24px;font-size:15px;text-align: left;margin: 0px">
                <strong style="vertical-align: top;">Profile Image:</strong>
            <img src="cid:image1" style="width: 100px; height: 80px;">
            </p>
            <p class="" style="font-family:'Muli','Arial Narrow',Arial;color:#000000;line-height:24px;font-size:15px;text-align: left;margin: 0px"><strong>Name:</strong> namevalue </p>
            <p class="" style="font-family:'Muli','Arial Narrow',Arial;color:#000000;line-height:24px;font-size:15px;text-align: left;margin: 0px"><strong>Temperature:</strong> temperaturevalue </p>
            <p class="" style="font-family:'Muli','Arial Narrow',Arial;color:#000000;line-height:24px;font-size:15px;text-align: left;margin: 0px"><strong>Timestamp:</strong> timestamp </p>
        </div>
    </div>
    <div style="max-width: 520px;margin-left: auto;margin-right: auto;text-align: center">
        <div style="margin-top: 30px">
            <p class="" style="font-family:'Muli','Arial Narrow',Arial;color:#a1a8ad;line-height:24px;font-size:15px;">© All rights reserved by Telemeatics</p>
        </div>
    </div>
</body>

</html>
"""


EMAIL_TEXT = """ 
    Hi {}, It has been detected that your temperature is higher than 99C. Current temperature is {}.
    Please consult medical consultant as soon as possible. 
    
    Feel free to call at 44 831 1234567 or email at "help@telematics.com" for help.
    
    Thanks
    Telematics Support
"""
