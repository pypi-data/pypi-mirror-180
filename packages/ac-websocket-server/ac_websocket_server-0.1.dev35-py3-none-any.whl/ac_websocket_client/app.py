#!/usr/bin/env python

'''Assetto Corsa Websockets App'''

import asyncio
from datetime import datetime
import json
import sys
import tkinter as tk
from typing import Optional
import websockets

from ac_websocket_client import DEBUG
from ac_websocket_client.objects import APP_TITLE, DebugUI, \
    GriddedButton, GriddedEntry, GriddedFrame, GriddedLabel, GriddedListbox, TrafficLight
from ac_websocket_server.protocol import Protocol


class App(tk.Tk):
    '''Wrapper class for Tk app'''

    def __init__(self, loop, url=None):
        super().__init__()

        self.loop = loop
        self.protocol("WM_DELETE_WINDOW", self.stop_ui)

        self.consumer_queue = asyncio.Queue()
        self.producer_queue = asyncio.Queue()

        self.is_connected = False
        self.is_registered = False
        self.is_started = False
        self.is_tracking = False

        self.url = url
        self.websocket = None

        self.acws_connect_button = tk.StringVar(value='Connect')
        self.ac_game_button = tk.StringVar(value='Start Game')
        self.ac_lobby_button = tk.StringVar(value='(Re)register')
        self.tracker_button = tk.StringVar(value='Start Tracker')

        self.acws_traffic_light: Optional[TrafficLight] = None
        self.ac_game_traffic_light: Optional[TrafficLight] = None
        self.ac_lobby_traffic_light: Optional[TrafficLight] = None
        self.tracker_traffic_light: Optional[TrafficLight] = None

        self.url_entry = tk.StringVar()

        self.game_timestamp_entry = tk.StringVar()
        self.registered_entry = tk.StringVar()
        self.track_entry = tk.StringVar()
        self.cars_entry = tk.StringVar()

        self.tracker_timestamp_entry = tk.StringVar()

        if self.url:
            self.url_entry.set(self.url)

        self.tasks = []

        self._create_ui()

    def _create_ui(self):
        '''Build the UI elements'''

        self.title(APP_TITLE)
        self.config(bg='lightgray')
        self.columnconfigure(0, weight=1)

        # ACWS Frame
        self.rowconfigure(0, weight=1)

        acws_frame = GriddedFrame.create(row=0, column=0, height=0.5)
        GriddedLabel.create(acws_frame, row=0, column=0, text="ACWS")
        GriddedLabel.create(acws_frame, row=0, column=1, text="url:")
        GriddedEntry.create(acws_frame, row=0, column=2,
                            textvariable=self.url_entry)
        GriddedButton.create(acws_frame, row=0, column=3,
                             textvariable=self.acws_connect_button, width=10,
                             command=lambda: self.loop.create_task(self._toggle_connection()))
        self.acws_traffic_light = TrafficLight(acws_frame, row=0, column=4)

        GriddedFrame.columnconfigure(acws_frame, 1, 1, 4, 1, 1)

        # AC Frame
        self.rowconfigure(1, weight=4)

        ac_frame = GriddedFrame.create(row=1, column=0, height=2)
        GriddedLabel.create(ac_frame, row=0, column=0, text="Game")
        GriddedLabel.create(ac_frame, row=0, column=1, text="started:")
        GriddedEntry.create(ac_frame, row=0, column=2,
                            textvariable=self.game_timestamp_entry)
        GriddedLabel.create(ac_frame, row=1, column=1, text="registered:")
        GriddedEntry.create(ac_frame, row=1, column=2,
                            textvariable=self.registered_entry)
        GriddedLabel.create(ac_frame, row=2, column=1, text="track:")
        GriddedEntry.create(ac_frame, row=2, column=2,
                            textvariable=self.track_entry)
        GriddedLabel.create(ac_frame, row=3, column=1, text="cars:")
        GriddedEntry.create(ac_frame, row=3, column=2,
                            textvariable=self.cars_entry)
        GriddedButton.create(ac_frame, row=0, column=3,
                             textvariable=self.ac_game_button, width=10,
                             command=lambda: self.loop.create_task(self._toggle_game()))
        self.ac_game_traffic_light = TrafficLight(ac_frame, row=0, column=4)
        GriddedButton.create(ac_frame, row=1, column=3,
                             textvariable=self.ac_lobby_button, width=10,
                             command=lambda: self.loop.create_task(self._toggle_registration()))
        self.ac_lobby_traffic_light = TrafficLight(ac_frame, row=1, column=4)

        GriddedFrame.columnconfigure(ac_frame, 1, 1, 4, 1, 1)

        # Tracker Frame
        self.rowconfigure(2, weight=1)

        tracker_frame = GriddedFrame.create(row=2, column=0)
        GriddedLabel.create(tracker_frame, row=0, column=0, text="Tracker")
        GriddedLabel.create(tracker_frame, row=0, column=1, text="started:")
        GriddedEntry.create(tracker_frame, row=0, column=2,
                            textvariable=self.tracker_timestamp_entry)
        GriddedButton.create(tracker_frame, row=0, column=3,
                             textvariable=self.tracker_button, width=10,
                             command=lambda: self.loop.create_task(self._start_tracker()))
        self.tracker_traffic_light = TrafficLight(
            tracker_frame, row=0, column=4)

        # Console Frame
        self.rowconfigure(3, weight=4)

        console_frame = GriddedFrame.create(row=3, column=0, height=3)
        listbox = GriddedListbox.create(console_frame)

        self.tasks.append(self.loop.create_task(self._monitor(listbox)))

        if DEBUG:
            self.update()
            DebugUI.print_window_info(self, 0)

    async def _handler(self, websocket):
        '''Handle websocket tasks'''
        consumer_task = asyncio.create_task(self._handler_consumer(websocket))
        producer_task = asyncio.create_task(self._handler_producer(websocket))
        _done, pending = await asyncio.wait(
            [consumer_task, producer_task],
            return_when=asyncio.FIRST_COMPLETED,
        )
        for task in pending:
            task.cancel()

    async def _handler_consumer(self, websocket):
        '''Handle messages received from websocket'''
        async for msg in websocket:
            await self.consumer_queue.put(msg)

    async def _handler_producer(self, websocket):
        '''Handle messages received to send on websocket'''
        while True:
            try:
                message = await self.producer_queue.get()
                await websocket.send(message)
            except Exception:
                print('\n> Connection Closing', file=sys.stderr)
                return

    async def _monitor(self, listbox: tk.Listbox):
        '''Monitor incoming messages and send to connection listbox'''
        while True:
            try:
                input_line = json.loads(await self.consumer_queue.get())
                output_fmt = {'fg': 'Black'}
                output_lines = ''
                if error_msg := input_line.get('error', None):
                    if error_msg['msg'] == 'ERROR,INVALID SERVER,CHECK YOUR PORT FORWARDING SETTINGS':
                        self.is_registered = False
                        self.ac_lobby_traffic_light.red()
                    output_fmt = {'fg': 'Red'}
                    output_lines = json.dumps(error_msg, indent=4)
                if success_msg := input_line.get('data', None):
                    if server_msg := success_msg.get('lobby', None):
                        if server_msg['connected']:
                            self.is_registered = True
                            self.registered_entry.set(
                                datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                            self.ac_lobby_traffic_light.green()
                        else:
                            self.is_registered = False
                            self.registered_entry.set('')
                            self.ac_lobby_traffic_light.red()
                    if server_msg := success_msg.get('server', None):
                        self.game_timestamp_entry.set(server_msg['timestamp'])
                        self.track_entry.set(server_msg['track'])
                        self.cars_entry.set(server_msg['cars'])
                        self.ac_game_traffic_light.green()
                    output_fmt = {'fg': 'Green'}
                    output_lines = json.dumps(success_msg, indent=4)
                output_timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                for output_line in output_lines.split('\n'):
                    listbox.insert(
                        tk.END, f'{output_timestamp}: {output_line}')
                    listbox.itemconfig(tk.END, output_fmt)
                listbox.yview(tk.END)
            except Exception as err:
                print(err)
                raise

    async def start_ui(self, interval=1/120):
        '''Start a the update of the UI'''
        while True:
            self.update()
            await asyncio.sleep(interval)

    def stop_ui(self):
        '''Cleanup all tasks'''
        for task in self.tasks:
            task.cancel()
        self.loop.stop()
        self.destroy()

    async def _toggle_connection(self, url=None):
        '''Connect to the websocket server'''

        if not url:
            url = self.url_entry.get()

        if not url:
            url = self.url

        if self.is_connected:
            await self.websocket.close()
            return

        try:
            async with websockets.connect(url) as websocket:
                self.url = url
                self.url_entry.set(url)
                self.title(f'{APP_TITLE} - Connected to {url}')
                self.acws_connect_button.set('Disconnect')
                self.acws_traffic_light.green()
                self.is_connected = True
                self.websocket = websocket
                await self._handler(websocket)
                await self.consumer_queue.put(Protocol.success(msg=f'Disconnecting from {url}'))
                self.is_connected = False
                self.title(f'{APP_TITLE}')
                self.acws_connect_button.set('Connect')
                self.acws_traffic_light.red()
        except OSError as error:
            await self.consumer_queue.put(Protocol.error(msg=str(error)))

    async def _toggle_game(self):
        '''Start the game'''

        if self.is_connected:
            if not self.is_started:
                await self.websocket.send('server start')
                self.is_started = True
                self.ac_game_button.set('Stop Game')
            else:
                await self.websocket.send('server stop')
                self.is_started = False
                self.ac_game_button.set('Start Game')
                self.ac_game_traffic_light_canvas.itemconfigure(
                    self.acws_traffic_light, fill='red')
        else:
            await self.consumer_queue.put(Protocol.error('Not connected to ACWS server'))

    async def _toggle_registration(self):
        '''(Re)-register in lobby'''

        if self.is_connected:
            await self.websocket.send('lobby restart')
        else:
            await self.consumer_queue.put(Protocol.error('Not connected to ACWS server'))

    async def _toggle_tracker(self):
        '''Toggle tracker'''

        if self.is_connected:
            await self.websocket.send('tracker start')
        else:
            await self.consumer_queue.put(Protocol.error('Not connected to ACWS server'))
