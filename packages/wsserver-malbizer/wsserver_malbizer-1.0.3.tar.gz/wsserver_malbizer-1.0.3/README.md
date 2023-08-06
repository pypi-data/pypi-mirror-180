## Python Package for Websocket Server Live

* WebsocketServer built in python.

* For active server on command line:
    - Install package with PIP;
    - Run command wsserver-malbizer '<port>'
    - Send JSON string for serve on model:

        {
            "subject": "subject for your message",
            "sender": "id_sender",
            "topic": [], //List of topics to inscribe message
            "payload": "Value for your message (JSON string)",
            "persist": false //indicate if message is persisted and send for new clients
        }



* For using on python file:

    - Import wsservermalbizer with WebsocketServer and use the code:

        WebSocketServer(port=port).start()
