import Servidor as server

import Cliente

server.StartServer(('',5002))
server.ConnectClient()
print(server.WriteChat())

