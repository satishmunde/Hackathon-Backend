from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Called when the WebSocket handshake is complete.
        # Here, you can perform actions like authentication or channel group joining.

        # For demonstration purposes, we will accept the connection and add it to a group.
        self.room_name = self.scope['url_route']['kwargs'].get('room_name', 'default_room')
        self.room_group_name = f'chat_{self.room_name}'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Called when the WebSocket disconnects.
        # Clean up resources or notify others about the disconnection.

        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

        # Optionally send a notification message to the group about the disconnection
        # await self.channel_layer.group_send(
        #     self.room_group_name,
        #     {
        #         'type': 'chat_message',
        #         'message': 'A user has disconnected.'
        #     }
        # )

    async def receive(self, text_data):
        # Process incoming messages from WebSocket
        try:
            text_data_json = json.loads(text_data)
            message_type = text_data_json.get('type', 'chat')
            message = text_data_json.get('message', '')

            if message_type == 'chat':
                # Broadcast message to room group
                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        'type': 'chat_message',
                        'message': f'{message} from Server !'
                    }
                )
            elif message_type == 'command':
                # Handle special commands if needed
                await self.send(text_data=json.dumps({
                    'type': 'command',
                    'message': f'Command received: {message}'
                }))
            else:
                # Handle unknown message types
                await self.send(text_data=json.dumps({
                    'type': 'error',
                    'message': 'Unknown message type'
                }))
        except json.JSONDecodeError:
            # Handle JSON decoding errors
            await self.send(text_data=json.dumps({
                'type': 'error',
                'message': 'Invalid message format'
            }))

    async def chat_message(self, event):
        # This method is called when a message is sent to the room group.
        message = event.get('message', '')

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'type': 'chat',
            'message': f'{message} from Server !'
        }))
