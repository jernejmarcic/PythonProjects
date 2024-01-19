from Website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True) # will auto re-run flask webserver on code change
