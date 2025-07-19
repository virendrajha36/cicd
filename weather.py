from flask import Flask
import requests

app = Flask(__name__)

@app.route('/', methods =['GET'])
def home():
    construct_url = "https://api.openweathermap.org/data/2.5/weather?q=India&appid=" + "YOUR_API_KEY"
    response = requests.get(construct_url)

    list_of_data = response.json()

    html_data = f"""
    <table border="1">
    <tr>
        <td>country_code</td>
        <td>coordinates</td>
        <td>temp</td>
        <td>pressure</td>
        <td>humidity</td>
    </tr>
    <tr>
        <td>{str(list_of_data['sys']['country'])}</td>
        <td>{str(list_of_data['coord']['lon']) + '  ' 
                    + str(list_of_data['coord']['lat'])}</td>
        <td>{str(list_of_data['main']['temp']) + 'K'}</td>
        <td>{str(list_of_data['main']['pressure'])}</td>
        <td>{str(list_of_data['main']['humidity'])}</td>
    </tr>

</table>
    """
    return html_data

if __name__ == "__main__":
    app.run(host='0.0.0.0')

