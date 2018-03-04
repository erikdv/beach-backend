from backend import app

# script for deployment

set_up()

if __name__ == '__main__':
    app.run(use_reloader=False)

