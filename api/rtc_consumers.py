from channels.generic.websocket import AsyncWebsocketConsumer
import json

class WebRTCSignalingConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Extract room name from URL
        self.room_name = self.scope['url_route']['kwargs'].get('room_name', 'default_room')
        self.room_group_name = f'webrtc_{self.room_name}'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Parse the incoming WebRTC signaling message
        try:
            data = json.loads(text_data)
            signal_type = data.get('type')

            if signal_type == 'offer':
                # Handle WebRTC offer and send to other participants in the room
                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        'type': 'webrtc_offer',
                        'from': self.channel_name,
                        'offer': data['offer']
                    }
                )
            elif signal_type == 'answer':
                # Handle WebRTC answer and send to the offerer
                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        'type': 'webrtc_answer',
                        'from': self.channel_name,
                        'answer': data['answer']
                    }
                )
            elif signal_type == 'ice-candidate':
                # Handle ICE candidate and send to the relevant peer
                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        'type': 'webrtc_ice_candidate',
                        'from': self.channel_name,
                        'candidate': data['candidate']
                    }
                )
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

    async def webrtc_offer(self, event):
        # Relay the offer to all participants in the room except the sender
        await self.send(text_data=json.dumps({
            'type': 'offer',
            'from': event['from'],
            'offer': event['offer']
        }))

    async def webrtc_answer(self, event):
        # Relay the answer to the offerer
        await self.send(text_data=json.dumps({
            'type': 'answer',
            'from': event['from'],
            'answer': event['answer']
        }))

    async def webrtc_ice_candidate(self, event):
        # Relay the ICE candidate to the peer that needs it
        await self.send(text_data=json.dumps({
            'type': 'ice-candidate',
            'from': event['from'],
            'candidate': event['candidate']
        }))
