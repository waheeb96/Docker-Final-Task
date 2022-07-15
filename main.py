from website import init
from website import bitcoin

server = init.create_server()

@server.route('/')
def main():
    return bitcoin.show_content()

if __name__ == "__main__":
    server.run(debug = True ,port = 5000 ,host = "0.0.0.0")
