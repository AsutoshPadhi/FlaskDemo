from flask import Flask, render_template, request

''' Define an instance of the flask app'''
app = Flask(__name__)

'''
    app.route is used for routing in flask
    '/' means index page
    any forms or links should contain /something instead of direct links
'''
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def login():
    return render_template('login.html')

'''
    This method is going to access data from a form that was in the previous page
    request.args['name_of_the_input_field'] is the syntax
'''
@app.route('/home', methods=['GET','POST'])
def home():
    '''Get the username and password from the login page'''
    username = request.args['username']
    password = request.args['password']

    '''Define a dictionary which gives information related to the username'''
    info = {
        "Pikachu":
            {
                "password": "electric",
                "data": "It evolves from Pichu when leveled up with high friendship and evolves into Raichu when exposed to a Thunder Stone. However, the starter Pikachu in Pokémon Yellow will refuse to evolve into Raichu unless it is traded and evolved on another save file. "
            },
        "Charizard":
            {
                "password": "fire",
                "data": "Charizard is a dual-type Fire/Flying Pokémon introduced in Generation I. It evolves from Charmeleon starting at level 36. It is the final form of Charmander. It can Mega Evolve into two forms: Mega Charizard X using Charizardite X and Mega Charizard Y using Charizardite Y."
            }
    }

    if username in info:
        if password == info[username]["password"]:
            print("Successful")
            '''
                We can pass information from backend to frontend using the render_template method itself
                The LHS is the name by which the value is going to be accessed in the html page
                The RHS is the actual value of the variable
            '''
            return render_template('home.html', username=username, data=info[username]["data"])
        else:
            print("Enter the correct Password")
            return render_template('error_page.html', error="password")

    else:
        print("Enter valid username")
        return render_template('error_page.html', error="username")

    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)