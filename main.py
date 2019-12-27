#!/usr/bin/env python3
import sys


clients = ['pablo', 'ricardo']

def create_client(client_name):
	global clients
	if client_name not in clients:
		clients.append(client_name)
	else:
		print('Client already exists')


def list_clients():
	global clients
	for idx, client in enumerate(clients):
		print('{}:{}'.format(idx, client))


def update_client(client_name, updated_client_name):
	global clients

	if client_name in client_name:
		index = clients.index(client_name)
		clients[index] = updated_client_name
	else:
		print('Clinet was not found')


def delete_client(client_name):
	global clients

	if client_name in clients:
		clients.remove(client_name)
	else:
		print('Client was not found')


def search_client(client_name):
	global clients
	for client in clients:
		if client != client_name:
			continue
		else:
			return True


def _print_welcome():
	print('WELCOME')
	print('*'*40)
	print('WHAT WOULD YOU DO')
	print('[L]list clients')
	print('[C]create client')
	print('[U]update client')
	print('[D]delete client')
	print('[S]search Client')


def _get_client_name():
	client_name = None

	while not client_name:
		client_name = input ('What is the client name?')

		if client_name == 'exit':
			client_name = None
			break

	if not client_name:
		sys.exit()

	return client_name


if __name__ == '__main__':
	_print_welcome()

	command = input()
	command = command.upper()

	if command == 'C':
		client_name = _get_client_name()
		create_client(client_name)
		list_clients()
	elif command == 'D':
		client_name = _get_client_name()
		delete_client(client_name)
		list_clients()
	elif command == 'U':
		client_name = _get_client_name()
		updated_clinet_name = input('What is the updated client name?')
		update_client(client_name, updated_clinet_name)		
		list_clients()
	elif command == 'S':
		client_name = _get_client_name()
		found = search_client(client_name)

		if found:
			print('The client was found')
		else:
			print('The client: {} was not found'.format(client_name))
	elif command == 'L':
		list_clients()
	else:
		print('invalid command') 