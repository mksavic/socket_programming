import re
import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip().decode('utf-8')
        print('{} wrote: {}'.format(self.client_address[0], self.data))

        if 'SECRET' in self.data:
            digits = ''.join(re.findall('\d+', self.data))
            count = sum(c.isdigit() for c in self.data)
            ret = 'Digits: {} Count: {}'.format(digits, count).encode('utf-8')
            self.request.sendall(ret)


if __name__ == '__main__':
    HOST, PORT = 'localhost', 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
        server.server_close()
