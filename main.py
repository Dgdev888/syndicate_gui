from flask import Flask
from flask import request
import pandas as pd
import numpy as np

def html_function(value1, value2, value3):
    if len(value1) == 0 and len(value2) == 0  and len(value3) == 0 :
        return("""<table class="table_center" id="projection results">
            <caption class="caption" style="caption-side:bottom"><br><i>* The general partner commitment and realized return datasets are based on an industry standard 2 percent general partner capital commitment<br>** The carried interest is calculated based on an industry standard 20 percent carry rate<br><br></caption>
            <tr>
                <th class ="table_header"> Deal Count </th>
                <th class ="table_header"> Deal Size </th>
                <th class ="table_header"> Commitment * </th>
                <th class ="table_header"> Setup Fee </th>
                <th class ="table_header"> Total Return </th>
                <th class ="table_header"> Realized Return *</th>
                <th class ="table_header"> Carried Interest **</th>
                <th class ="table_header"> Fund Revenue</th>
            <tr>
                <td class ="table_text"> <span style="font-weight:bold; color: #220061"> #1 </span></td>
                <td class ="table_text"> $ 50,000 </td> 
                <td class ="table_text"> $ 1,000 </td>
                <td class ="table_text"> $ 8,000 </td>
                <td class ="table_text"> 25 % </td>
                <td class ="table_text"> $ 250 </td>
                <td class ="table_text"> $ 2,100 </td>
                <td class ="table_text"> $ 2,350 </td>
            <tr>
                <td class ="table_text"> <span style="font-weight:bold; color: #220061"> #2 </span></td>
                <td class ="table_text"> $ 60,000 </td> 
                <td class ="table_text"> $ 1,200 </td>
                <td class ="table_text"> $ 8,000 </td>
                <td class ="table_text"> 25 % </td>
                <td class ="table_text"> $ 300 </td>
                <td class ="table_text"> $ 2,600 </td>
                <td class ="table_text"> $ 2,900 </td>
            <tr>
                <td class ="table_text"> <span style="font-weight:bold; color: #220061"> #3 </span></td>
                <td class ="table_text"> $ 72,000 </td> 
                <td class ="table_text"> $ 1,440 </td>
                <td class ="table_text"> $ 8,000 </td>
                <td class ="table_text"> 25 % </td>
                <td class ="table_text"> $ 360 </td>
                <td class ="table_text"> $ 3,200 </td>
                <td class ="table_text"> $ 3,560 </td>
            <tr>
                <td class ="table_text"> <span style="font-weight:bold; color: #220061"> #4 </span></td>
                <td class ="table_text"> $ 86,399 </td> 
                <td class ="table_text"> $ 1,727 </td>
                <td class ="table_text"> $ 8,000 </td>
                <td class ="table_text"> 25 % </td>
                <td class ="table_text"> $ 431 </td>
                <td class ="table_text"> $ 3,919 </td>
                <td class ="table_text"> $ 4,351 </td>
            <tr>
                <td class ="table_text"> <span style="font-weight:bold; color: #220061"> #5 </span></td>
                <td class ="table_text"> $ 103,680 </td> 
                <td class ="table_text"> $ 2,073 </td>
                <td class ="table_text"> $ 8,000 </td>
                <td class ="table_text"> 25 % </td>
                <td class ="table_text"> $ 518 </td>
                <td class ="table_text"> $ 4,784 </td>
                <td class ="table_text"> $ 5,302 </td>
            <tr>
                <td class ="table_text"> <span style="font-weight:bold; color: #220061"> #6 </span></td>
                <td class ="table_text"> $ 124,415 </td> 
                <td class ="table_text"> $ 2,488 </td>
                <td class ="table_text"> $ 8,000 </td>
                <td class ="table_text"> 25 % </td>
                <td class ="table_text"> $ 622 </td>
                <td class ="table_text"> $ 5,820 </td>
                <td class ="table_text"> $ 6,442 </td>
            <tr>
                <td class ="table_text"> <span style="font-weight:bold; color: #220061"> #7 </span></td>
                <td class ="table_text"> $ 149,299 </td> 
                <td class ="table_text"> $ 2,985 </td>
                <td class ="table_text"> $ 8,000 </td>
                <td class ="table_text"> 25 % </td>
                <td class ="table_text"> $ 746 </td>
                <td class ="table_text"> $ 7,064 </td>
                <td class ="table_text"> $ 7,811 </td>
            <tr>
                <td class ="table_text"> <span style="font-weight:bold; color: #220061"> #8 </span></td>
                <td class ="table_text"> $ 179,159 </td> 
                <td class ="table_text"> $ 3,583 </td>
                <td class ="table_text"> $ 8,000 </td>
                <td class ="table_text"> 25 % </td>
                <td class ="table_text"> $ 895 </td>
                <td class ="table_text"> $ 8,557 </td>
                <td class ="table_text"> $ 9,453 </td>
            <tr>
                <td class ="table_text"> <span style="font-weight:bold; color: #220061"> #9 </span></td>
                <td class ="table_text"> $ 214,990 </td> 
                <td class ="table_text"> $ 4,299 </td>
                <td class ="table_text"> $ 8,000 </td>
                <td class ="table_text"> 25 % </td>
                <td class ="table_text"> $ 1,074 </td>
                <td class ="table_text"> $ 10,349 </td>
                <td class ="table_text"> $ 11,424 </td>
            <tr>
                <td class ="table_text"> <span style="font-weight:bold; color: #220061"> #10 </span></td>
                <td class ="table_text"> $ 257,989 </td> 
                <td class ="table_text"> $ 5,159 </td>
                <td class ="table_text"> $ 8,000 </td>
                <td class ="table_text"> 25 % </td>
                <td class ="table_text"> $ 1,289 </td>
                <td class ="table_text"> $ 12,499 </td>
                <td class ="table_text"> $ 13,789 </td>

            </tr>
            </div>

            </body>
            """)
    else:
        first_check = int(value1.replace(",", ""))
        check_increase = float(value2)
        total_return = float(value3)

        data = [["Deal Count", "Deal Size", "Setup Fee","Total Return"]]

        for i in range(1, 10 + 1):
            data.append([i,first_check,8000,total_return/100])


        df = pd.DataFrame(data[1:],columns=data[0])
        df['Deal Size'] = df['Deal Size'] * ((1 + check_increase/100) ** np.arange(len(df)))
        df['Commitment'] = df['Deal Size'] * 0.02
        df['Invested'] = df["Deal Size"] - df["Setup Fee"]
        df['RGL Total'] = df['Invested'] * df['Total Return']
        df['Realized Return'] = df['Commitment'] * df["Total Return"]
        df['Carry Calc'] = df['RGL Total'] * 0.20
        df.loc[df['Carry Calc'] <= 0, 'Carried Interest'] = 0 
        df.loc[df['Carry Calc'] > 0, 'Carried Interest'] = df['Carry Calc']
        df = df.drop(columns=["Invested","RGL Total","Carry Calc"])
        df['Fund Revenue'] = df["Realized Return"] + df["Carried Interest"]
        df = df[["Deal Count", "Deal Size", "Commitment", "Setup Fee", "Total Return", "Realized Return", "Carried Interest", "Fund Revenue"]]
        df = df.astype({"Deal Size": int, "Commitment": int, "Realized Return": int, "Carried Interest": int, "Fund Revenue": int})

        return (f"""<table class="table_center" id="projection results">
                    <caption class="caption" style="caption-side:bottom"><br><i>* The realized gain is based on an industry standard 2 percent general partner capital commitment<br>** The carried interest is calculated based on an industry standard 20 percent rate<br><br></caption>
                    <tr>
                        <th class ="table_header"> Deal Count </th>
                        <th class ="table_header"> Deal Size </th>
                        <th class ="table_header"> Commitment * </th>
                        <th class ="table_header"> Setup Fee </th>
                        <th class ="table_header"> Total Return </th>
                        <th class ="table_header"> Realized Return *</th>
                        <th class ="table_header"> Carried Interest **</th>
                        <th class ="table_header"> Fund Revenue</th>
                    <tr>
                        <td class ="table_text"> <span style="font-weight:bold; color: #220061"> #1 </span></td>
                        <td class ="table_text"> $ {'{:,}'.format(df['Deal Size'][0])} </td> 
                        <td class ="table_text"> $ {'{:,}'.format(df['Commitment'][0])} </td> 
                        <td class ="table_text"> $ {'{:,}'.format(df['Setup Fee'][0])} </td>
                        <td class ="table_text"> {'{:,}'.format(round(df['Total Return'][0]*100,2))} %</td>
                        <td class ="table_text"> $ {'{:,}'.format(df['Realized Return'][0])} </td>
                        <td class ="table_text"> $ {'{:,}'.format(df['Carried Interest'][0])} </td>
                        <td class ="table_text"> $ {'{:,}'.format(df['Fund Revenue'][0])} </td>
                    <tr>
                        <td class ="table_text"> <span style="font-weight:bold; color: #220061"> #2 </span></td>
                        <td class ="table_text"> $ {'{:,}'.format(df['Deal Size'][1])} </td> 
                        <td class ="table_text"> $ {'{:,}'.format(df['Commitment'][1])} </td> 
                        <td class ="table_text"> $ {'{:,}'.format(df['Setup Fee'][1])} </td>
                        <td class ="table_text"> {'{:,}'.format(round(df['Total Return'][1]*100,2))} %</td>
                        <td class ="table_text"> $ {'{:,}'.format(df['Realized Return'][1])} </td>
                        <td class ="table_text"> $ {'{:,}'.format(df['Carried Interest'][1])} </td>
                        <td class ="table_text"> $ {'{:,}'.format(df['Fund Revenue'][1])} </td>
                    <tr>
                        <td class ="table_text"> <span style="font-weight:bold; color: #220061"> #3 </span></td>
                        <td class ="table_text"> $ {'{:,}'.format(df['Deal Size'][2])} </td> 
                        <td class ="table_text"> $ {'{:,}'.format(df['Commitment'][2])} </td> 
                        <td class ="table_text"> $ {'{:,}'.format(df['Setup Fee'][2])} </td>
                        <td class ="table_text"> {'{:,}'.format(round(df['Total Return'][2]*100,2))} %</td>
                        <td class ="table_text"> $ {'{:,}'.format(df['Realized Return'][2])} </td>
                        <td class ="table_text"> $ {'{:,}'.format(df['Carried Interest'][2])} </td>
                        <td class ="table_text"> $ {'{:,}'.format(df['Fund Revenue'][2])} </td>
                    <tr>
                        <td class ="table_text"> <span style="font-weight:bold; color: #220061"> #4 </span></td>
                        <td class ="table_text"> $ {'{:,}'.format(df['Deal Size'][3])} </td> 
                        <td class ="table_text"> $ {'{:,}'.format(df['Commitment'][3])} </td> 
                        <td class ="table_text"> $ {'{:,}'.format(df['Setup Fee'][3])} </td>
                        <td class ="table_text"> {'{:,}'.format(round(df['Total Return'][3]*100,2))} %</td>
                        <td class ="table_text"> $ {'{:,}'.format(df['Realized Return'][3])} </td>
                        <td class ="table_text"> $ {'{:,}'.format(df['Carried Interest'][3])} </td>
                        <td class ="table_text"> $ {'{:,}'.format(df['Fund Revenue'][3])} </td>
                    <tr>
                        <td class ="table_text"> <span style="font-weight:bold; color: #220061"> #5 </span></td>
                        <td class ="table_text"> $ {'{:,}'.format(df['Deal Size'][4])} </td> 
                        <td class ="table_text"> $ {'{:,}'.format(df['Commitment'][4])} </td> 
                        <td class ="table_text"> $ {'{:,}'.format(df['Setup Fee'][4])} </td>
                        <td class ="table_text"> {'{:,}'.format(round(df['Total Return'][4]*100,2))} % </td>
                        <td class ="table_text"> $ {'{:,}'.format(df['Realized Return'][4])} </td>
                        <td class ="table_text"> $ {'{:,}'.format(df['Carried Interest'][4])} </td>
                        <td class ="table_text"> $ {'{:,}'.format(df['Fund Revenue'][4])} </td>
                    <tr>
                        <td class ="table_text"> <span style="font-weight:bold; color: #220061"> #6 </span></td>
                        <td class ="table_text"> $ {'{:,}'.format(df['Deal Size'][5])} </td> 
                        <td class ="table_text"> $ {'{:,}'.format(df['Commitment'][5])} </td> 
                        <td class ="table_text"> $ {'{:,}'.format(df['Setup Fee'][5])} </td>
                        <td class ="table_text"> {'{:,}'.format(round(df['Total Return'][5]*100,2))} %</td>
                        <td class ="table_text"> $ {'{:,}'.format(df['Realized Return'][5])} </td>
                        <td class ="table_text"> $ {'{:,}'.format(df['Carried Interest'][5])} </td>
                        <td class ="table_text"> $ {'{:,}'.format(df['Fund Revenue'][5])} </td>
                    <tr>
                        <td class ="table_text"> <span style="font-weight:bold; color: #220061"> #7 </span></td>
                        <td class ="table_text"> $ {'{:,}'.format(df['Deal Size'][6])} </td> 
                        <td class ="table_text"> $ {'{:,}'.format(df['Commitment'][6])} </td> 
                        <td class ="table_text"> $ {'{:,}'.format(df['Setup Fee'][6])} </td>
                        <td class ="table_text"> {'{:,}'.format(round(df['Total Return'][6]*100,2))} %</td>
                        <td class ="table_text"> $ {'{:,}'.format(df['Realized Return'][6])} </td>
                        <td class ="table_text"> $ {'{:,}'.format(df['Carried Interest'][6])} </td>
                        <td class ="table_text"> $ {'{:,}'.format(df['Fund Revenue'][6])} </td>
                    <tr>
                        <td class ="table_text"> <span style="font-weight:bold; color: #220061"> #8 </span></td>
                        <td class ="table_text"> $ {'{:,}'.format(df['Deal Size'][7])} </td> 
                        <td class ="table_text"> $ {'{:,}'.format(df['Commitment'][7])} </td> 
                        <td class ="table_text"> $ {'{:,}'.format(df['Setup Fee'][7])} </td>
                        <td class ="table_text"> {'{:,}'.format(round(df['Total Return'][7]*100,2))} %</td>
                        <td class ="table_text"> $ {'{:,}'.format(df['Realized Return'][7])} </td>
                        <td class ="table_text"> $ {'{:,}'.format(df['Carried Interest'][7])} </td>
                        <td class ="table_text"> $ {'{:,}'.format(df['Fund Revenue'][7])} </td>
                    <tr>
                        <td class ="table_text"> <span style="font-weight:bold; color: #220061"> #9 </span></td>
                        <td class ="table_text"> $ {'{:,}'.format(df['Deal Size'][8])} </td> 
                        <td class ="table_text"> $ {'{:,}'.format(df['Commitment'][8])} </td> 
                        <td class ="table_text"> $ {'{:,}'.format(df['Setup Fee'][8])} </td>
                        <td class ="table_text"> {'{:,}'.format(round(df['Total Return'][8]*100,2))} %</td>
                        <td class ="table_text"> $ {'{:,}'.format(df['Realized Return'][8])} </td>
                        <td class ="table_text"> $ {'{:,}'.format(df['Carried Interest'][8])} </td>
                        <td class ="table_text"> $ {'{:,}'.format(df['Fund Revenue'][8])} </td>
                    <tr>
                        <td class ="table_text"> <span style="font-weight:bold; color: #220061"> #10 </span></td>
                        <td class ="table_text"> $ {'{:,}'.format(df['Deal Size'][9])} </td> 
                        <td class ="table_text"> $ {'{:,}'.format(df['Commitment'][9])} </td> 
                        <td class ="table_text"> $ {'{:,}'.format(df['Setup Fee'][9])} </td>
                        <td class ="table_text"> {'{:,}'.format(round(df['Total Return'][9]*100,2))} %</td>
                        <td class ="table_text"> $ {'{:,}'.format(df['Realized Return'][9])} </td>
                        <td class ="table_text"> $ {'{:,}'.format(df['Carried Interest'][9])} </td>
                        <td class ="table_text"> $ {'{:,}'.format(df['Fund Revenue'][9])} </td>
                        </tr>
                        </div>
                        </body>
                        """)

app = Flask(__name__)

@app.route("/")
def index():

    user_input1 = request.args.get("deal size", "")
    user_input2 = request.args.get("deal increase", "")
    user_input3 = request.args.get("average return", "")

    ending_html = html_function(user_input1, user_input2, user_input3)

    return (
        """
            <head>
            <title> Syndicate Revenue Calculator </title>
            <style>
            body {margin:0;}
            
            .navbar {
                overflow: hidden; 
                background-color: #FFF; 
                position: sticky; 
                box-shadow: 0 2px 4px 0 rgba(0,0,0,.2); 
                top: 0; width: 100%;}

            .navbar a {
                float: left; 
                display: block; 
                color: #220061; 
                text-align: center; 
                padding: 24px 40px; 
                text-decoration: none; 
                font-size: 25px; 
                font-family: 
                Foundersgrotesk, sans-serif;}

            .main {
                padding: 10px; 
                margin-top: 0px; 
                height: auto; 
                background-color: #eef0ff;}

            .main_header {
                color: #220061; 
                font-size: 48px; 
                font-family: Foundersgrotesk,sans-serif; 
                text-align: center;}

            .sub_header {
                color: #220061; 
                font-size: 24px; 
                font-family: Foundersgrotesk,sans-serif; 
                text-align: center;}

            .body_text {
                color: #162040; 
                font-size: 16px; 
                font-family: Foundersgrotesk,sans-serif; 
                text-align: center;
                padding: 0px;
                padding-right: 300px;
                padding-left: 300px;}

            .table_center {
                text-align: center; 
                margin-left: auto; 
                margin-right: auto;}

            .table_header {
                border: 0px solid grey; 
                border-collapse: collapse; 
                background-color: #FFF; 
                padding: 15px; 
                color: #220061; 
                font-family: Foundersgrotesk,sans-serif; 
                text-align: center; 
                margin-left: auto; 
                margin-right: auto;}

             .table_text {
                border: 0px solid grey; 
                border-collapse: collapse; 
                background-color: #FFF; 
                padding: 15px; color: #220061;
                font-family: Foundersgrotesk,sans-serif; 
                text-align: center; 
                margin-left: auto; 
                margin-right: auto; 
                font-weight:lighter;}

            .caption {
                color: #162040; 
                font-size: 13px; 
                font-family: Foundersgrotesk,sans-serif; 
                text-align: left;
                padding: 0px;
                padding-right: 15px;
                padding-left: 15px;}

            div.form {
                display: block;
                text-align: center;}
            
            form {
                display: inline-block;
                margin-left: auto;
                margin-right: auto;
                text-align: center;}

            input[type=number] {
                padding: 5px 10px;
                margin: 5px 0;
                box-sizing: border-box;}

            </style>
            </head>
            
            <div class="navbar">
            <a href="https://www.angellist.com"> <img src="https://assets-global.website-files.com/5f34db2422dcee712f853aa0/5f467e0c9b972682d89af60e_AngelList%20Venture.svg" width="178" height="24" alt="company logo"> </a>
            </div>

            <div class="main">
            <h1 class ="main_header"> Syndication Revenue Calculator</h1>
            <p class ="body_text">
                The syndication revenue calculator was designed to assist fund managers in understanding 
                how individual deal performance affects future revenue. These projections should be used for 
                eductional purposes only and not serve as any investment advice. Please enter only whole numbers, decimals and symbols are
                currently not supported at this time. Designed by <a href="https://www.linkedin.com/in/danielgruppo/">Daniel Gruppo.</a><br><br></p>

            <div class="form">
                <form action="" method="get">
                            <input type="text" style="font-size:10pt; width: 275px; height: 35px; font-family: Foundersgrotesk,sans-serif; color: #162040;" name="deal size" placeholder="First Deal Size (Ex: 50000)">
                            <input type="text" style="font-size:10pt; width: 275px; height: 35px; font-family: Foundersgrotesk,sans-serif; color: #162040;" name="deal increase" placeholder="Average Deal % Increase (Ex: 20)">
                            <input type="text" style="font-size:10pt; width: 275px; height: 35px; font-family: Foundersgrotesk,sans-serif; color: #162040;" name="average return" placeholder="Average Total Return % (Ex: 25)">
                            <br><br><input type="submit" style="font-size:16pt;" value="Calculate Results"><br>
                </form>
            </div>
            """
            + ending_html)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)

