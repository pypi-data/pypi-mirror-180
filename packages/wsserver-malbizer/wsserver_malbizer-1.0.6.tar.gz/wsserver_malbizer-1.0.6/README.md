## Python Package for Websocket Server Live

# WebsocketServer built in python.

# For active server on command line:
    - Install package with PIP;
    - Run command wsserver-malbizer 'port_value_numerical'
    - Send JSON string for serve on model:

        {
            "subject": "subject for your message",
            "sender": "id_sender",
            "topic": [], //List of topics to inscribe message
            "payload": "Value for your message (JSON string)",
            "persist": false //indicate if message is persisted and send for new clients
        }



# For using on python file:

    - Import wsservermalbizer with WebsocketServer and use the code:

        WebSocketServer(port=port).start()

# For use Client (command-line):
    - Run command (if port_value_numerical is 7135):

        wsclient-malbizer "ws://localhost:7135" "topic"

    - watch for messages on server websocket;

# For use Message Sender (command-line):

    - Run command (if port_value_numerical is 7135):

        wssend-malbizer "ws://localhost:7135" "payload" "subject" "user" "topics,separed,with,comma"


    - await command send for server;


# For use Client (python file):

    - Import wsservermalbizer with WebsocketClientReceiver and use the code (if port_value_numerical is 7135):

        WebsocketClientReceiver("ws://localhost:7135","topics,separed,with,comma,for,subscribe").receiver()


# For use Message Sender (python file):

    - Import wsservermalbizer with WebsocketClientReceiver and use the code (if port_value_numerical is 7135):

        client = WebsocketClientMessage()
        client.sender = "user"
        client.subject = "subject"
        client.payload = "payload JSON"
        client.topics = ["topics","to","send"]
        client.persist = False //True if you need persistance

        sender = WebsocketClientSender(client, "ws://localhost:7135")

        sender.send()